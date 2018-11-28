#include <bits/stdc++.h>

int main ()
{
  int t, n, x;
  scanf ("%d", &t);
  for (x = 1; x <= t ; x++) {
    scanf ("%d", &n);
    int m = 0, i, j;
    if (n > 0) {
      for (i = n; m != 1023; i += n) {
        for (j = i; j; j /= 10) m |= 1 << (j % 10);
      }
    }
    printf (n > 0 ? "Case #%d: %d\n" : "Case #%d: INSOMNIA\n", x, i - n);
  }
  return 0;
}
