#include <bits/stdc++.h>

using namespace std;

char foo[1234567];

int main() {
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  int tt;
  scanf("%d", &tt);
  for (int qq = 1; qq <= tt; qq++) {
    printf("Case #%d: ", qq);
    scanf("%s", foo);
    int n = strlen(foo);
    while (n > 0 && foo[n - 1] == '+') {
      n--;
    }
    int ans = 0;
    for (int i = 0; i < n; i++) {
      if (i == 0 || foo[i] != foo[i - 1]) {
        ans++;
      }
    }
    printf("%d\n", ans);

  }
  return 0;
}
