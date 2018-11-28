#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

double mnt[1001][1001], mxt[1001][1001];
double maxseen[1001];

int main() {
  int T, N, S, prob=1;
  for (cin >> T; T--;) {
    cin >> N >> S;
    vector<int> x(N), y(N), z(N), vx(N), vy(N), vz(N);
    for (int i = 0; i < N; i++) {
      cin >> x[i] >> y[i] >> z[i] >> vx[i] >> vy[i] >> vz[i];
    }

    double lo = 0.0, hi = 10000.0;
    while (hi-lo > 1e-5) {
      double d = (hi+lo)/2;
      for (int i = 0; i < N; i++)
      for (int j = 0; j < N; j++) {
        mnt[i][j] = 1e60; mxt[i][j] = -1e60;
        int xs = vx[i]-vx[j];
        int ys = vy[i]-vy[j];
        int zs = vz[i]-vz[j];
        int dx = x[i]-x[j];
        int dy = y[i]-y[j];
        int dz = z[i]-z[j];
        if (xs == 0 && ys == 0 && zs == 0) {
          if (dx*dx+dy*dy+dz*dz <= d*d) {
            mnt[i][j] = 0; mxt[i][j] = 1e18;
          }
        } else {
          double t = -(xs*dx+ys*dy+zs*dz)/(double)(xs*xs+ys*ys+zs*zs);
          double mnx = dx + t*xs;
          double mny = dy + t*ys;
          double mnz = dz + t*zs;
          if (mnx*mnx + mny*mny + mnz*mnz <= d*d) {
            double d2 = sqrt(d*d-mnx*mnx-mny*mny-mnz*mnz);
            double sd = sqrt(xs*xs+ys*ys+zs*zs);
            mnt[i][j] = t - d2/sd;
            mxt[i][j] = t + d2/sd;
          }
        }
      }

      for (int i = 0; i < N; i++) maxseen[i] = -1.0;
      priority_queue<pair<pair<double, double>, int>> q;
      q.push(make_pair(make_pair(0, S), 0));
      bool success = false;
      while (!q.empty()) {
        double t1 = q.top().first.first, t2 = q.top().first.second;
        int i = q.top().second;
        q.pop();
        if (i == 1) {success = true; break;}

        if (t1 <= maxseen[i]) continue;
        bool change;
        do {
          change = false;
          for (int j = 0; j < N; j++) if (j != i) {
            if (mnt[i][j] > t2) continue;
            if (mxt[i][j] < t1) continue;
            if (mxt[i][j]+S > t2) {t2 = mxt[i][j]+S; change = true;}
          }
        } while (change);
        maxseen[i] = t2;
        for (int j = 0; j < N; j++) if (j != i) {
          if (mnt[i][j] > t2) continue;
          if (mxt[i][j] < t1) continue;
          q.push(make_pair(make_pair(max(t1, mnt[i][j]), min(t2, mxt[i][j])+S), j));
        }
      }
      if (success) hi = d; else lo = d;
    }
    printf("Case #%d: %.6lf\n", prob++, (hi+lo)/2);
  }
}
