#include <ctime>
#include <iostream>
#include <iomanip>
#include <set>
#include <vector>
#include <string>
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

int cnt(vector<string> v) {
  set<string> S;
  for (int i = 0; i < (int)v.size(); i++) {
    for (int j = 0; j < (int)v[i].size(); j++) {
      S.insert(v[i].substr(0,j+1));
    }
  }
  return (int)S.size()+1;
}

int pw(int x, int y) {
  int ans = 1;
  for (int i = 0; i < y; i++) {
    ans *= x;
  }
  return ans;
}

int main(void) {
  freopen("input.txt", "rt", stdin); freopen("output.txt", "wt", stdout);
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  int T;
  cin >> T;
  for (int tt = 0; tt < T; tt++) {
    int m,n, lim;
    vector<string> V;
    int ans = 0, cc = 0;
    cin >> m >> n;
    for (int i = 0; i < m; i++) {
      string s;
      cin >> s;
      V.push_back(s);
    }
    lim = pw(n,m);
    for (int bit = 0; bit < lim; bit++) {
      vector<string> A[11];
      int nn = bit;
      bool ok = true;
      int aa = 0;
      for (int i = 0; i < m; i++) {
        A[nn%n].push_back(V[i]);
        nn /= n;
      }
      for (int i = 0; i < n; i++) {
        if (A[i].size() == 0) ok = false;
      }
      if (!ok) continue;
      for (int i = 0; i < n; i++) {
        aa += cnt(A[i]);
      }
      if (aa >= ans) {
        if (aa == ans) cc++;
        else {
          ans = aa;
          cc = 1;
        }
      }
    }
    cout << "Case #" << tt+1 << ": ";
    cout << ans << " " << cc << endl;
    merr << "Case #" << tt+1 << ": ";
    merr << ans << " " << cc << endl;
  }
  TIMESTAMP;
  return 0;
}
