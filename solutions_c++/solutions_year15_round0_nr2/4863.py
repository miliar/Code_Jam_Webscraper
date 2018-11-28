#include <stdio.h>

int main() {
  int T;
  int D, P[1000];
  scanf("%d", &T);
  int res, sum, max = 1;
  int i, j, k;
  for (i = 1;i <= T; ++i) {
    scanf("%d", &D);
    max = 1;
    res = 1000000000;
    for (j = 0;j < D; ++j) {
      scanf("%d", &P[j]);
      max = max > P[j] ? max : P[j];
    }
    res = max;
    // j is amount
    for (j = 2;j <= max; ++j) {
      sum = j;
      for (k = 0;k < D; ++k) {
        if (P[k] <= j) continue;
        sum += (P[k] + j-1)/j-1;
      }
      if (sum <  res) res = sum;
    }
    printf("Case #%d: %d\n", i, res); 
  }
  return 0;
}

