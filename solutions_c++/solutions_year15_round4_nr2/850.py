#include <cstdio>
#include <cstring>
#include <cmath>
#include <functional>
#include <utility>
#include <vector>
#include <algorithm>
using namespace std;

const long double eps = 1e-11;

int n;
long double v, x;
long double r[1024], c[1024], d[1024];

vector<pair<long double, long double> > vpd;

int main() {
  int t, T;
  scanf("%d", &T);
  for (t = 1; t <= T; ++t) {
    scanf("%d", &n);
    scanf("%Lf %Lf", &v, &x);
    for (int i = 0; i < n; ++i) {
      scanf("%Lf %Lf", &r[i], &c[i]);
      d[i] = x - c[i];
    }

    long double le, ri, mi;
    le = 0; ri = 1e10;
    bool ok = false;
    for (int iter = 0; iter < 100; ++iter) {
      long double msm = 0;
      long double psm, nsm;
      psm = 0;
      nsm = 0;
      mi = (le + ri) / 2;
      for (int i = 0; i < n; ++i) {
        if (abs(d[i]) < eps) {
          msm += mi * r[i];
        } else if (d[i] > 0) {
          psm += mi * r[i] * d[i];
        } else {
          nsm -= mi * r[i] * d[i];
        }
      }
      if (psm > nsm) {
        vpd.clear();
        long double sm = 0;
        for (int i = 0; i < n; ++i) {
          if (abs(d[i]) > eps) {
            if (d[i] > 0) {
              vpd.push_back(make_pair(d[i], r[i]));
              sm += mi * r[i];
            } else {
              msm += mi * r[i];
            }
          }
        }
        long double de = psm - nsm;
        sort(vpd.begin(), vpd.end(), greater<pair<long double, long double> >());
        for (int i = 0; i < (int) vpd.size(); ++i) {
          if (de < eps) {
            break;
          }
          if (de >= vpd[i].first * vpd[i].second * mi) {
            de -= vpd[i].first * vpd[i].second * mi;
            sm -= vpd[i].second * mi;
          } else {
            long double q = de / vpd[i].first / vpd[i].second;
            de = 0;
            sm -= q * vpd[i].second;
          }
        }
        msm += sm;
      } else {
        vpd.clear();
        long double sm = 0;
        for (int i = 0; i < n; ++i) {
          if (abs(d[i]) > eps) {
            if (d[i] > 0) {
              msm += mi * r[i];
            } else {
              vpd.push_back(make_pair(-d[i], r[i]));
              sm += mi * r[i];
            }
          }
        }
        long double de = nsm - psm;
        sort(vpd.begin(), vpd.end(), greater<pair<long double, long double> >());
        for (int i = 0; i < (int) vpd.size(); ++i) {
          if (de < eps) {
            break;
          }
          if (de >= vpd[i].first * vpd[i].second * mi) {
            de -= vpd[i].first * vpd[i].second * mi;
            sm -= vpd[i].second * mi;
          } else {
            long double q = de / vpd[i].first / vpd[i].second;
            de = 0;
            sm -= q * vpd[i].second;
          }
        }
        msm += sm;
      }
      // printf("OP %lf %lf\n", msm, v);
      if (msm >= v) {
        ok = true;
        ri = mi;
      } else {
        le = mi;
      }
    }
    if (!ok) {
      printf("Case #%d: IMPOSSIBLE\n", t);
    } else {
      printf("Case #%d: %.10Lf\n", t, ri);
    }
  }
  return 0;
}
