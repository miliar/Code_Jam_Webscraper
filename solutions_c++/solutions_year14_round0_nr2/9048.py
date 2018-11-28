#include <cstdio>
#include <cassert>

#include <iostream>
#include <algorithm>
using namespace std;

#define TRACE(x) cerr << #x << " = " << (x) << endl
#define REP(i, n) for (int i = 0; i < (n); ++i)
#define SZ(c) ((int) (c).size())

typedef long long llint;

int main() {
  int T;
  scanf("%d", &T);
  for (int tt = 1; tt <= T; ++tt) {
    double C, F, X;
    scanf("%lf%lf%lf", &C, &F, &X);

    double S = 2;
    double t = 0;
    double ans = X / S;

    REP(iter, 1000000) {
      t += C / S;
      S += F;
      ans = min(ans, t + X / S);
    }

    printf("Case #%d: %lf\n", tt, ans);
  }
  return 0;
}
