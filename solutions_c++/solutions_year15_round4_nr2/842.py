#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <iomanip>
#include <cmath>

using namespace std;
typedef long double ld;
const ld EPS = 1e-16;
int t, n;
ld V, X;
vector <ld> flows;
vector <ld> temps;

bool dequal(ld a, ld b){
  return fabs(a - b) < EPS;
}

ld solve(){
  if (n == 1){
    if (fabs(temps[0] - X) > EPS) return -1;
    else return (V / flows[0]);
  }

  ld ans = 2e18;

  for (int i = 0; i < n; i++){
    if (fabs(temps[i] - X) < EPS){
      ans = min(ans, V / flows[i]);
    }
  }

  if (dequal(temps[0], X) && dequal(temps[1], X)){
    ans = min(ans, V / (flows[0] + flows[1]));
  }

  for (int i = 0; i < n - 1; i++){
    for (int j = i + 1; j < n; j++){
      ld lo_temp = min(temps[i], temps[j]);
      ld hi_temp = max(temps[i], temps[j]);

      if (X + EPS < lo_temp || X > hi_temp + EPS) continue;

      ld t1 = temps[i], t2 = temps[j];
      ld v1 = flows[i], v2 = flows[j];

      if (t1 < t2) {
	swap(t1, t2);
	swap(v1, v2);
      }

      // binary search
      ld lo = 0.0;
      ld hi = 1.0;
      ld C, D;
      while (fabs(lo - hi) > EPS){
	C = (lo + hi) / 2.0;
	D = 1.0 - C;
	if ((t1 * C + t2 * D) > X) hi = C;
	else lo = C;
      }

      ld fst = (V * C) / v1;
      ld snd = (V * D) / v2;
      ans = min(ans, max(fst, snd));
    }
  }
  return ans;
}

int main(){
  cin >> t;
  for (int cs = 1; cs <= t; cs++){
    cout << fixed << setprecision(10);
    cout << "Case #" << cs << ": ";
    cin >> n >> V >> X;
    flows.resize(n); temps.resize(n);
    for (int i = 0; i < n; i++) cin >> flows[i] >> temps[i];

    ld ans = solve();
    if (ans < -0.5 || ans > 1e18) cout << "IMPOSSIBLE" << endl;
    else cout << ans << endl;
  }
  return 0;
}
