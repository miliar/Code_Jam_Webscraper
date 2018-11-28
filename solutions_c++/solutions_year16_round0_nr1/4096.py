#include <iostream>
#include <vector>
#include <string>
#include <array>

void put(std::array<bool, 10> &v, uint64_t n) {
  while (n) {
    auto d = n % 10;
    n /= 10;
    v[d] = true;
  }
}

int main() {
  int T;
  std::cin >> T;
  for (auto test = 1; test <= T; ++test) {
    int N;
    std::cin >> N;
    if (N == 0) {
      std::cout << "Case #" << test << ": INSOMNIA" << std::endl;
      continue;
    }
    std::array<bool, 10> v{};

    uint64_t m = 1;
    for (;;) {
      put(v, m * N);
      if (std::count(std::begin(v), std::end(v), true) == v.size()) {
        std::cout << "Case #" << test << ": " << (m * N) << std::endl;
        break;
      }

      ++m;
    }
  }
}
