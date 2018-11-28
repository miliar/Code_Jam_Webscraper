#include <stdio.h>
#include <string.h>

int main ()
{
  int T, i, j, k, l, m, n, R, C, M; // c, m, o, x, b;
  char out[50*51+1];
  scanf ("%d", &T);
  for (i = 1; i <= T; i++) {
    scanf ("%d%d%d", &R, &C, &M);
/*    for (c = 1; c < (1<<(R*C)); c <<= 1) {
      b = c;
      if (b >= (1<<C)) b |= b >> C;
      if (b < (1<<((R-1)*C))) b |= b << C;
      if (ffs (b) % C) b |= b << 1;
      if (C > 1 && ffs (b) % C != 1) b |= b >> 1;
      
      for (x = 0; x < R*C; x++, b >>= 1) {
        printf ("%d%c", b & 1, x % C == C - 1 ? '\n' : ' ');
      }
      printf ("---\n");
    }*/
    printf ("Case #%d:\n", i);
    for (j = R; j >= 2; j--) {
      for (k = C; k >= 2; k--) {
        for (l = k; l > 1; l--) {
          for (m = k; m >= l; m--) {
            if (l + m + k * (j - 2) == R * C - M &&
                (k == m || j > 3) && (l == m || j > 2)) break;
          }
          if (m >= l) break;
        }
        if (l > 1) break;
      }
      if (k >= 2) break;
    }
    if (C == 1 && M < R * C) {
      j = R - M;
      k = 1;
      l = 1;
      m = 1;
    }
    if (R == 1) {
      putchar ('c');
      for (n = 1; n < C; n++) putchar (n < C - M ? '.' : '*');
      putchar ('\n');
    }
    else if (j == 1 && M != R * C - 1) printf ("Impossible\n");
    else {
      //fprintf (stderr, "j=%d k=%d l=%d\n", j, k, l);
      memset (out, '*', sizeof (out));
      for (n = 0; n < j; n++) memset (out + n * (C+1), '.', k);
      if (j > 1) memset (out + (j-2) * (C+1) + m, '*', C - m);
      if (j > 1) memset (out + (j-1) * (C+1) + l, '*', C - l);
      out[0] = 'c';
      for (n = 0; n < R; n++) out[n * (C + 1) + C] = '\n';
      printf ("%.*s", R * (C + 1), out);
      for (n = 0; n < R * (C + 1); n++) if (out[n] == '*') M--;
      if (M != 0)
        fprintf (stderr, "Error!\n");
    }
/*
    for (m = 0; m < (1<<(R*C)); m++) {
      if (__builtin_popcount (m) != M) continue;
      for (c = 1; c < (1<<(R*C)); c <<= 1) {
        o = m;
        for (x = c; x; x &= ~o) {
          o |= (~(x-1)) & x;
          b = (~(x-1)) & x;
          if (b >= (1<<C)) b |= b >> C;
          if (b < (1<<((R-1)*C))) b |= b << C;
          if (ffs (b) % C) b |= b << 1;
          if (C > 1 && ffs (b) % C != 1) b |= b >> 1;
          if (!(b & m)) x |= b;
        }
        if (o == (1<<(R*C)) - 1) break;
      }
      if (c < (1<<(R*C))) break;
    }
    if (m < (1<<(R*C))) {
      for (x = 0; x < R*C; x++, m >>= 1, c >>= 1) {
        putchar (c & 1 ? 'c' : m & 1 ? '*' : '.');
        if (x % C == C - 1) putchar ('\n');
      }
    }
    else printf ("Impossible\n");
*/
  }
  return 0;
}
