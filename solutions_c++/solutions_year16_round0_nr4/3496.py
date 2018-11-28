#include <iostream>

using namespace std;

unsigned long long pow(unsigned long long base, int n) {
  unsigned long long ans = 1;
  while (n) {
    if (n & 1) {
      ans *= base;
    }

    base *= base;
    n /= 2;
  }

  return ans;
}

int main() {
  int t;
  cin >> t;
  for (int ci = 1; ci <= t; ++ci) {
    int k, c, s;
    cin >> k >> c >> s;
    cout << "Case #" << ci << ":";
    int res = k;
    if (c == 1 || k == 1) {
      if (k > s) cout << " IMPOSSIBLE" << endl;
      else {
        for (int i = 1; i <= k; ++i) {
          cout << " " << i;
        }
        cout << endl;
      }
    } else {
      if (k - 1 > s) cout << "IMPOSSIBLE" << endl;
      else {
        unsigned long long block_size = pow(k, c - 1);
        unsigned long long ans = 2;
        for (int i = 0; i < k - 1; ++i) {
          cout << " " << ans + block_size * i;
          ++ans;
        }
        cout << endl;
      }
    }
  }

  return 0;
}
