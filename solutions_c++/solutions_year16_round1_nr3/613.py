#include <bits/stdc++.h>

int main ()
{
  int t, n, i, j, f[1001], r, k, l, best[1001];
  scanf ("%d", &t);
  for (i = 1; i <= t; i++) {
    scanf ("%d", &n);
    for (j = 1; j <= n; j++) scanf ("%d", &f[j]);
    r = 0;
    memset (best, 0, sizeof (best));
    for (j = 1; j <= n; j++) {
      int cnt = 1, x[n+1];
      memset (x, 0, sizeof (x));
      int l = 0;
      x[j] = ++l;
      for (k = j; !x[f[k]]; k = f[k]) x[f[k]] = ++l;
      if (f[k] == j && l > r) r = l;
      //if (f[f[k]] == k && best[k] < l) fprintf (stderr,
      //  "A string of length %d begins at %d and ends at %d\n", l, j, k);
      if (f[f[k]] == k && best[k] < l) best[k] = l;
    }
    int sum = 0;
    for (j = 1; j <= n; j++) {
      if (f[j] > j && f[f[j]] == j) sum += best[j] + best[f[j]] - 2;
    }
    printf ("Case #%d: %d\n", i, r > sum ? r : sum);
  }
  return 0;
}
