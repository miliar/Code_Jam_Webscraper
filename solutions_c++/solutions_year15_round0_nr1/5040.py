#include <bits/stdc++.h>

using namespace std;

int main() {
  freopen("A-large.in", "r ", stdin);
  freopen("A-large.out", "w", stdout);
  int T, tst = 1;
  scanf("%d", &T);
  while (T--) {
    int n;
    char a[1003];
    scanf("%d %s", &n, a);
    int x = 0, ans = 0;
    for (int i = 0; i <= n; ++i) {
      ans += (i - x) * (i > x && a[i] > '0');
      x += (a[i] - '0') + (i - x) * (i > x && a[i] > '0');
    }
    printf("Case #%d: %d\n", tst, ans);
    ++tst;
  }
}