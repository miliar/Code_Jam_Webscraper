#include <cmath>
#include <iostream>
#include <string>

void ToBitString(size_t n, std::string &result) {
  if (!n) {
    result = "";
    return;
  }
  ToBitString(n / 2, result);
  result += '0' + (n & 1);
}

size_t BitStringToBase(const std::string &BIT_STRING, const size_t BASE) {
  size_t result = 0;
  for (char c : BIT_STRING) {
    result = result * BASE + (c - '0');
  }
  return result;
}

size_t NonTrivialDivsor(size_t n) {
  size_t sqrt_n = sqrt(n);
  for (size_t divisor = 2; divisor <= sqrt_n; ++divisor) {
    if (!(n % divisor)) {
      return divisor;
    }
  }
  return 0;
}

int main() {

  size_t T;
  std::cin >> T;
  for (size_t t = 1; t <= T; ++t) {
    size_t N, J;
    std::cin >> N >> J;
    std::cout << "Case #" << t << ":\n";
    size_t l = (size_t)1 << (N - 1);
    size_t r = 1;
    size_t max_mid = (size_t)1 << (N - 2);
    for (size_t mid = 0; J && (mid < max_mid); ++mid) {
      std::string bit_string;
      ToBitString(l + r + mid * 2, bit_string);
      size_t non_trivial_divsor[10];
      bool solved = true;
      for (size_t base = 2; solved && base <= 10; ++base) {
        non_trivial_divsor[base] = NonTrivialDivsor(BitStringToBase(bit_string, base));
        solved = non_trivial_divsor[base];
      }
      if (solved) {
        std::cout << bit_string;
        for (size_t base = 2; base <= 10; ++base) {
          std::cout << " " << non_trivial_divsor[base];
        }
        std::cout << "\n";
        --J;
      }
    }
  }
  return 0;
}
