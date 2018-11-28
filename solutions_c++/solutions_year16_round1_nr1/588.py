#include <bits/stdc++.h>

int main ()
{
  int t, i, j;
  scanf ("%d\n", &t);
  for (i = 1; i <= t; i++) {
    char s[1010], r[1010] = "A";
    fgets (s, 1009, stdin);
    r[0] = s[0];
    for (j = 1; s[j] != '\n'; j++) {
      if (r[0] <= s[j]) {
        memmove (r + 1, r, strlen (r) + 1);
        r[0] = s[j];
      }
      else sprintf (r + strlen (r), "%c", s[j]);
    }
    printf ("Case #%d: %s\n", i, r);
  }
  return 0;
}
