#include <algorithm>
#include <queue>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <cstdio>
inline int getInt(){ int s; scanf("%d", &s); return s; }
inline double getDouble(){ double s; scanf("%lf", &s); return s; }

#include <set>

using namespace std;

double solve(const vector<double> &v) {
  const int n = v.size();
  vector<vector<double> > dp(n + 1, vector<double>(n + 1));
  dp[0][0] = 1.0;

  for(double d : v) {
    vector<vector<double> > next(n + 1, vector<double>(n + 1));

    REP(i,n) REP(j,n) {
      next[i + 1][j] += dp[i][j] * d;
      next[i][j + 1] += dp[i][j] * (1 - d);
    }

    dp.swap(next);
  }

  return dp[n/2][n/2];
}

int main(){
  const int T = getInt();
  REP(t,T) {
    const int n = getInt();
    const int k = getInt();
    vector<double> p(n); REP(i,n) p[i] = getDouble();
    sort(p.begin(), p.end());

    double ans = 0;
    REP(i,k+1) {
      vector<double> v;
      REP(j,i) v.push_back(p[j]);
      REP(j,k-i) v.push_back(p[n - 1 - j]);
      ans = max(ans, solve(v));
    }

    printf("Case #%d: %.10f\n", t + 1, ans);
  }
  return 0;
}
