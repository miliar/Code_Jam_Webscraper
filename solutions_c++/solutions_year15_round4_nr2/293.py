#include <bits/stdc++.h>
using namespace std;

const int MAXN = 101;
const double inf = 1.0/0.0;

int N;
double V, X;
double R[MAXN], C[MAXN];

double addX(double v1, double x1, double v2, double x2) {
  return (v1*x1 + v2*x2) / (v1 + v2);
}

double getT(double lv, double lx, double hv, double hx) {
  double t2 = (X * V - lx * V) / ((hx - lx) * hv);
  double t1 = (V - hv * t2) / lv;
  if(t1 < 0 || t2 < 0) return inf;
  return max(t2, t1);
}

int main() {
  int T; cin >> T;
  for(int tc = 1; tc <= T; ++tc) {
    cout << "Case #" << tc << ": ";
    cin >> N >> V >> X;
    for(int i = 0; i < N; ++i) {
      cin >> R[i] >> C[i];
    }

    double lv = 0, lx = 0, mv = 0, mx = 0, hv = 0, hx = 0;
    for(int i = 0; i < N; ++i) {
      if(C[i] == X) {
        mx = addX(mv, mx, R[i], C[i]);
        mv += R[i];
      }else if(C[i] < X) {
        lx = addX(lv, lx, R[i], C[i]);
        lv += R[i];
      } else {
        hx = addX(hv, hx, R[i], C[i]);
        hv += R[i];
      }
    }
    double res = inf;
    if(lv == 0 || hv == 0) {
      res = V / mv;
    } else {
      res = min(res, getT(lv+mv, addX(lv, lx, mv, mx), hv, hx));
      res = min(res, getT(lv, lx, hv+mv, addX(hv, hx, mv, mx)));
    }
    if(res == inf) printf("IMPOSSIBLE\n");
    else printf("%.9f\n", res);
  }
  return 0;
}
