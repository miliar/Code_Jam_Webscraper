#include <stdio.h>
#include <assert.h>

int main (void) {
  int T = 0;
  (void) scanf("%d", &T);
  for (int currentcase = 1; currentcase <= T; ++currentcase) {
    int n = 0;
    scanf("%d", &n);
    int add = 0;
    int cur = 0;
    for (int i = 0; i <= n; i++) {
      char c = ' ';
      while ((c = getchar()) == ' ');
      int m = c - '0';
      if (i > cur) {
        add += i - cur;
        cur = i;
      }
      cur += m;
    }
    printf("Case #%d: %d\n", currentcase, add);
  }
  return 0;
}
