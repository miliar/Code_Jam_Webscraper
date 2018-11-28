#include <bits/stdc++.h>

int main ()
{
  int t, x;
  scanf ("%d", &t);
  for (x = 1; x <= t; x++) {
    char s[120];
    scanf ("%s", s);
    int cnt = s[strlen (s) - 1] == '-' ? 1 : 0, m;
    for (m = 0; s[m + 1]; m++) if (s[m] != s[m + 1]) cnt++;
    printf ("Case #%d: %d\n", x, cnt);
  }
  return 0;
}

/* Verify everything up to length 21:
int tab[1<<22], f[1<<22];

int main ()
{
  int t, x;
  char s[120];
  for (x = 1; x < 22; x++) {
    memset (f, 0, sizeof (f));
    tab[0] = 0;
    f[0] = 1;
    int i = 0, j = 1, k = 1, r = 1;
    for (i = 0; i < k; i++) {
      if (j == i) {
        j = k;
        r++;
      }
      int rev = 0, v = tab[i], l, m;
      for (l = 1; l <= x; l++) {
        rev = (rev << 1) | (1 ^ (v & 1));
        v >>= 1;
        if (!f[(v << l) | rev]) {
          f[(v << l) | rev] = 1;
          tab[k++] = (v << l) | rev;
          
          for (m = 0; m < x; m++) s[m] = ((((v<<l)|rev)>>m)&1) ? '-' : '+';
          s[x] = '\0';
          int cnt = s[strlen (s) - 1] == '-' ? 1 : 0;
          for (m = 0; s[m + 1]; m++) if (s[m] != s[m + 1]) cnt++;
          if (cnt != r) printf ("%s %d %d\n", s, r, cnt);
        }
      }
    }
  }
  return 0;
}
*/
