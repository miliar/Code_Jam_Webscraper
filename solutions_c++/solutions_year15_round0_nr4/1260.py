#include <math.h>
#include <stdio.h>
#include <algorithm>

int pancakes[1002];

int main() {
  int t, x, r, c;
  scanf("%d", &t);
  for (int C = 1; C <= t; ++C) {
    scanf("%d%d%d", &x, &r, &c);
    printf("Case #%d: ", C);
    if (x == 1) printf("GABRIEL\n");
    else if(x == 2) {
      if (!(r & 1) || !(c & 1))
        printf("GABRIEL\n");
      else printf("RICHARD\n");
    } else if (x == 3) {
      if (r == 2 && c == 3)
        printf("GABRIEL\n");
      else if (r == 3 && c == 2)
        printf("GABRIEL\n");
      else if (r == 3 && c == 3)
        printf("GABRIEL\n");
      else if (r == 3 && c == 4)
        printf("GABRIEL\n");
      else if (r == 4 && c == 3)
        printf("GABRIEL\n");
      else printf("RICHARD\n");
    } else {
      if (r == 4 && c == 4)
        printf("GABRIEL\n");
      else if (r == 3 && c == 4)
        printf("GABRIEL\n");
      else if (r == 4 && c == 3)
        printf("GABRIEL\n");
      else printf("RICHARD\n");
    }
  }
  return 0;
}