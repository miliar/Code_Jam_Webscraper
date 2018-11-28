#include <bits/stdc++.h>
#define pb push_back
#define REP(i,n) for (int i=0; i<(int)(n); ++i)
#define ALL(x) x.begin(), x.end()
#define chmax(a, b) a = max(a, b)
#define chmin(a, b) a = min(a, b)

using namespace std;

typedef pair<int, int> pii;
typedef long long ll;
typedef long double ld;
const int INF = 1 << 29;
const ld eps = 1e-8;

int N;
ld V, X;
ld r[100];
ld c[100];

int main(void) {
  int TestCase, TC = 0;
  cin >> TestCase;
  while(TestCase != TC) {
    cin >> N >> V >> X;
    cout << setprecision(10) << fixed;
    REP(i, N) cin >> r[i] >> c[i];
    cout << "Case #" << ++TC << ": ";
    if (N == 1) {
      if (abs(c[0] - X) > eps) cout << "IMPOSSIBLE" << endl;
      else cout << V / r[0] << endl;
    }
    else {
      if (abs(c[0] - c[1]) < eps) {
	if (abs(c[0] - X) > eps) cout << "IMPOSSIBLE" << endl;
	else cout << V / (r[0] + r[1]) << endl;
      }
      else {
	if (X < min(c[0], c[1])  - eps || max(c[0], c[1]) + eps < X) cout << "IMPOSSIBLE" << endl;
	else {
	  ld v1 = (X - c[0]) * V / (c[1] - c[0]);
	  ld v0 = V - v1;
	  cout << max(v0 / r[0], v1 / r[1]) << endl;
	}
      }
    }
  }
  return 0;
}
