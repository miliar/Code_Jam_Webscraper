#include <bits/stdc++.h>

using namespace std;

struct RTC{~RTC(){cerr << "Time: " << clock() * 1.0 / CLOCKS_PER_SEC <<" seconds\n";}} runtimecount;
#define DBG(X) cerr << #X << " = " << X << '\n';
#define mp make_pair
#define mt make_tuple
#define pb push_back
#define eb emplace_back
#define sz(x) ((int)(x).size())
#define all(c) (c).begin(),(c).end()
#define forn(i, n) for (int i = 0; i < (n); i++)
int c, d, v;
vector<bool> solve(vector<int> den) {
  vector<bool> sepuede(v+1, false);
  vector<int> ans;
  ans.pb(0);
  forn (i, sz(den)) {
    int val = den[i];
    int len = sz(ans);
    forn (j, len) {
      int sum = ans[j] + val;
      if (sum <= v && !sepuede[sum]) {
        sepuede[sum] = true;
        ans.pb(sum);
      }
    }
  }
  return sepuede;
}
int main() {
  int t;
  cin >> t;
  for (int caso = 1; caso <= t; caso++) {
    cin >> c >> d >> v;
    vector<int> den;
    forn (i, d) {
      int tmp;
      cin >> tmp;
      den.pb(tmp);
    }
    int ans = 0;
    while (true) {
      vector<bool> vec = solve(den);
      assert(sz(vec) == (v + 1));
      int obj = -1;
      for (int i = 1; i <= v; i++)
        if (!vec[i]) {
          obj = i;
          break;
        }
      if (obj == -1) break;
      den.pb(obj);
      DBG(obj);
      ans++;
    }
    printf("Case #%d: %d\n", caso, ans);
  }
  return 0;
}
