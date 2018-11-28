#include <ctime>
#include <iostream>
#include <iomanip>
#include <set>
#include <map>
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
    int n;
    int A[1111];
    map<int, int> mp, sp;
    set<int> S;
    int l,r;
    int ans = 0;
    cin >> n;
    l = 0, r = n-1;
    for (int i = 0; i < n; i++) {
      cin >> A[i];
      S.insert(A[i]);
      mp[A[i]] = sp[A[i]] = i;
    }
    for (int i = 0; i < n; i++) {
      int mn = *S.begin();
      int p = mp[mn], ssp = sp[mn];
      int ld = p-l, rd = r-p;
      if (ld < rd) {
        ans += ld;
        for (int j = 0; j < ssp; j++) {
          mp[A[j]]++;
        }
        l++;
      } else {
        ans += rd;
        for (int j = ssp+1; j < n; j++) {
          mp[A[j]]--;
        }
        r--;
      }
      S.erase(S.begin());
    }
    cout << "Case #" << tt+1 << ": ";
    cout << ans << endl;
  }
  TIMESTAMP;
  return 0;
}
