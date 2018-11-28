#include <stdio.h>

int main ()
{
  int t, a, b, k, i, j, l, r;
  scanf ("%d", &t);
  for (i = 1; i <= t; i++) {
    scanf ("%d%d%d", &a, &b, &k);
    r = 0;
    for (j = 0; j < a; j++) {
      for (l = 0; l < b; l++) if ((j & l) < k) r++;
    }
    printf ("Case #%d: %d\n", i, r);
  }
  return 0;
}
