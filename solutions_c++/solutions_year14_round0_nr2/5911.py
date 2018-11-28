#include <iostream>
#include <iomanip>
#include <algorithm>

const double p = 2.0;

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cout << std::fixed << std::setprecision(7);
  int t;
  std::cin >> t;
  for (int i = 0; i < t; i++) {
    double c, f, x;
    std::cin >> c >> f >> x;
    double b = x / p;
    double elapsed = 0.0;
    double rate = p;
    while (elapsed < b) {
      double b2 = elapsed + x / rate;
      b = std::min(b, b2);
      elapsed += c / rate;
      rate += f;
    }
    std::cout << "Case #" << i + 1 << ": " << b << std::endl;
  }
}
