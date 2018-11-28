#include <bits/stdc++.h>
using namespace std;
#define SZ(c) int((c).size())
#define ALL(c) (c).begin(),(c).end()
#define REP(i,n) for(int i=0;i<int(n);++i)
template<class T>inline void check_min(T&a,T b){if(b<a)a=b;}
template<class T>inline void check_max(T&a,T b){if(a<b)a=b;}
typedef long long lint;

const int MAX_N = 1024;

inline double sqr(double x) {
  return x * x;
}

struct Point {
  double x, y, z;
  double vx, vy, vz;
  void read() {
    scanf("%lf%lf%lf", &x, &y, &z);
    scanf("%lf%lf%lf", &vx, &vy, &vz);
  }
  double len(const Point &rhs) {
    return sqrt(sqr(x - rhs.x) + sqr(y - rhs.y) + sqr(z - rhs.z));
  }
} ps[MAX_N];

int n, s;
double dist[MAX_N][MAX_N];

bool check(double limit) {
  vector<int> q = {0};
  basic_string<bool> vis(n, false);
  vis[0] = true;
  REP (i, SZ(q)) {
    int u = q[i];
    if (u == 1) return true;
    REP (v, n) {
      if (!vis[v] && dist[u][v] <= limit) {
        q.push_back(v);
        vis[v] = true;
      }
    }
  }
  return false;
}

double solve() {
  scanf("%d%d", &n, &s);
  REP (i, n) ps[i].read();
  double ma = 0;
  REP (i, n) {
    for (int j = i + 1; j < n; ++j) {
      dist[i][j] = dist[j][i] = ps[i].len(ps[j]);
      check_max(ma, dist[i][j]);
    }
  }
  double low = 0, high = ma;
  REP (i, 200) {
    double mid = (low + high) * 0.5;
    if (check(mid)) high = mid;
    else low = mid;
  }
  return (low + high) * 0.5;
}

int main() {
  int n_case;
  scanf("%d", &n_case);
  for (int index = 1; index <= n_case; ++index) {
    printf("Case #%d: %.20lf\n", index, solve());
  }
  return 0;
}
