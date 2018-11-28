#include <stdio.h>
#include <string.h>

int main() {
  int T, k, n;
  char s[1007];
  int ans;
  bool fail;
  scanf("%d", &T);
  for (int t = 1; t <= T; ++t) {
    scanf("%s%d", s, &k);
    n = strlen(s);
    ans = 0;
    fail = false;
    for (int i = 0; i < n; ++i) {
      if (s[i] == '-') {
        if (i + k > n) {
          fail = true;
          break;
        } else {
          for (int j = 0; j < k; ++j) {
            if (s[i + j] == '-') s[i + j] = '+';
            else s[i + j] = '-';
          }
          ans += 1;
        }
      }
    }
    printf("Case #%d: ", t);
    if (fail) {
      printf("IMPOSSIBLE\n");
    } else {
      printf("%d\n", ans);
    }
  }
  return 0;
}
