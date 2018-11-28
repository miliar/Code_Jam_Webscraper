#include <cstdio>
#include <climits>
#include <queue>
#include <algorithm>

const int N = 1000 + 10;

int n, a[N];

int main() {
  int tcase;
  scanf("%d", &tcase);
  for (int no = 1; no <= tcase; ++no) {
    scanf("%d", &n);
    for (int i = 1; i <= n; ++i) scanf("%d", a + i);
    int ans = *std::max_element(a + 1, a + n + 1);
    for (int i = 1; i <= ans; ++i) {
      int sum = 0;
      for (int j = 1; j <= n; ++j) sum += (a[j] - 1) / i;
      ans = std::min(ans, sum + i);
    }
    printf("Case #%d: %d\n", no, ans);
  }
  return 0;
}
