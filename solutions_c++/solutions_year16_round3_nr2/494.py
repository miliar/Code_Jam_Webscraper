#include <iostream>
#include <algorithm>

using namespace std;

typedef long long int ll;

int main() {
  ios_base::sync_with_stdio(false);
  int tt;
  cin >> tt;
  for (int t = 1; t <= tt; ++t) {
    cout << "Case #" << t << ": ";
    ll b, m;
    cin >> b >> m;
    if (m > (1ll << (b - 2))) {
      cout << "IMPOSSIBLE" << endl;
    }
    else {
      cout << "POSSIBLE" << endl;
      if (m == (1ll << (b - 2))) cout << '0' << string(b - 1, '1') << endl;
      else {
        cout << '0';
        for (ll i = b - 3; i >= 0; --i) {
          if (m & (1ll << i)) cout << '1';
          else cout << '0';
        }
        cout << '0' << endl;
      }
      for (int i = 1; i < b; ++i) {
        cout << string(i + 1, '0') << string(b - 1 - i, '1') << endl;
      }
    }
  }
}