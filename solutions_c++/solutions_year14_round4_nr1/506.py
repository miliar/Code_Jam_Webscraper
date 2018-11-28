#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

int s[10100];

int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    int n, x; cin >> n >> x;
    for (int i = 0; i < n; i++) cin >> s[i];
    sort(s, s+n);

    map<int, int> open;
    int res = 0;
    for (int i = n-1; i >= 0; i--) {
      map<int, int>::iterator it = open.lower_bound(s[i]);
      // for (map<int, int>::iterator it2 = open.begin(); it2 != open.end(); ++it2)
      //   cout << it2->first << " " << it2->second << endl;

      if (it != open.end()) {
        if (--it->second == 0) open.erase(it);
      } else {
        open[x - s[i]]++;
        res++;
      }
    }
    cout << "Case #" << c << ": " << res << endl;
  }
  return 0;
}
