#include <cstdio>
#include <string.h>

int main() {
  char s[110];
  int t;

  scanf("%d", &t);
  for (int c = 1; c <= t; ++c) {
    scanf("%s", s);

    int sol = 0;
    for (int i = strlen(s) - 1; i >= 0; --i) {
      if (sol & 1) {
        if (s[i] == '+') ++sol;
      } else {
        if (s[i] == '-') ++sol;
      }
    }

    printf("Case #%d: %d\n", c, sol);
  }
  return 0;
}
