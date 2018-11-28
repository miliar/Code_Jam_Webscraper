#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int t;
  cin >> t;
  for (int tt = 1; tt <= t; ++tt) {
    cout << "Case #" << tt << ": ";
    ll n;
    cin >> n;
    if (n == 0) cout << "INSOMNIA" << endl;
    else {
      set<int> s;
      ll k = 1;
      while (s.size() < 10) {
        ll x = n * k;
        while (x > 0ll) {
          s.insert(x % 10ll);
          x /= 10ll;
        }
        ++k;
      }
      cout << n * (k - 1ll) << endl;
    }
  }
}