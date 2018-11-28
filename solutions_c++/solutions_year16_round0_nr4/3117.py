#include <iostream>
#include <cmath>

int main() {
  int sz;
  std::cin >> sz;
  for (int i = 1; i <= sz; ++i) {
    long c, k, s;
    std::cin >> k >> c >> s;
    std::cout << "Case #" << i << ": ";
    long t = (long)pow(k, c - 1);
    for (int i = 0; i < s; ++i) {
      std::cout << (i * t) + 1 << ' ';
    }
    std::cout << std::endl;
  }
  return 0;
}