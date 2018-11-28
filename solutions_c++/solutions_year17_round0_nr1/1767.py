#include <cstdio>
#include <cstring>
char s[1001];
int main() {
  int t;
  scanf("%d", &t);
  for (int ti = 0; ti < t; ++ti) {
    int k;
    scanf("%s%d", s, &k);
    int n = strlen(s), ans = 0;
    for (int i = 0; i < n - k + 1; ++i) {
      if (s[i] == '-') {
        ++ans;
        for (int j = i; j < i + k; ++j) {
          s[j] = s[j] == '+' ? '-' : '+';
        }
      }
    }
    bool flag = true;
    for (int i = n - k + 1; i < n; ++i) {
      if (s[i] == '-') {
        flag = false;
        break;
      }
    }
    printf("Case #%d: ", ti + 1);
    if (flag) {
      printf("%d\n", ans);
    } else {
      printf("IMPOSSIBLE\n");
    }
  }
  return 0;
}
