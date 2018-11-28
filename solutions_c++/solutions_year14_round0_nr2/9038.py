#include <stdio.h>

int main() {
  int T;
  double C, F, X;
  scanf("%d", &T);
  double res, sum, tmp;
  double f = 2.0;
  int i;
  for (i = 1;i <= T; ++i) {
    scanf("%lf %lf %lf", &C, &F, &X);
    sum = 0;
    res = 10000000;
    f = 2.0;
    while (res > sum) {
      tmp = X/f;
      if (sum + tmp < res) res = sum + tmp;
      sum += C/f;
      f += F;
    }
    printf("Case #%d: %07f\n", i, res); 
  }
  return 0;
}

