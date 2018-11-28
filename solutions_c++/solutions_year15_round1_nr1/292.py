// {{{ template
#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<string> vs;
typedef vector<long long> vll;
typedef vector<pii> vpii;
// }}}

int main() {
  cin.sync_with_stdio(0); cin.tie(0);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int n;
    cin >> n;
    vi a(n);
    for (int i = 0; i < n; i++) {
      cin >> a[i];
    }
    int x = 0, y = 0;
    for (int i = 1; i < n; i++) {
      if (a[i - 1] >= a[i]) {
        x += a[i - 1] - a[i];
        y = max(y, a[i - 1] - a[i]);
      }
    }
    int yy = 0;
    for (int i = 1; i < n; i++) {
      yy += min(y, a[i - 1]);
    }
    cout << "Case #" << t << ": " << x << ' ' << yy << endl;
  }
  return 0;
}

