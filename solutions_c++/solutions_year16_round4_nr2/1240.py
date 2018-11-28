#include <bits/stdc++.h>
using namespace std;
int main ()
{
  int t, i, k, n, j, l;
  scanf ("%d", &t);
  for (i = 1; i <= t; i++) {
    scanf ("%d%d", &n, &k);
    double p[200], best = 0, p2[200];
    for (j = 0; j < n; j++) scanf ("%lf", &p[j]);
    for (j = 0; j < (1<<n); j++) {
      if (__builtin_popcount (j) == k) {
        int m = 0;
        for (l = 0; l < n; l++) if (j & (1<<l)) p2[m++] = p[l];
        double x = 0;
        for (l = 0; l < (1<<k); l++) {
          if (__builtin_popcount (l) == k / 2) {
            double v = 1;
            int o;
            for (o = 0; o < k; o++) v *= (l & (1<<o)) ? p2[o] : 1 - p2[o];
            x += v;
          }
        }
        if (best < x) best = x;
      }
    }
    printf ("Case #%d: %.9lf\n", i, best);
  }
  return 0;
}
