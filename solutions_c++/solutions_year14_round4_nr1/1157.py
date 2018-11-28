#include <iostream>
#include <set>
using namespace std;

int main() {
/*  multiset<int> s;
  s.insert(4);
  s.insert(5);
  s.insert(4);

  multiset<int>::iterator it = s.end();
  --it;
  s.erase(it);

  it = s.end();
  --it;
  s.erase(it);

  for ( = s.begin(); it != s.end(); ++it) {
    cout << *it << endl;
  }
*/

  int t;
  cin >> t;
  for (int tt = 1; tt <= t; ++tt) {
    int n, x, cur;
    multiset<int> s;
    multiset<int>::iterator it;

    cin >> n >> x;
    for (int i = 0; i < n; ++i) {
      cin >> cur;
      s.insert(cur);
    }

    int res = 0;
    while (!s.empty()) {
      ++res;
      it = s.end(); --it;
      int remain = x - *it;
      //cout << *it << " + ";
      s.erase(it);

      if (!s.empty()) {
        it = s.upper_bound(remain);
        if (it != s.begin()) {
          --it;
          //cout << *it << endl;
          s.erase(it);
        }
      }
    }

    cout << "Case #" << tt << ": " << res << endl;
  }
}
