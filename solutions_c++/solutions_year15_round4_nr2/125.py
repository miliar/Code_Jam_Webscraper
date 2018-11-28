#include <cassert>
#include <cstring>

#include <cstdio>
#include <cstdlib>

#include <algorithm>
#include <iostream>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < int(b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

typedef long long llint;

int n;
double V, p;
vector<double> rs, ts;

double solve() {
  if (n == 1) {
    if (ts[0] == p) return V / rs[0];
    return -1;
  }

  if (n == 2) {
    if (ts[0] > ts[1]) {
      swap(ts[0], ts[1]);
      swap(rs[0], rs[1]);
    }
    if (p < ts[0] || ts[1] < p) return -1;
    if (p == ts[0] && p == ts[1]) return V / (rs[0] + rs[1]);
    if (p == ts[0]) return V / rs[0];
    if (p == ts[1]) return V / rs[1];

    double alpha = (ts[1]-p) / (p-ts[0]);
    double x, y;
    const double eps = 1e-9;
    double ans = 1e100;

    // x lim
    x = rs[0];
    y = x/alpha;
    if (x <= rs[0]+eps && y <= rs[1]+eps) {
      double val = V / (x + y);
      if (val < ans) ans = val;
    }

    // y lim
    y = rs[1];
    x = alpha*y;
    if (x <= rs[0]+eps && y <= rs[1]+eps) {
      double val = V / (x + y);
      if (val < ans) ans = val;
    }    
    
    assert(ans < 1e100);
    return ans;
  }

  assert(false);
}

int main(void) {
  int ntc; scanf("%d", &ntc);
  REP(tc, ntc) {
    rs.clear(); ts.clear();
    scanf("%d %lf %lf", &n, &V, &p);
    REP(i, n) {
      double r, t; scanf("%lf %lf", &r, &t);
      rs.push_back(r);
      ts.push_back(t);
    }

    printf("Case #%d: ", tc+1);
    double val = solve();
    if (val == -1) printf("IMPOSSIBLE\n");
    else printf("%.20lf\n", val);
    fflush(stdout);
  }
  return 0;
}   
