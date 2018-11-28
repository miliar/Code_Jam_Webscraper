#include <bits/stdc++.h>

using namespace std;

int main() {
  int t, n, j;
  cin >> t >> n >> j;
  cout << "Case #1:" << endl;
  for (int i = 0; i < j; ++i) {
    cout << "1";
    for (int k = 0; k < (n - 2) / 2; ++k) {
      if (i & (1 << k)) cout << "00";
      else cout << "11";
    }
    cout << "1";
    for (int k = 2; k <= 10; ++k) cout << ' ' << k + 1;
    cout << endl;
  }
}