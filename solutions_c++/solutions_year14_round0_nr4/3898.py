#include <cstdio>
#include <deque>
#include <algorithm>

int main() {
  int t, n;
  double input;
  std::deque<double> n1, k1;
  scanf("%d", &t);
  for (int x = 1; x <= t; x++) {
    n1.clear();
    k1.clear();
    scanf("%d", &n);
    for (int i = 1; i <= 2 * n; i++) {
      scanf("%lf", &input);
      if (i <= n) {
        n1.push_back(input);
      } else {
        k1.push_back(input);
      }
    }
    std::sort(n1.begin(), n1.end());
    std::sort(k1.begin(), k1.end());
    std::deque<double> n2 = n1, k2 = k1;
    int it = n - 1;
    while (!(n1.empty() || k1.empty()) && it >= 0) {
      if (n1[it] < k1[it]) {
        n1.pop_front();
        k1.pop_back();
      }
      it--;
    }
    it = n - 1;
    while (!(n2.empty() || k2.empty()) && it >= 0) {
      if (k2[it] < n2[it]) {
        k2.pop_front();
        n2.pop_back();
      }
      it--;
    }
    printf("Case #%d: %d %d\n", x, n1.size(), n - k2.size());
  }
  return 0;
}
