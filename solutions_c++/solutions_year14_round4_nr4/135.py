#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

struct Node {
  int val, depth;
  bool present;
  Node *children[26];

  int num_shards;
  bool full;

  Node(int val_, int depth_) : val(val_), depth(depth_) {
    num_shards = -1;
    present = full = false;
    for (int i = 0; i < 26; i++)
      children[i] = NULL;
  }

  void clear() {
    for (int i = 0; i < 26; i++) {
      if (children[i] != NULL) {
        children[i]->clear();
        delete children[i];
      }
    }
  }
};

// TODO: track size
void add_to_dict(Node *r, string s) {
  Node *cur = r;
  for (int i = 0; i < s.length(); i++) {
    int val = s[i] - 'A';
    if (!(cur->children[val]))
      cur->children[val] = new Node(val, cur->depth + 1);
    cur = cur->children[val];
  }
  cur->present = true;
}

const long long P = 1000000007;
const int N_MAX = 108;
const int M_MAX = 1024;

long long _factorial[M_MAX];
long long factorial(long long n) {
  assert(0 <= n && n < M_MAX);
  if (n == 0)
    return 1;
  if (_factorial[n] == -1) {
    _factorial[n] = (factorial(n - 1) * n) % P;
  }
  return _factorial[n];
}

long long _binom[M_MAX][M_MAX];
long long binom(long long n, long long k) {
  assert(n >= 0);
  if (n < k)
    return 0;
  if (k == 0)
    return 1;

  if (_binom[n][k] == -1) {
    _binom[n][k] = (binom(n - 1, k - 1) + binom(n - 1, k)) % P;
  }
  return _binom[n][k];
}

long long ways_to_place(const vector<int> &groups, int n) {
  long long ret = 1;
  for (int i = 0; i < groups.size(); i++)
    ret = (ret * binom(n, groups[i])) % P;
  return ret;
}

long long ways_to_cover(const vector<int> &sizes, int n) {
  long long ret = 0;
  long long sign = 1;
  for (int i = n; i > 0; i--) {
    long long amt = (binom(n, i) * ways_to_place(sizes, i)) % P;
    ret += (sign * amt + P) % P;
    ret %= P;
    sign = -sign;
  }
  return ret;
}

int N, M;
Node *root = NULL;
long long num_ways;
int max_nodes;

void multiply_answer(long long factor) {
  num_ways = (num_ways * factor) % P;
}

void init() {
  num_ways = 1;
  max_nodes = 0;

  if (root) {
    root->clear();
    delete root;
  }
  root = new Node(-1, 0);

  cin >> M >> N;
  string s;
  for (int i = 0; i < M; i++) {
    cin >> s;
    add_to_dict(root, s);
  }
}

void recurse_node(Node *cur) {
  vector<int> groups;
  int tot_shards = 0;

  if (cur->present) {
    groups.push_back(1);
    tot_shards++;
  }

  for (int i = 0; i < 26; i++) {
    Node *child = cur->children[i];
    if (!child)
      continue;
    recurse_node(child);

    if (child->full)
      cur->full = true;
    groups.push_back(child->num_shards);
    tot_shards += child->num_shards;
  }
  max_nodes += min(tot_shards, N);

  if (cur->full) {
    // a child is full
    cur->num_shards = N;
    for (int i = 0; i < 26; i++) {
      Node *child = cur->children[i];
      if (child && (!(child->full)))
        multiply_answer(binom(N, child->num_shards));
    }
    if (cur->present)
      multiply_answer(N);
    return;
  }

  if (tot_shards < N) {
    cur->num_shards = tot_shards;
    // fix ordering
    multiply_answer(ways_to_cover(groups, tot_shards));
    return;
  }

  cur->full = true;
  multiply_answer(ways_to_cover(groups, N));
  cur->num_shards = N;
}

void solve_case(int t) {
  init();
  recurse_node(root);
  cout << "Case #" << t << ": "
       << max_nodes << " " << num_ways << "\n";
}

int main() {
  for (int i = 0; i < M_MAX; i++) {
    _factorial[i] = -1;
    for (int j = 0; j < M_MAX; j++) {
      _binom[i][j] = -1;
    }
  }

  /*
  vector<int> g;
  g.push_back(3);
  g.push_back(3);
  g.push_back(3);
  cout << binom(9, 3) << endl;
  cout << ways_to_place(g, 9) << endl;
  cout << ways_to_cover(g, 9) << endl;
  */

  int T;
  cin >> T;

  for (int i = 0; i < T; i++) {
    solve_case(i + 1);
  }

  return 0;
}
