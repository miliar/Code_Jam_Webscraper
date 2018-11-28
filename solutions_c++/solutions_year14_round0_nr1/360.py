#include <stdio.h>

int main ()
{
  int T, i, ans, x, j, mask[2], k;
  scanf ("%d", &T);
  for (i = 1; i <= T; i++) {
    for (k = 0; k < 2; k++) {
      mask[k] = 0;
      scanf ("%d", &ans);
      for (j = 0; j < 16; j++) {
        scanf ("%d", &x);
        if (j / 4 + 1 == ans) mask[k] |= 1<<x;
      }
    }
    mask[0] &= mask[1];
    for (k = 1; k <= 16 && !(mask[0] & (1<<k)); k++) {}
    if (!mask[0]) printf ("Case #%d: Volunteer cheated!\n", i);
    else if ((mask[0] - 1) & mask[0]) printf ("Case #%d: Bad magician!\n", i);
    else printf ("Case #%d: %d\n", i, k);
  }
  return 0;
}
