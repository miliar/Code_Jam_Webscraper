#include <cstdio>
#include <string.h>
#include <stdlib.h>

int main(void) {
  freopen("A-small-attempt0.in", "r", stdin);
  freopen("A-small.out", "w", stdout);

  int tcase;
  scanf("%d", &tcase);

  for (int i=0; i<tcase; ++i) {
    int a;
    char s[1001] = {0, };

    scanf("%d %s", &a, &s[0]);

    int cnt = 0;
    int standing = s[0] - '0';
    for (int j=1; j<strlen(s); ++j) {
      if (s[j] != '0' && j > standing) {
        cnt += j - standing;
        standing += cnt;
      }
      standing += s[j] - '0';
    }

    printf("Case #%d: %d\n", i+1, cnt);
  }
  return 0;
}
