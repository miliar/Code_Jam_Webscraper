#include <algorithm>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <string>
#include <utility>
#include <vector>

using namespace std;

int count_bits(int n) {
  int x = 0;
  while (n > 0) {
    if (n & 1) {
      ++x;
    }
    n /= 2;
  }
  return x;
}

double solve(int n, int k, double p[]) {
  double max_prob = 0;
  for (int x = 0; x < (1 << n); ++x) {
    if (count_bits(x) == k) {
      double total = 0;
      for (int y = 0; y < (1 << k); ++y) {
        if (count_bits(y) == k / 2) {
          int z = 0;
          double prob = 1;
          for (int i = 0; i < n; ++i) {
            if ((x >> i) & 1) {
              if ((y >> z) & 1) {
                prob *= p[i];
              } else {
                prob *= 1 - p[i];
              }
              ++z;
            }
          }
          total += prob;
        }
      }
      max_prob = max(max_prob, total);
    }
  }
  return max_prob;
}

int main() {
  int t, n, k;
  double p[200];
  cin >> t;
  cout.precision(10);
  for (int case_num = 1; case_num <= t; ++case_num) {
    cin >> n >> k;
    for (int i = 0; i < n; ++i) {
      cin >> p[i];
    }
    cout << "Case #" << case_num << ": " << fixed << solve(n, k, p) << endl;
  }
  return 0;
}
