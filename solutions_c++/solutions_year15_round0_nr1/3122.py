#include <bits/stdc++.h>
using namespace std;

char aud[11111];

int main() {
  int test; scanf("%d", &test);
  for (int cas = 1; cas <= test; ++cas) {
    int n; scanf("%d%s", &n, aud);
    int fore = 0, ans = 0;
    for (int i = 0; i <= n; ++i) {
      if (aud[i] != '0' && fore < i) {
        ans += i - fore;
        fore = i;
      }
      fore += aud[i] - '0';
    }
    printf("Case #%d: %d\n", cas, ans);
  }
  return 0;
}
