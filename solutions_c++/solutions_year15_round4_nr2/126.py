#include <bits/stdc++.h>

#define REP(i,n) for(int i=0;i<(int)(n);i++)
#define ALL(x) (x).begin(),(x).end()

using namespace std;

typedef long double ld;

const ld eps = 1e-11;

ld R[128], C[128];

void solve(int cas) {
  int N; cin >> N;
  ld V, X; cin >> V >> X;
  REP(i,N) cin >> R[i] >> C[i];
  ld res = 1e17;
  ld liv = 0, lic = 0, lav = 0, lac = 0, lcv = 0, lcc = 0;
  REP(i,N) {
    if (abs(C[i] - X) < eps) { lcv += R[i]; lcc += R[i] * C[i]; }
    if (C[i] < X) { liv += R[i]; lic += R[i] * C[i]; }
    else { lav += R[i]; lac += R[i] * C[i]; }
  }
  if (lcv > eps) res = min(res, V / lcv);

  if (liv > eps && lav > eps) {
    ld num1 = (liv + lcv) * X - (lic - lcc);
    ld num2 = lav * X - lac;
    ld v = V / ((liv + lcv) * num2 - lav * num1);
    if (num2 * v > -num1 * v) res = min(res, num2 * v);
    
    swap(liv, lav); swap(lic, lac);
    num1 = (liv + lcv) * X - (lic - lcc);
    num2 = lav * X - lac;
    v = V / ((liv + lcv) * num2 - lav * num1);
    if (num2 * v > -num1 * v) res = min(res, num2 * v);
  }
    
  cout << "Case #" << cas << ": ";
  if (res > 1e16) cout << "IMPOSSIBLE" << endl;
  else cout << res << endl;
}

int main() {
  int T; cin >> T;
  cout << setprecision(9) << fixed;
  REP(cas,T) solve(cas + 1);
  return 0;
}
