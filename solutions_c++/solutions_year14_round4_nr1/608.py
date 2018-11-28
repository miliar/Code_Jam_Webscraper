#include <ctime>
#include <iostream>
#include <iomanip>
#include <set>
#include <algorithm>
#include <cstdio>

using namespace std;

// TEMPLATE {{{
#ifdef ONLINE_JUDGE
#define OJ 1
#else
#define OJ 0
#endif

#define endl '\n'
//#define TIMESTAMP fprintf(stderr, "Execution time: %.3lf s.\n", (double)clock()/CLOCKS_PER_SEC)
#define TIMESTAMP merr << "Execution time: " << fixed << setprecision(3) << (double)clock()/CLOCKS_PER_SEC << " s.\n"
class C_ {}; template <typename T> C_& operator <<(C_& m, const T& s) { if (!OJ) cerr << "\E[91m" << s << "\E[0m"; return m; }
C_ merr;
/// END OF TEMPLATE }}}

int main(void) {
  freopen("input.txt", "rt", stdin); freopen("output.txt", "wt", stdout);
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  int T;
  cin >> T;
  for (int tt = 0; tt < T; tt++) {
    int n,x;
    multiset<int> ms;
    int ans = 0;
    cin >> n >> x;
    for (int i = 0; i < n; i++) {
      int a;
      cin >> a;
      ms.insert(-a);
    }
    while (ms.size()) {
      int used = -*ms.rbegin();
      ms.erase(ms.find(*ms.rbegin()));
      ans++;
      if (ms.size() == 0) break;
      multiset<int>::iterator it = ms.lower_bound(-(x-used));
      int low;
      if (it == ms.end()) {
        low = -*ms.rbegin();
      } else {
        low = -*it;
      }
      if (low <= x-used) {
        ms.erase(ms.find(-low));
      }
    }
    cout << "Case #" << tt+1 << ": " << ans << endl;
  }
  TIMESTAMP;
  return 0;
}
