#include <algorithm>
#include <iostream>
#include <random>
#include <vector>

using namespace std;

long long first_factor(__int128 x) {
  for (long long p = 2; p * p <= min(x, __int128(100000000)); ++p) {
    if (x % p == 0) {
      return p;
    }
  }
  return -1;
}

int main() {
  int t, n, j;
  cin >> t;
  for (int case_num = 1; case_num <= t; ++case_num) {
    cout << "Case #" << case_num << ":" << endl;
    cin >> n >> j;
    int count = 0;
    for (long long x = (1LL << (n - 1)) + 1; count < j and x < (1LL << n); x += 2) {
      vector<long long> factors;
      for (int b = 2; b <= 10; ++b) {
        long long r = x;
        __int128 y = 0;
        __int128 z = 1;
        while (r > 0) {
          y += (r & 1) * z;
          z *= b;
          r /= 2;
        }
        long long f = first_factor(y);
        if (f < 0) {
          goto next;
        }
        factors.push_back(f);
      }
      for (int i = 0; i < n; ++i) {
        cout << ((x >> (n - 1 - i)) & 1);
      }
      for (int f : factors) {
        cout << ' ' << f;
      }
      cout << endl;
      ++count;
next:;
    }
    if (count < j) {
      cerr << "NOT COMPLETED" << endl;
    }
  }
  return 0;
}
