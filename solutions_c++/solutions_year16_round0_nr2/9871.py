#include <bits/stdc++.h>

using namespace std;

char s[22];

int main() {
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  int tt;
  scanf("%d", &tt);
  for (int cc = 1; cc <= tt; ++cc) {
    printf("Case #%d: ", cc);
    scanf("%s", s);
    int n = strlen(s);
    int ans = 0;
    for (int i = n - 1, r = 0; i >= 0; --i) {
      if (((s[i] == '+') ^ r) == 0) {
        ++ans;
        r = 1 - r;
      }
    }
    printf("%d\n", ans);
  }
  return 0;
}