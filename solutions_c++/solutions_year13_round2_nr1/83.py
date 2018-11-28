#include <stdio.h>
#include <algorithm>

using namespace std;

int a[11111];

int main() {
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  int tt;
  scanf("%d", &tt);
  for (int qq=1;qq<=tt;qq++) {
    printf("Case #%d: ", qq);
    int w, n;
    scanf("%d %d", &w, &n);
    for (int i=0;i<n;i++) scanf("%d", a+i);
    sort(a, a+n);
    int ans = n;
    for (int r=0;r<=n;r++) {
      int add = 0, x = w;
      for (int i=0;i<r;i++) {
        while (x <= a[i]) {
          if (x == 1) {
            add = n;
            break;
          }
          x += x-1;
          add++;
        }
        x += a[i];
      }
      int cur = add+(n-r);
      if (cur < ans) ans = cur;
    }
    printf("%d\n", ans);
  }
  return 0;
}
