#include <algorithm>
#include <stdio.h>

char s[100][104], *ptr[100];

int main ()
{
  int t, i, n, j, k, c[100], r, chr;
  scanf ("%d", &t);
  for (i = 1; i <= t; i++) {
    scanf ("%d", &n);
    for (j = 0; j < n; j++) {
      scanf ("%s", s[j]);
      ptr[j] = s[j];
    }
    r = 0;
    while (*ptr[n-1] != '\0') {
      for (j = 0; j < n && *ptr[j] == *ptr[n-1]; j++) {
        for (c[j] = 0; *ptr[j] == ptr[j][1]; c[j]++) (ptr[j])++;
        (ptr[j])++;
      }
      if (j < n) break;
      std::sort (c, c + n);
      for (j = 0; j < n; j++) r += j < n/2 ? c[n/2] - c[j] : c[j] - c[n/2];
    }
    for (j = 0; j < n && *ptr[j] == '\0'; j++) {}
    if (j == n) printf ("Case #%d: %d\n", i, r);
    else printf ("Case #%d: Fegla Won\n", i);
  }
  return 0;
}
