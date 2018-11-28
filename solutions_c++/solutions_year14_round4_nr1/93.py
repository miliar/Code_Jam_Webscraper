#include <cmath>
#include <cstdio>
#include <cstring>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
using std::string;
using std::vector;

int a[11111];

int Work() {
  int n, x;
  scanf("%d%d", &n, &x);
  for (int i = 0; i < n; ++i)
    scanf("%d", a + i);
  std::sort(a, a + n);
  int ans = 0;
  for (int l = 0, r = n - 1; l <= r; ) {
    if (a[r] + a[l] <= x) {
      ++ans;
      --r; ++l;
    } else {
      ++ans;
      --r;
    }
  }
  return ans;
}

int main() {
  int cases;
  scanf("%d", &cases);
  for (int i = 1; i <= cases; ++i) {
    printf("Case #%d: %d\n", i, Work());
  }
  return 0;
}
