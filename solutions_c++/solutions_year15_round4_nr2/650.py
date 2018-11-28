#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;
#define DEBUG(x) cerr << '>' << #x << ':' << (x) << endl;
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define REP(i,a) for(int i=0; i<(a);++i)
inline bool EQ(double a, double b) {return fabs(a-b) < 1e-9;}

const int INF = 1<<29;
typedef long long ll;

vector<pair<double, double>> vecs;
vector<pair<double, double>> ivecs;

bool estimateMax(double* hi) {
  bool p1 = false, p2 = false;
  double t1 = 0, t2 = 0;
  for (auto v : vecs) {
    if (v.first >= v.second - 1e-8) {
      if (p1 == false) {
        p1 = true;
        t1 = 1.0 / v.first;
      } else {
        t1 = min(t1, 1.0 / v.first);
      }
    }
    if (v.second >= v.first - 1e-8) {
      if (p2 == false) {
        p2 = true;
        t2 = 1.0 / v.second;
      } else {
        t2 = min(t2, 1.0 / v.second);
      }
    }
  }
  if (p1 && p2) {
    *hi = 2 * max(t1, t2);
    return true;
  } else {
    return false;
  }
}

bool canReach(const vector<pair<double, double>>& vecs, double t) {
  double x = 0, y = 0;
  for (auto p : vecs) {
    double dx = p.first * t;
    double dy = p.second * t;
    double nx = x + dx;
    double ny = y + dy;
    if (nx + ny >= 2) {
      double a = dy / dx;
      double b = -1;
      double c = y - dy / dx * x;
      double d = (a + b + c) / sqrt(a*a+b*b);
      return d < 1e-14;
    }
    x = nx;
    y = ny;
  }
  return false;
}

bool isPossible(double t) {
  /*
  fprintf(stderr, "t: %.10lf\n", t);
  DEBUG(canReach(vecs, t));
  DEBUG(canReach(ivecs, t));
  */
  return canReach(vecs, t) && canReach(ivecs, t);
}

class RelCmp {
public:
  bool operator() (pair<double, double> p1, pair<double, double> p2) const {
    double r1 = p1.first / p1.second;
    double r2 = p2.first / p2.second;
    return r1 > r2;
  }
};

void solve() {
  vecs.clear();
  ivecs.clear();
  int N;
  double V, X;
  scanf("%d%lf%lf", &N, &V, &X);
  REP(i,N) {
    double R, C;
    scanf("%lf%lf", &R, &C);
    vecs.push_back({R/V, C*R / (V*X)});
  }
  double lo = 0;
  double hi;
  bool possible = estimateMax(&hi);
  if (!possible) {
    printf("IMPOSSIBLE\n");
    return;
  }
  for (auto p : vecs) {
    ivecs.push_back({p.second, p.first});
  }
  sort(vecs.begin(), vecs.end(), RelCmp());
  sort(ivecs.begin(), ivecs.end(), RelCmp());
  while (hi - lo > 1e-8) {
    double med = (hi+lo) / 2;
    if (isPossible(med)) {
      hi = med;
    } else {
      lo = med;
    }
  }
  printf("%.10lf\n", (hi+lo) / 2);
}

int main() {
  int T;
  scanf("%d", &T);
  REP(t,T) {
    printf("Case #%d: ", t+1);
    solve();
  }
  return 0;
}
