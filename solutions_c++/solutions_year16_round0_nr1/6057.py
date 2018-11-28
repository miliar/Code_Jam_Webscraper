#include <assert.h>
#include <memory.h>
#include <algorithm>
#include <cstdio>
#include <iostream>
#include <limits>
#include <numeric>
#include <set>
#include <string>
#include <vector>

using namespace std;

/*** TEMPLATE CODE ENDS HERE */

set<int> extract(long long x) {
  set<int> s;
  for (; x > 0; x /= 10) s.insert(x % 10);
  return s;
}

int main() {
#ifdef LOCAL_HOST
  freopen("A-small-attempt0.in", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif

  cout.sync_with_stdio(0);
  cin.tie(0);

  int T;
  cin >> T;

  set<int> al;
  for (int i = 0; i < 10; ++i) al.insert(i);

  for (int tt = 1; tt <= T; ++tt) {
    long long n;
    cin >> n;
    if (n == 0) {
      cout << "Case #" << tt << ": "
           << "INSOMNIA\n";
      continue;
    }
    set<int> s;
    for (int i = 1;; i++) {
      set<int> ns = s;
      set<int> s1 = extract(n * i);
      ns.insert(s1.begin(), s1.end());
      s = ns;
      if (ns == al) {
        cout << "Case #" << tt << ": " << n * i << endl;
        break;
      }
    }
  }

  return 0;
}
