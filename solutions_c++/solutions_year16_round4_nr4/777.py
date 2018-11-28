#include <bits/stdc++.h>

using namespace std;

typedef long long LL;
const int maxint = 0x7f7f7f7f, mod = 1000000007;
const double eps = 1e-8, pi = acos(-1.0);

void rd() { }
template<typename... T> void rd(int &h, T &... t) { scanf("%d", &h); rd(t...); }
template<typename... T> void rd(long long &h, T &... t) { scanf("%lld", &h); rd(t...); }
template<typename... T> void rd(double &h, T &... t) { scanf("%lf", &h); rd(t...); }

const int maxN = 5;
int tests, n;
bool was[maxN][maxN], cur[maxN][maxN];
bool used[maxN];
int order[maxN];
bool gflag;

void dfs(int d) {
  if (gflag) return;
  if (d == n+1) return;
  int x = order[d];
  bool found = false;
  for (int y = 1; y <= n; ++y) {
    if (cur[x][y] && !used[y]) {
      found = true;
      used[y] = true;
      dfs(d+1);
      used[y] = false;
    }
  }
  if (!found) gflag = true;
}

bool test() {
  for (int i = 1; i <= n; ++i) {
    order[i] = i;
  }
  do {
    gflag = false;
    memset(used, 0, sizeof(used));
    dfs(1);
    if (gflag) return false;  
  } while (next_permutation(order + 1, order + 1 + n));
  return true;
}

bool solve(int mask) {
  int mask2 = mask;
  memset(cur, 0, sizeof(cur));
  for (int i = 1; i <= n; ++i) {
    for (int j = 1; j <= n; ++j) {
      int x = mask2 & 1;
      if (x && was[i][j]) return false;
      cur[i][j] = x | was[i][j];
      mask2 >>= 1;
    }
  }
  return test();
}

int main() {
  freopen("D-small-attempt0.in", "r", stdin);

  rd(tests);
  for (int tt = 1; tt <= tests; ++tt) {
    cerr << tt << endl;
    rd(n);
    for (int i = 1; i <= n; ++i) {
      getchar();
      for (int j = 1; j <= n; ++j) {
        char ch;
        scanf("%c", &ch);
        was[i][j] = (ch == '1' ? true : false);
      }
    }
    int ret = maxint;
    for (int mask = 0; mask < (1 << (n*n)); ++mask) {
      if (solve(mask)) ret = min(ret, __builtin_popcount(mask));
    }
    printf("Case #%d: %d\n", tt, ret);
  }

  return 0;
}
