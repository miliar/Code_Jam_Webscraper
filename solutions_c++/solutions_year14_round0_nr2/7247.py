#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <set>
using namespace std;

int main() {
  int TC = 1, T;
  double C, F, X;
  scanf("%d", &T);
  while(T--) {
    scanf("%lf%lf%lf", &C, &F, &X);
    double t = X/2, t1=0, cc = 2;
    while (1) {
      t1 += C/cc;
      cc+=F;
      double tmp = t1 + X/cc;
      if (tmp < t) t = tmp;
      else break;
    }
    printf("Case #%d: %.16lf\n", TC++, t);
  }
}