#include <cstdio>

int main() {
  int ti, tn;
  int n, a[1024];
  char s[1024];
  scanf("%d", &tn);
  for (int ti = 0; ti < tn; ti ++) {
    scanf("%d", &n);
    scanf("%s", s);
    int ans = 0, up = 0;
    for (int i = 0; i <= n; i ++) {
      int req = s[i] - '0';
      if (up < i) {
        ans += i - up;
        up = i;
      }
      up += req;
    }
    printf("Case #%d: %d\n", ti + 1, ans);
  }
}
