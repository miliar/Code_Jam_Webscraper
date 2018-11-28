#include <cstdio>
#include <cstring>
#include <cassert>

#include <algorithm>
#include <iostream>
#include <set>
using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

typedef long long llint;

const int MAX = 110;
const int mod = int(1e9) + 7;

int R, C;
int g[MAX][MAX];

// llint solve(int R, int C) {
//   llint ret = 0;
//   if (R % 3 != 1) ++ret;
//   if (R % 3 != 2) ++ret;
//   ret %= mod;
//   return ret;
// }

bool good(int a, int b) {
  int cnt = 0;
  cnt += g[a][(b+1)%C] == g[a][b];
  cnt += g[a][(b-1+C)%C] == g[a][b];
  if (a > 0) cnt += g[a-1][b] == g[a][b];
  if (a+1 < R) cnt += g[a+1][b] == g[a][b];
  return cnt == g[a][b];
}

set<llint> bio;

bool check() {
  REP(off, C) {
    llint h = 0;
    REP(i, R) REP(j, C) h = (h*10007 + g[i][(off+j)%C]) % mod;
    if (bio.count(h)) return false;
  }
  REP(off, C) {
    llint h = 0;
    REP(i, R) REP(j, C) h = (h*10007 + g[i][(off+j)%C]) % mod;
    bio.insert(h);
  }

  REP(a, R) REP(b, C) if (!good(a, b)) return false;
  return true;
}

int rec(int a, int b) {
  if (b == C) ++a, b = 0;
  if (a == R) {
    if (!check()) return 0;
    // puts("----");
    // REP(i, R) {
      // REP(j, C) printf("%d", g[i][j]);
      // puts("");
    // }
    return 1;
  }

  if (a && b && !good(a-1, b-1)) return false;

  int ret = 0;
  for (int i = 1; i <= 4; ++i) {
    g[a][b] = i;
    ret += rec(a, b+1);
  }
  return ret;
}


int main() {
  int T;
  scanf("%d", &T);
  for (int tt = 1; tt <= T; ++tt, fflush(stdout)) {
    scanf("%d%d", &R, &C);
    // printf("Case #%d: %lld\n", tt, solve(R, C));
    bio.clear();
    printf("Case #%d: %d\n", tt, rec(0, 0));
  }
  return 0;
}
