

#include <stdio.h>

int main() {
  unsigned int tests, casenum=0;
  scanf("%d", &tests);

  while (tests--) {
    unsigned int S, Sa=0, friends=0, stood_up=0;
    scanf("%d ", &S);

    do {
      unsigned char audience;
      audience = fgetc(stdin);
      audience -= '0';

      if (Sa > stood_up) {
        friends += Sa - stood_up;
        stood_up = Sa;
      } Sa++;

      stood_up += audience;

      //fgetc(stdin);
    } while(S--);

    printf ("Case #%u: %u\n", ++casenum, friends);
  }


}
