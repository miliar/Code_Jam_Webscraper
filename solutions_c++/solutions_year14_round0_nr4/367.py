#include <algorithm>
#include <stdio.h>
#include <string.h>

double n[1000], k[1000];
int T, i, N, j, w, dw;

int main ()
{
  int m;
  scanf ("%d", &T);
  for (i = 1; i <= T; i++) {
    scanf ("%d", &N);
    for (j = 0; j < N; j++) scanf ("%lf", &n[j]);
    for (j = 0; j < N; j++) scanf ("%lf", &k[j]);
    std::sort (n, n + N);
    std::sort (k, k + N);
    m = 0;
    w = N;
    for (j = 0; j < N; j++) {
      for (; m < N && k[m] < n[j]; m++) {}
      if (m < N) w--;
      m++;
    }
    dw = 0;
    m = 0;
    for (j = 0; j < N; j++) {
      for (; m < N && n[m] < k[j]; m++) {}
      if (m < N) dw++;
      m++;
    }
    printf ("Case #%d: %d %d\n", i, dw, w);
  }
}
