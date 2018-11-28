#include <bits/stdc++.h>
using namespace std;

int main() {
  int tests;
  cin >> tests;
  for (int t = 1; t <= tests; ++t) {
    int n, cnt = 0, sol = 0;
    string w;
    cin >> n >> w;
    for (int i = 0; i <= n; ++i) {
      sol += max(0, i-sol-cnt);
      cnt += w[i] - '0';
    }
    cout << "Case #" << t << ": " << sol << endl;
  }
  return 0;
}