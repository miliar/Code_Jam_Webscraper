#include <bits/stdc++.h>

const int n = 16;
const int j = 50;

bool isPrime (uint64_t v, int& d) {
  for (uint64_t p = 2 ; p * p <= v ; p += 1) {
    if (v % p == 0) {
      d = p;
      return false;
    }
  }
  return true;
}

uint64_t value (uint64_t n, int base) {
  uint64_t v = 0;
  uint64_t m = 1;
  while (n != 0) {
    uint64_t d = n % 2;
    v += m * d;
    m *= base;
    n /= 2;
  }
  return v;
}

void solution () {
  uint64_t limit = 1 << (n - 2);
  uint64_t i = 0;
  int t = 0;
  int d = 0;
  std::vector<uint64_t> divisors(9);
  while (i < limit) {
    int v = (1 << (n - 1)) | (i << 1) | 1;
    i += 1;
    if (isPrime(v, d)) continue;
    divisors[0] = d;

    bool ok = true;
    for (int b = 3 ; b <= 10 && ok ; b += 1) {
      uint64_t x = value(v, b);
      if (isPrime(x, d)) ok = false;
      divisors[b - 2] = d;
    }

    if (ok) {
      std::cout << value(v, 10) << " ";
      for (uint64_t x: divisors) {
        std::cout << " " << x;
      }
      std::cout << std::endl;
      t += 1;
      if (t == j) return ;
    }
  }
}

int main () {
  // std::ios_base::sync_with_stdio(false);

  std::freopen("C.out", "w", stdout);

  std::cout << "Case #1: " << std::endl;
  solution();

  return 0;
}
