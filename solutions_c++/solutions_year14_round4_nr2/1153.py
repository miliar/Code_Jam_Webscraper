#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

int main() {
  int t;
  cin >> t;
  for (int tt = 1; tt <= t; ++tt) {
    int n;
    cin >> n;
    int a[11], b[11];
    for (int i = 0; i < n; ++i) {
      cin >> a[i];
      b[i] = a[i];
    }

    int best = 1234567890;

    sort(a, a+n);

    do {
      int pos = 0;
      while (pos < n-1 && a[pos+1] > a[pos]) ++pos;
      while (pos < n-1 && a[pos+1] < a[pos]) ++pos;
      if (pos != n-1) continue;

/*      cout << "---\n";
      for (int i = 0; i < n; ++i) cout << b[i] << " ";
      cout << " --> ";
      for (int i = 0; i < n; ++i) cout << a[i] << " ";
      cout << endl;
*/
      int c[11];
      for (int i = 0; i < n; ++i) c[i] = b[i];

      map<int, int> whereis;
      for (int i = 0; i < n; ++i) whereis[c[i]] = i;

      int cur = 0;
      //cout << "---\n";
      for (int i = 0; i < n; ++i) {
        int heregoes = a[i];
        int w = whereis[heregoes];
        //cout << i << " is at " << w << endl;
        if (w > i) {
          cur += w - i;
          for (int j = w; j > i; --j) {
            //cout << "pushing " << j-1 << " right\n";
            c[j] = c[j-1];
            whereis[c[j]] = j;
          }
          c[i] = heregoes;
          whereis[heregoes] = i;
//        } else if (w != i) {
//          cout << "FAIL\n";
        }
      }
      if (cur < best) best = cur;
    } while (next_permutation(a, a+n));

    cout << "Case #" << tt << ": " << best << endl;
  }
}
