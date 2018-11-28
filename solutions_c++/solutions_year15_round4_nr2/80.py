#include <algorithm>
#include <cassert>
#include <cstring>
#include <iostream>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

typedef long long llint;
typedef long double ldb;

const int MAX = 110;
const ldb eps = 1e-12;

bool lt(ldb a, ldb b) { return a+eps < b; }
bool gt(ldb a, ldb b) { return lt(b, a); }
bool eq(ldb a, ldb b) { return !lt(a, b) && !lt(b, a); }

ldb R[MAX], C[MAX];
int n;
ldb V, X;

ldb solve() {
  if (n == 1) {
    if (!eq(X, C[0])) return -1;
    return V / R[0];
  }

  if (eq(C[0], C[1])) {
    if (!eq(X, C[0])) return -1;
    return V / (R[0] + R[1]);
  }

  ldb V1 = (X - C[0]) / (C[1] - C[0]) * V;
  ldb V0 = V - V1;
  if (lt(V0, 0) || lt(V1, 0)) return -1;
  return max(V1 / R[1], V0 / R[0]);
}

int main(void) {
  int TC;
  scanf("%d", &TC);
  for (int tp = 1; tp <= TC; ++tp, fflush(stdout)) {
    scanf("%d", &n);
    scanf("%Lf %Lf", &V, &X);
    REP(i, n) scanf("%Lf %Lf", R+i, C+i);
    
    printf("Case #%d: ", tp);
    ldb ans = solve();
    if (ans < -eps) puts("IMPOSSIBLE"); else
      printf("%.10Lf\n", ans);
  }
  return 0;
}
