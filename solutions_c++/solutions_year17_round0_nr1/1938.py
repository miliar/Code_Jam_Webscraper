#include <cstdio>
#include <cstring>

char s[1010];

int main() {
  freopen("/Users/yogy/ClionProjects/untitled/A-large.in", "r", stdin);
  freopen("/Users/yogy/ClionProjects/untitled/al.out", "w", stdout);
  int T, tc = 0;
  scanf("%d", &T);
  while (T--) {
    int k;
    scanf("%s%d", s, &k);
    int ans = 0;
    int n = strlen(s);
    for (int i = 0; i <= n - k; ++i) {
      if (s[i] == '-') {
        ++ans;
        for (int j = 1; j < k; ++j) {
          if(s[i + j] == '+') s[i + j] = '-';
          else s[i + j] = '+';
        }
      }
    }
    bool ok = true;
    for (int i = n - k + 1; i < n; ++i) {
      if (s[i] == '-') {
        ok = false;
        break;
      }
    }
    if (ok)
      printf("Case #%d: %d\n", ++tc, ans);
    else
      printf("Case #%d: IMPOSSIBLE\n", ++tc);
  }
  return 0;
}