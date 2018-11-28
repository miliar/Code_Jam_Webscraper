#include <iostream>

using namespace std;

void solve() {
  int d;
  cin >> d;
  int p[d];
  for (int i = 0; i < d; ++i) cin >> p[i];
  int res = 1e9;
  for (int i = 1; i <= 1000; ++i) {
    int r = 0;
    for (int j = 0; j < d; ++j) r += (p[j] - 1) / i;
    res = min(res, r + i);
  }
  cout << res << endl;
}

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    cout << "Case #" << i + 1 << ": ";
    solve();
  }
}
