

#include <stdio.h>

int main() {
  unsigned int tests, casenum=0;
  scanf("%d", &tests);

  while (tests--) {
    unsigned int X, R, C;
    scanf("%u %u %u", &X, &R, &C);

    if ((R*C)%X > 0) goto richard;

    if (X>R && X>C) goto richard;

    {
      unsigned int L = (X>>1) + (X&1);
      if (L>R || L>C) goto richard;
    }

    if (X>=4){
      if (R < C) {
        if (X >= 2*R-1) goto richard;
      } else {
        if (X >= 2*C-1) goto richard;
      }
    }

    printf ("Case #%u: GABRIEL\n", ++casenum);
    continue;

    richard:
    printf ("Case #%u: RICHARD\n", ++casenum);
  }


}
