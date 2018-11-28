#include <cassert>
#include <cmath>
#include <map>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <cstdio>
inline int getInt(){ int s; scanf("%d", &s); return s; }

#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <complex>

using namespace std;

const double EPS = 1e-8;
const double INF = 1e12;

typedef complex<double> P;
typedef P point;

const double PI = 2 * acos(0);

double normalArg(const P &p){
  double ret = arg(p);
  if(p == P(0, 0)) return 0;
  if(ret < 0) ret += 2 * PI;
  return ret;
}

int main(){
  const int T = getInt();
  REP(t,T){
    const int n = getInt();
    vector<P> ps(n);
    REP(i,n){
      const int x = getInt();
      const int y = getInt();
      ps[i] = P(x, y);
    }

    printf("Case #%d:\n", t + 1);
    REP(i,n){
      vector<double> a(n);
      REP(j,n) a[j] = normalArg(ps[j] - ps[i]);
      // REP(j,n) printf("(%.2f, %.2f)%.2f ", (ps[j] - ps[i]).real(), (ps[j] - ps[i]).imag(), a[j]); puts("");
      sort(a.begin(), a.end());
      assert(a[0] == 0.0);

      REP(i,n-1) a.push_back(a[i + 1] + 2 * PI);

      int f = 1;
      int ans = n - 1;
      for(int j = 1; j < n + n - 1; j++){
	while(a[j] - a[f] > PI + EPS) f++;
	ans = min(ans, n - (1 + (j - f + 1)));
      }
      // REP(j,n) printf("%.2f ", a[j]);

      printf("%d\n", ans);
    }
  }
  return 0;
}
