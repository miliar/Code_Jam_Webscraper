#include <bits/stdc++.h>

#define FOR(i,b,e) for(int i=(b); i <= (e); ++i)
#define FORD(i,b,e) for(int i=(b); i >= (e); --i)
#define REP(i,n) for(int i=0; i < (n); ++i)
#define SIZE(c) (int) (c).size()
#define ALL(c) (c).begin(), (c).end()
#define PB push_back
#define MP make_pair
#define ST first
#define ND second
#define FWD(i,a,b) for (int i=(a); i<(b); ++i)
#define BCK(i,a,b) for (int i=(a); i>(b); --i)
#define PI acos(-1.0)
#define pb push_back
#define mp make_pair
#define st first
#define nd second

using namespace std;

typedef long long int LLI;
typedef pair < int , int > PII;
typedef pair < LLI , LLI > PLL;

typedef vector < int > VI;
typedef vector < bool > VB;
typedef vector < PII > VP;
typedef vector < LLI > VL;
typedef vector < PLL > VPL;

typedef vector < VI > VVI;
typedef vector < VL > VVL;
typedef vector < VB > VVB;
typedef vector < VP > VVP;
typedef vector<double> VD;

VD mult(const VD& vec, double d0, double d1) {
  int n = SIZE(vec);
  VD res(n + 1);
  REP(i, n) res[i] += vec[i] * d0;
  FOR(i, 1, n) res[i] += vec[i-1] * d1;
  return res;
}

int main() {
  ios_base::sync_with_stdio(false);

  cout << fixed << setprecision(10);

  int t;
  cin >> t;

  FOR(TC, 1, t) {
    cout << "Case #" << TC << ": ";

    int n, k;
    cin >> n >> k;
    vector<double> p(n);

    REP(i, n) cin >> p[i];

    sort(ALL(p));

    double res = 0;

    FOR(l, 0, k) {
      vector<double> taken;
      REP(i, l) taken.pb(p[i]);
      REP(i, k-l) taken.pb(p[n-1-i]);
      vector<double> poly = {1.};
      REP(i, k) poly = mult(poly, 1 - taken[i], taken[i]);
      res = max(res, poly[k/2]);
    }

    cout << res << endl;
  }
}
