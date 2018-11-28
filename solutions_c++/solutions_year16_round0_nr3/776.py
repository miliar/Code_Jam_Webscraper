#include <bits/stdc++.h>

int main ()
{
  long long t, n, j, c, i, div, result[11];
  scanf ("%lld%lld%lld", &t, &n, &j);
  printf ("Case #1:\n");
  for (c = (1ll<<(n-1))+1; j; c += 2) {
    for (i = 2; i <= 10; i++) {
      __int128_t x = 0;
      for (long long k = c; k; k >>= 1) x = x * i + (k & 1);
      for (div = 2; div < 128 && x % div != 0; div = (div + 1) | 1) {}
      if (div >= 128) break; // Give up
      result[i] = div;
    }
    if (i >= 10) {
      for (i = c; i; i >>= 1) printf ((i & 1) ? "1" : "0");
      for (i = 2; i <= 10; i++) printf (" %lld", result[i]);
      printf ("\n");
      j--;
    }
  }
  return 0;
}
