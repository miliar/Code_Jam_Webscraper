#include <bits/stdc++.h>

using namespace std;

long long change_base(int binary, int base) {
  long long ret = 0;
  for (int i = 15; i >= 0; --i) {
    ret *= base;
    if ((binary >> i) & 1) ++ret;
  }
  return ret;
}

int main() {
  const int num_bits = 16;
  const int lim_print = 50;

  puts("Case #1:");
  int printed = 0;
  for (int i = 0; i < (1 << num_bits); ++i) {
    if ((i & 1) == 0) continue;
    if (((i >> 15) & 1) == 0) continue;

    vector<int> divisors;
    for (int j = 2; j <= 10; ++j) {
      long long x = change_base(i, j);
      for (long long k = 2; k * k <= x; ++k) {
        if (x % k == 0) {
          divisors.push_back(k);
          break;
        }
      }
      if (divisors.size() != j - 1) break;
    }

    if (divisors.size() == 9) {
      printf("%0*lld", num_bits, change_base(i, 10));
      for (int i = 0; i < 9; ++i) printf(" %d", divisors[i]);
      puts("");
      if (++printed == lim_print) break;
    }
  }
  return 0;
}