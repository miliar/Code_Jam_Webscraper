#include <bitset>
#include <algorithm>
#include <array>
#include <iostream>
#include <ios>
#include <istream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

long factor(long n) {
  if ((n&1) == 0) return 2;
  for (long div = 3; div * div <= n; div += 2) {
    if (n % div == 0) {
      return div;
    }
  }

  return -1;
}

int main(int argc, char *argv[]) {
  cout.precision(8); cout.setf(ios_base::showpoint);
  long t; cin >> t;

  for (long i = 1; i <= t; ++i) {
    int n, j; cin >> n >> j;

    cout << "Case #" << i << ": " << endl;

    int num = 1 + (1 << (n-1));
    std::bitset<32> bs = num;
    std::array<long, 9> factors;
    while (j != 0) {
      bool is_prime = false;
      for (int base = 2; base <= 10; ++base) {
        long d = 0;
        long digit = 1;
        for (int k = 0; k < n; ++k) {
          if (bs.test(k)) d += digit;
          digit *= base;
        }


        auto div = factor(d);
        if (div == -1) {
          is_prime = true;
          break;
        }

        // cout << base << ", " << d << endl;
        factors[base-2] = div;
      }

      if (!is_prime) {
        cout << bitset<16>(num);
        for (auto factor : factors) {
          cout << " " << factor;
        }
        cout << endl;
        --j;
      }

      num += 2;
      bs = bitset<32>(num);
    }
  }

  return 0;
}
