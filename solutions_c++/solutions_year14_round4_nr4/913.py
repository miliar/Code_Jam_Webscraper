#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

struct Trie {
  struct Node;
  struct Node {
    char ch;
    Node *children[26];
    Node(char ch_) : ch(ch_) {
      for (int i = 0; i < 26; i++)
        children[i] = NULL;
    };
    ~Node() {
      for (int i = 0; i < 26; i++)
        if (children[i])
          delete children[i];
    }
  };
  Node root;
  int node_count;
  Trie() : root('\0'), node_count(1) {};
  void add(string &s) {
    Node *cur = &root;
    for (int i = 0; i < s.size(); i++) {
      int ch = s[i] - 'A';
      if (!cur->children[ch]) {
        cur->children[ch] = new Node(ch);
        node_count++;
      }
      cur = cur->children[ch];
    }
  }
};

int M, N;
string S[8];

void dfs(set<vector<int>> &met, vector<int> &b, vector<int> &a, int &cur_max, int &cur_max_count) {
  if (b.size() > N) {
    // A arrangement;
    int count = 0;
    vector<int> key;
    for (int i = 1; i < b.size(); i++) {
      vector<int> sub_key;
      for (int j = b[i-1]; j < b[i]; j++)
        sub_key.push_back(a[j]);
      sort(sub_key.begin(), sub_key.end());
      for (int i = 0; i < sub_key.size(); i++)
        key.push_back(sub_key[i]);
      key.push_back(-1);
    }
    if (met.find(key) != met.end())
      return;
    met.insert(key);
    for (int i = 1; i < b.size(); i++) {
      Trie t;
      for (int j = b[i-1]; j < b[i]; j++)
        t.add(S[a[j]]);
      count += t.node_count;
    }
    if (count > cur_max) {
      cur_max = count;
      cur_max_count = 0;
    }
    if (count == cur_max) {
      cur_max_count++;
    }
    return;
  }
  if (b.size() == N) {
    b.push_back(a.size());
    dfs(met, b, a, cur_max, cur_max_count);
    b.pop_back();
  } else {
    for (int i =  b.back() + 1; i < M; i++) {
      b.push_back(i);
      dfs(met, b, a, cur_max, cur_max_count);
      b.pop_back();
    }
  }
}

int main() {
  int T;
  cin >> T;
  #pragma omp for
  for (int CASE = 1; CASE <= T; CASE++) {
    cin >> M >> N;
    vector<int> a(M);
    for (int i = 0; i < M; i++) {
      cin >> S[i];
      a[i] = i;
    }
    set<vector<int>> met;
    int cur_max = 0, cur_max_count = 0;
    do {
      vector<int> b(1);
      dfs(met, b, a, cur_max, cur_max_count);
    } while (next_permutation(a.begin(), a.end()));
    cout << "Case #" << CASE << ": " << cur_max << " " << cur_max_count << endl;
  }
}
