#include <algorithm>
#include <cstdio>

const int N = 1000 + 10;

int p[N], n;

int main() {
  int test;
  scanf("%d", &test);
  for (int t = 1; t <= test; ++ t) {
    scanf("%d", &n);
    int maxp = 0;
    for (int i = 0; i < n; ++ i) {
      scanf("%d", p + i);
      maxp = std::max(maxp, p[i]);
    }
    int result = 1 << 30;
    for (int eaten = 1; eaten <= maxp; ++ eaten) {
      int temp = eaten;
      for (int i = 0; i < n; ++ i) {
        temp += (p[i] - 1) / eaten;
      }
      result = std::min(result, temp);
    }
    printf("Case #%d: %d\n", t, result);
  }
  return 0;
}
