#include <cstdio>

#include <iostream>
#include <vector>

using std::vector;

typedef long long ll;

bool divides(ll number, ll divisor, int base) {
  ll rem = 0;
  for (ll pos = 32; pos >= 0; --pos) {
    rem *=  base;
    rem += (number & (1LL << pos)) == 0 ? 0 : 1;
    rem %= divisor;
//    std::cout << pos << " " << rem << "\n";
  }
  return rem == 0;
}

int find_divisor(ll number, int base) {
  for (int cur = 2; cur < 1000; ++cur) {
    if (divides(number, cur, base)) {
      return cur;
    }
  }
  return -1;
}

void solve(int digits, int wanted) {
  int found = 0;
  vector<int> divisors(11);
  for (ll current = (1LL << (digits - 1)) + 1; found < wanted; current += 2) {
    std::fill(divisors.begin(), divisors.end(), -1);
    for (int base = 2; base <= 10; ++base) {
      divisors[base] = find_divisor(current, base);
      if (divisors[base] == -1) {
        goto next_number;
      }
    }
    for (ll i = digits - 1; i >= 0; --i) {
      std::cout << ((current & (1 << i)) ? 1 : 0);
    }
    for (int base = 2; base <= 10; ++base) {
      std::cout << " " << divisors[base];
    }
    std::cout << "\n";
    ++found;
next_number:
    ;
  }
}

int main() {
//  std::cout << divides(0b10000000000000000000100100101011LL, 211, 6) << "\n";
  int T;
  std::cin >> T;
  std::cout << "Case #1:\n";
  int digits;
  int wanted;
  std::cin >> digits >> wanted;
  solve(digits, wanted);
}
