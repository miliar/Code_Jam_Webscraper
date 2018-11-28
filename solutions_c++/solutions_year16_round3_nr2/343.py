#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;

int main() {
  int t;
  cin >> t;
  for (int cas = 1; cas <= t; ++cas) {
    ll n, k;
    cin >> n >> k;
    cout << "Case #" << cas << ": ";
    if ((1ll<<(n - 2)) < k) {
      cout << "IMPOSSIBLE" << endl;
      continue;
    }
    cout << "POSSIBLE" << endl;
    if (k == (1ll<<(n - 2))) {
      cout << 0;
      for (int i = 1; i < n; ++i) cout << 1;
      cout << endl;
    }
    else {
      cout << 0;
      vi B(n, 0);
      int tt = 0;
      while (k > 0) {
	if (k%2) B[tt] = 1;
	k /= 2;
	++tt;
      }
      for (int i = n - 3; i >= 0; --i) cout << B[i];
      cout << 0 << endl;
    }
    for (int i = 1; i <= n - 1; ++i) {
      for (int j = 0; j < i + 1; ++j) cout << 0;
      for (int j = i + 1; j < n; ++j) cout << 1;
      cout << endl;
    }
  }
}