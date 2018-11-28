#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int main() {
  freopen("B-large.in", "r", stdin);
  freopen("B.out", "w", stdout);
  int totCas;
  scanf("%d", &totCas);
  for (int cas = 1; cas <= totCas; cas++) {
    double C, F, X;
    scanf("%lf%lf%lf", &C, &F, &X);
    double cur = 2, spend = 0;
    double ans = X / cur;
    double prev = ans;
    for (int cnt = 0; ; cnt++) {
      spend += C / cur;
      cur += F;

      ans = min(ans, spend + X / cur);

      if (spend + X / cur > prev) {
        break;
      }
      prev = spend + X / cur;
    }
    printf("Case #%d: %.10f\n", cas, ans);
  }
  return 0;
}

