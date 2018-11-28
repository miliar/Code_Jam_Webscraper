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
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int x, r, c;
    cin >> x >> r >> c;
    if ((r * c) % x != 0) {
      cout << "Case #" << t << ": RICHARD" << endl;
      continue;
    }
    if (x <= 2) {
      cout << "Case #" << t << ": GABRIEL" << endl;
    } else if (x == 3) {
      cout << "Case #" << t << ": " << (r * c == 3 ? "RICHARD" : "GABRIEL") << endl;
    } else if (x == 4) {
      bool ok = false;
      ok |= (r % 4 == 0) && (c >= 3);
      ok |= (r >= 3) && (c % 4 == 0);
      cout << "Case #" << t << ": " << (ok ? "GABRIEL" : "RICHARD") << endl;
    } else if (x == 5) {
      bool ok = false;
      ok |= (r % 5 == 0) && (c >= 4);
      ok |= (r >= 4) && (c % 5 == 0);
      cout << "Case #" << t << ": " << (ok ? "GABRIEL" : "RICHARD") << endl;
    } else if (x >= 6) {
      cout << "Case #" << t << ": RICHARD" << endl;
    }
  }
  return 0;
}

