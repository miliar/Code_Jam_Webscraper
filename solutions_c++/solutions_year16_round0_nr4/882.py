#include <bits/stdc++.h>

int main ()
{
  int t, k, i, j, c, s, x;
  scanf ("%d", &t);
  for (x = 1; x <= t; x++) {
    scanf ("%d%d%d", &k, &c, &s);
    printf ("Case #%d:", x);
    if (c * s < k) printf (" IMPOSSIBLE\n");
    else {
      for (j = 0; j < k; ) {
        long long v = 0;
        for (i = 0; i < c; i++) v = v * k + (j < k ? j++ : 0);
        printf (" %lld", v + 1);
      }
      printf ("\n");
    }
  }
  return 0;
}
