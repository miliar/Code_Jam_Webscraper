#include <bits/stdc++.h>

int main ()
{
  int t, i, n, j, k, cnt[2501], h;
  scanf ("%d", &t);
  for (i = 1; i <= t; i++) {
    scanf ("%d", &n);
    memset (cnt, 0, sizeof (cnt));
    for (j = 0; j < n + n - 1; j++) {
      for (k = 0; k < n; k++) {
        scanf ("%d", &h);
        cnt[h]++;
      }
    }
    printf ("Case #%d:", i);
    for (j = 0; j <= 2500; j++) {
      if (cnt[j] % 2) printf (" %d", j);
    }
    printf ("\n");
  }
  return 0;
}
