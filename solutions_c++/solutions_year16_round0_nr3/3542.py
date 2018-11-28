#include <cmath>
#include <cassert>
#include <iostream>
#include <vector>
#include <string>
#include <array>
#include <iomanip>

int divisor(int64_t n) {
  int d = 2;
  auto to = int(sqrt(n));
  for (; d < to; ++d) {
    if (n % d == 0) {
      return d;
    }
  }
  return -1;
}

std::string to_bin(int64_t n, int w) {
  std::string s;
  for (int j = 0; j < w; ++j, n >>= 1) {
    if (n & 1) {
      s += '1';
    } else {
      s += '0';
    }
  }

  std::reverse(std::begin(s), std::end(s));

  return s;
}

void check(const std::string &s, const std::vector<int> &divs) {
  for (int i = 2; i <= 10; ++i) {
    int64_t n = 0;
    for (auto c : s) {
      n *= i;
      n += c - '0';
    }
    auto q = divs[i - 2];
    if (n % q) {
      std::cerr << s << ", i=" << i << ", n=" << n << ", q=" << q
                << ": not divisible" << std::endl;
      assert(0);
    }
  }
}

int main() {
  int T;
  std::cin >> T;
  for (auto test = 1; test <= T; ++test) {
    int N, J;
    std::cin >> N >> J;
    int numans = 0;

    std::cout << "Case #" << test << ":" << std::endl;

    for (int mid = 0; mid < (1 << (N - 2)); ++mid) {
      std::vector<int> divs;
      for (int i = 2; i <= 10; ++i) {
        auto m = mid;
        int64_t n = 1;
        int64_t r = 1;
        for (int j = 0; j < N - 2; ++j) {
          r *= i;
          n += r * (m & 1);
          m >>= 1;
        }
        r *= i;
        n += r;

        auto div = divisor(n);
        if (div == -1) {
          goto fail;
        }
        divs.push_back(div);
      }

      std::cout << "1" << to_bin(mid, N - 2) << "1";
      for (auto d : divs) {
        std::cout << " " << d;
      }
      std::cout << std::endl;

      check("1" + to_bin(mid, N - 2) + "1", divs);

      ++numans;

      if (numans == J) {
        break;
      }

      continue;

    fail:
      ;
    }
  }
}
