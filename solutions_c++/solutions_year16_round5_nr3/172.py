#include <cmath>
#include <queue>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <cstdio>
inline int getInt(){ int s; scanf("%d", &s); return s; }

#include <set>

using namespace std;

int main(){
  const int C = getInt();

  REP(cc,C) {
    const int n = getInt();
    const int _ = getInt();

    vector<double> x(n), y(n), z(n);
    vector<double> vx(n), vy(n), vz(n);

    REP(i,n) {
      x[i] = getInt();
      y[i] = getInt();
      z[i] = getInt();
      vx[i] = getInt();
      vy[i] = getInt();
      vz[i] = getInt();
    }

    const double inf = 1e10;
    vector<double> dp(n, inf);

    typedef pair<double, int> data;
    priority_queue<data, vector<data>, greater<data> > pq;
    pq.push(data(0, 0));

    auto f = [&](int i, int j) {
      const double dx = x[i] - x[j];
      const double dy = y[i] - y[j];
      const double dz = z[i] - z[j];
      return dx * dx + dy * dy + dz * dz;
    };

    while(pq.size()) {
      const data d = pq.top(); pq.pop();
      const double dist = d.first;
      const int pos = d.second;

      if(dp[pos] != inf) continue;
      dp[pos] = dist;

      REP(i,n) if(pos != i && dp[i] == inf) {
	const double next = f(pos, i);
	pq.push(data(max(next, dist), i));
      }
    }

    printf("Case #%d: %.10f\n", cc + 1, sqrt(dp[1]));
  }

  return 0;
}
