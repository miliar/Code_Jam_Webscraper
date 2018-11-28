

#include <stdio.h>


/*
1 = 0
i = 1
j = 2
k = 3

+ = 0
- = 1
*/
const static unsigned char values[4][4] = {{0, 1, 2, 3}, {1, 0, 3, 2}, {2, 3, 0, 1}, {3, 2, 1, 0}};
const static unsigned char signals[4][4] = {{0, 0, 0, 0}, {0, 1, 0, 1}, {0, 1, 1, 0}, {0, 0, 1, 1}};

int main() {
  unsigned int tests, casenum=0;
  scanf("%d", &tests);

  while (tests--) {
    unsigned int X, L;
    unsigned char sig = 0;
    unsigned char result = 0;
    unsigned char expected_result = 1;

    scanf("%u %u", &L, &X);

    fgetc(stdin);

    unsigned char string[10002];
    fgets((char *)&string, 10001, stdin);

    while (X--) {
      unsigned char *c_ptr = string;
      for(unsigned int i = 0; i < L; i++) {
        unsigned char c = *(c_ptr++);
        //c = (c&0x07) - !(c & 0x08); //Accept '1'
        c -= 'i' - 1;
        if (c < 1 || c > 3) printf("ERRO");
        sig = sig ^ signals[result][c];
        result = values[result][c];

        if(!sig && result == expected_result) {
          expected_result++;
          result = 0;
          sig = 0;
        }
      }
    }

    if (sig == 0 && result == 0 && expected_result == 4) printf ("Case #%u: YES\n", ++casenum);
    else printf ("Case #%u: NO\n", ++casenum);
  }
}
