#include <bits/stdc++.h>

using namespace std;

struct Initializer {
  Initializer() {
    cin.tie(0);
    ios::sync_with_stdio(0);
    cout << fixed << setprecision(15);
  }
} initializer;

using namespace boost::multiprecision;

void solve() {
  int n, j;
  cin >> n >> j;
  for (int i = 0; i < j; ++i) {
    string s = "";
    for (int k = 0, m = i; k < n / 2 - 1; ++k, m /= 2) {
      if (m % 2) s += "11";
      else s += "00";
    }
    cout << "1" << s << "1";
    for (int k = 2; k <= 10; ++k) cout << " " << k + 1;
    cout << endl;
  }
}

int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cout << "Case #" << i << ":" << endl;
    solve();
  }
}
