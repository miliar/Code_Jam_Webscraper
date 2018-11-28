#include <stdio.h>

int main ()
{
  int i, T, j;
  long double C, F, X, r, tm, best;
  scanf ("%d", &T);
  for (i = 1; i <= T; i++) {
    scanf ("%Lf%Lf%Lf", &C, &F, &X);
    r = 2;
    best = X;
    tm = 0;
    j = 0;
    while (tm + X / r > tm + C / r + X / (r + F)) {
      tm += C / r;
      r += F;
      j++;
    }
    printf ("Case #%d: %.7Lf\n", i, tm + X / r);
    //fprintf (stderr, "%d\n", j);
  }
  return 0;
}
