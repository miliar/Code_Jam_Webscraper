// #define PRETEST
#include <string>
#include <string.h>
#include <iostream>
#include <stdio.h>
#include <set>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

int main(void) {
#ifdef PRETEST
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
#endif
  int T;
  double C, F, X;
  scanf("%d", &T);
  for (int z = 1; z <= T; ++z) {
    scanf("%lf%lf%lf", &C, &F, &X);
    int k = X / C - 2.0 / F;
    double t = 0.0;
    double f = 2.0;
    for (int i = 1; i <= k; ++i) {
      t += C / f;
      f += F;
    }
    t += X / f;
    printf("Case #%d: %.7lf\n", z, t);
  }
  return 0;
}
