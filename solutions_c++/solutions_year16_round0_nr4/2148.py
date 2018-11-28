#include <bits/stdc++.h>
using namespace std;

typedef long long LL;


void solve() {
  LL k, c, s;
  cin >> k >> c >> s;

  LL t = (k + c - 1) / c;
  if (t > s) {
    cout << "IMPOSSIBLE" << endl;
    return;
  }

  vector<LL> pow(c + 1);
  pow[0] = 1;

  for (int i = 1; i <= c; ++i) {
    pow[i] = pow[i - 1] * k;
  }

  for (int j = 0; j < k; j += c) {
    LL pos = 0;
    for (int i = j; i < j + c && i < k; ++i) {
      pos += pow[i - j] * i;
    }

    cout << pos + 1 << " ";
  }
  cout << endl;
}

int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cerr << i << " of " << t << endl;
    cout << "Case #" << i << ": ";
    solve();
  }
}
