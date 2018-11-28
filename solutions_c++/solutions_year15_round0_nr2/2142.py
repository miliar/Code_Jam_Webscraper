#include <algorithm>
#include <iostream>
#include <vector>

int DivideToAtMost(const std::vector<int>& p, int x) {
  int n = 0;
  for (int i = 0; i < p.size(); i++) {
    n += (p[i] + x - 1) / x - 1;
  }
  return n;
}

int main() {
  int t;
  std::cin >> t;
  for (int i = 0; i < t; i++) {
    int d;
    std::cin >> d;
    std::vector<int> p(d);
    for (int j = 0; j < d; j++) {
      std::cin >> p[j];
    }
    int m = *std::max_element(p.begin(), p.end());
    int y = m;
    for (int x = m - 1; x > 0; x--) {
      int n = DivideToAtMost(p, x);
      y = std::min(y, n + x);
    }
    std::cout << "Case #" << i + 1 << ": " << y << std::endl;
  }
}
