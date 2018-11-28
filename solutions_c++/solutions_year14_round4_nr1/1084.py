#include <iostream>
using namespace std;
int a[10000];
bool b[10000];
int main() {
  int tc;
  scanf("%d", &tc);
  for (int cas = 1; cas <= tc; ++cas) {
    int n, m;
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; ++i) scanf("%d", &a[i]);
    memset(b, 0, sizeof(b));
    sort(a, a+n);
    int ans = 0;
    for (int i = n - 1; i >= 0; --i) {
      if (b[i]) continue;
      for (int j = i - 1; j >= 0; --j) {
        if (!b[j] && a[i] + a[j] <= m) {
          b[j] = true;
          break;
        }
      }
      ++ans;
    }
    printf("Case #%d: %d\n", cas, ans);
  }
  return 0;
}
