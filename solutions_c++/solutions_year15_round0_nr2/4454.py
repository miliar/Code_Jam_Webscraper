#include <bits/stdc++.h>
#include <cassert>
using namespace std;
using ll=long long; using ld=long double;
#define rep(i,s,e) for (int i=(s),__ee=(e);i<__ee;++i)
#define all(x) begin(x),end(x)
#define clr(x,y) memset(x,y,sizeof x)
#define contains(x,y) ((x).find(y)!=end(x))
#define pb push_back
#define mk make_pair
#define mkt make_tuple
#define fst first
#define snd second
#define sz(x) ((int)(x).size())
int dx[]={0,0,1,-1,1,-1,1,-1}, dy[]={-1,1,0,0,1,-1,-1,1};
void run();
int main() {
#ifdef LOCAL
#  define dbg(s, ...) printf(s "\n", __VA_ARGS__)
#else
#  define endl "\n"
#  define dbg(s,...)
#  define FILE "x"
  //freopen(FILE ".in", "r", stdin), freopen(FILE ".out", "w", stdout);
  ios::sync_with_stdio(0);
#endif
  cout << fixed << setprecision(16);
  run();
}

map<vector<char>,int> dp;
int f(vector<char> x) {
  sort(all(x));
  auto it = dp.find(x);
  if (it != end(dp))
    return it->second;
  int& res = dp[x];
  res = 1<<29;
  vector<char> nxt = x;
  bool hasnonzero = 0;
  for (int i = 0; i < x.size(); ++i) {
    if (nxt[i]) nxt[i]--, hasnonzero = 1;
  }
  if (!hasnonzero)
    return res=0;
  res = min(res, 1 + f(nxt));
  for (int i = 0; i < x.size(); ++i) {
    for (int j = 0; j < i; ++j) if (i != j) {
      for (int k = 0; k <= x[i]; ++k) {
        if (x[i] - k >= x[j] + k) {
          x[i]-= k;
          x[j]+= k;
          res = min(res, 1 + f(x));
          x[i]+= k;
          x[j]-= k;
        }
      }
    }
  }
  return res;
}

void run() {
  int T; cin >> T;
  for (int t = 1; t <= T; ++t) {
    //dp.clear(); // TODO remove
    cout << "Case #" << t << ": ";
    int n; cin >> n;
    vector<char> x(13);
    for (int i = 0; i < n; ++i) {
      int y; cin >> y;
      x[i] = y;
    }
    sort(all(x));
    cout << f(x) << endl;
    //for (auto it : dp) {
      //for (int i = 0; i < it.first.size(); ++i) cout << (int)it.first[i] << " ";
      //cout << ": " << it.second << endl;
    //}
  }
}
