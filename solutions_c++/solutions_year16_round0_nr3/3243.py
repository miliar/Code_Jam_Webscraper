#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <map>

std::string s;
int T, N, J;

long is_prime(long n) {
  long sz = (long)sqrt(n);
  for (int i = 2; i < sz; ++i) {
    if (n % i == 0) {
      return i;
    }
  }
  return 1;
}

long to_base(std::string &s, int base) {
  long n = 0;
  for (int i = 0; i < s.size(); ++i) {
    n *= base;
    if (s[i] == '1') {
      n += 1;
    }
  }
  return n;
}

std::vector<long> check() {
  std::vector<long> divisors;
  for (int i = 2; i <= 10; ++i) {
    long d = is_prime(to_base(s, i));
    if (d == 1) {
      break;
    } else {
      divisors.push_back(d);
    }
  }
  return divisors;
}

void generate(int idx) {
  if (J == 0) {
    return;
  }
  if (idx == 0) {
    std::vector<long> divisors = check();
    if (divisors.size() == 9) {
      std::cout << s;
      for (int i = 0; i < 9; ++i) {
        std::cout << ' ' << divisors[i];
      }
      std::cout << std::endl;
      --J;
    }
    return;
  }
  // check with 0 bit
  generate(idx - 1);
  if (J == 0) {
    return;
  }
  // flip bit and check with 1 bit
  s[idx] = '1';
  generate(idx - 1);

  // unflip
  s[idx] = '0';
}

int main() {
  std::cin >> T >> N >> J;
  s = std::string(N, '0');
  s[0] = '1';
  s[N-1] = '1';
  std::cout << "Case #1:" << std::endl;
  generate(14);
}