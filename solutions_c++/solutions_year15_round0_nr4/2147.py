#include <stdio.h>

using namespace std;

int main() {
  int t, x, r, c, i;

  scanf("%d", &t);
  i = 1;
  while (t--) {
    scanf("%d %d %d", &x, &r, &c);
    if (x >= 7) {
      printf("Case #%d: RICHARD\n", i);
    } else if (x == 1) {
      printf("Case #%d: GABRIEL\n", i);
    } else if (x == 2) {
      if ((r * c) % 2 == 1)
	printf("Case #%d: RICHARD\n", i);
      else
	printf("Case #%d: GABRIEL\n", i);
    } else if (x == 3) {
      if ((r * c) % 3 == 0 && c >= 2 && r >= 2)
	printf("Case #%d: GABRIEL\n", i);
      else
	printf("Case #%d: RICHARD\n", i);
    } else if (x == 4) {
      if ((r * c) % 4 == 0 && r > 2 && c > 2)
	printf("Case #%d: GABRIEL\n", i);
      else
	printf("Case #%d: RICHARD\n", i);
    }
    i++;
  }
  return 0;
}
