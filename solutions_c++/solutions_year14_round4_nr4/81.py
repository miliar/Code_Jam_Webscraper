#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <iostream>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <utility>
#include <numeric>
#include <algorithm>
#include <bitset>
#include <complex>
#include <array>

using namespace std;

typedef unsigned uint;
typedef long long Int;

const int INF = 1001001001;
const Int INFLL = 1001001001001001001LL;

template<typename T> void pv(T a, T b) { for (T i = a; i != b; ++i) cout << *i << " "; cout << endl; }
template<typename T> void chmin(T& a, T b) { if (a > b) a = b; }
template<typename T> void chmax(T& a, T b) { if (a < b) a = b; }
int in() { int x; scanf("%d", &x); return x; }

const Int MO = 1000000007;
Int comb[32][32];

void precalc() {
  comb[0][0] = 1;
  for (int i = 1; i < 32; ++i) {
    comb[i][0] = comb[i][i] = 1;
    for (int j = 1; j < i; ++j) {
      comb[i][j] = comb[i - 1][j] + comb[i - 1][j - 1];
      comb[i][j] %= MO;
    }
  }
}

int M, N;
string S[1024];

struct trie {
  int num, leaf;
  int next[26];
  trie() {
    num = leaf = 0;
    for (int i = 0; i < 26; ++i) next[i] = -1;
  }
} pool[200000];

int allocated;

void init() { 
  allocated = 0;
  for (int i = 0; i < 200000; ++i) {
    pool[i] = trie();
  }
}
int alloc() { return allocated++; }
void insert(int t, const string& s) {
  for (int i = 0; i < s.size(); ++i) {
    int c = s[i] - 'A';
    ++pool[t].num;
    if (pool[t].next[c] == -1) {
      pool[t].next[c] = alloc();
    }
    t = pool[t].next[c];
  }
  ++pool[t].num;
  pool[t].leaf = 1;
}

int solve1(int t) {
  int res = 0;
  for (int i = 0; i < 26; ++i) {
    if (pool[t].next[i] != -1) {
      res += solve1(pool[t].next[i]);
    }
  }
  return res + min(N, pool[t].num);
}

Int dfs(int t) {
  vector<Int> r;
  vector<int> cols;
  for (int i = 0; i < 26; ++i) {
    if (pool[t].next[i] != -1) {
      r.push_back(dfs(pool[t].next[i]));
      cols.push_back(min(N, pool[pool[t].next[i]].num));
    }
  }

  if (pool[t].leaf) {
    r.push_back(1);
    cols.push_back(1);
  }

  int need = min(N, pool[t].num);
  Int res = 0;
  for (int ign = 0; ign < need; ++ign) {
    Int tmp = 1;
    for (int i = 0; i < r.size(); ++i) {
      if (need - ign < cols[i]) {
        tmp = 0;
        break;
      }
      tmp = tmp * r[i] % MO * comb[need - ign][cols[i]] % MO;
    }
    tmp = tmp * comb[need][ign] % MO;
    if (ign % 2 == 0) {
      res = (res + tmp) % MO;
    } else {
      res = (res - tmp + MO) % MO;
    }
  }

  return res;
}

void solve() {
  M = in();
  N = in();
  for (int i = 0; i < M; ++i) {
    char buf[128];
    scanf("%s", buf);
    S[i] = buf;
  }

  init();
  int root = alloc();
  for (int i = 0; i < M; ++i) {
    insert(root, S[i]);
  }

  int sol1 = solve1(root);
  Int res = dfs(root);
  res = (res * comb[N][min(N, pool[root].num)] % MO);
  printf("%d %lld\n", sol1, res);
}

int main()
{
  int T = in();
  precalc();

  for (int CN = 1; CN <= T; ++CN) {
    printf("Case #%d: ", CN);
    solve();
  }

  return 0;
}
