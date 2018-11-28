#include <cstdio>

char S[1002];

int main() {
  int T=100;
  scanf("%d", &T);
  for (int t = 1; t <= T; ++t) {
    int s_max;
    scanf("%d", &s_max);
    scanf("%s", S);

    int cur = 0;
    int ret = 0;
    for (int i = 0; i <= s_max; ++i) {
      if (i <= cur) {
        cur += (S[i]-'0');
      } else if (S[i] != '0') {
        ret += (i - cur);
        cur += ret;
        cur += (S[i]-'0');
      }
    }
    printf("Case #%d: %d\n", t, ret);
  }
  return 0;
}
