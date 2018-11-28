#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>

using namespace std;

const int MAX_LEN = 50 + 5;
const int MAX_DIST = 6;

struct Node {
  bool final;
  Node* next[26];
  int dp[MAX_LEN][MAX_DIST];
  Node() {
    memset(next, 0, sizeof(next));
    memset(dp, -1, sizeof(dp));
  }
  ~Node() {
    for (int i = 0; i < 26; ++i) {
      if (next[i]) {
        delete next[i];
      }
    }
  }

  void reset() {
    memset(dp, -1, sizeof(dp));
    for (int i = 0; i < 26; ++i) {
      if (next[i]) {
        next[i]->reset();
      }
    }
  }
};

struct Trie {
  Node* root;
  int states;
  Trie(): root(new Node), states(1) {
  }

  ~Trie() {
    delete root;
    // TODO: delete all the stuff.
  }

  void reset() {
    root->reset();
  }

  void insert(const char* word) {
    const char* cur = word;
    Node* node = root;
    while (*cur && *cur >= 'a' && *cur <= 'z') {
      if (!node->next[*cur - 'a']) {
        node->next[*cur - 'a'] = new Node;
        ++states;
      }
      node = node->next[*cur - 'a'];
      ++cur;
    }
    node->final = true;
  }
};

Trie t;
string s;

int rec(Node* node, int pos, int dist) {
  if (pos == s.size()) {
    return (node->final || node == t.root) ? 0 : 1000;
  }
  if (dist > 5) {
    dist = 5;
  }
  int& ret = node->dp[pos][dist];
  if (ret != -1) {
    return ret;
  }
  ret = 1000;
  if (node->final) {
    ret = rec(t.root, pos, dist);
  }
  if (dist == 5) {
    for (int i = 0; i < 26; ++i) {
      if (!node->next[i]) {
        continue;
      }
      ret = min(ret, rec(node->next[i], pos + 1, 1) + 1);
    }
  }
  if (node->next[s[pos] - 'a']) {
    ret = min(ret, rec(node->next[s[pos] - 'a'], pos + 1, dist + 1));
  }
//  printf("ret is %d\n", ret);
  return ret;
}

int main() {
  freopen("/dev/null", "w", stderr);
  int T;
  scanf("%d", &T);
  char buffer[MAX_LEN];
  FILE* dict = fopen("dict.txt", "r");
  char buf[20];
  while (fgets(buf, 20, dict)) {
    t.insert(buf);
  }
  for (int test = 0; test < T; ++test) {
    t.reset();
    fprintf(stderr, "%d states\n", t.states);
    scanf("%s", buffer);
    s = buffer;
    printf("Case #%d: %d\n", test + 1, rec(t.root, 0, 5));
//    printf("searching for cuisi\n");
//    printf("codecuisi: %d\n", rec(t.root, s.size() - 9, 0));
  }
}
