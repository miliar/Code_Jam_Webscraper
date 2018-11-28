#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <sstream>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std;
typedef vector<int> VI;
typedef vector<VI> MI;
typedef pair<int,int> II;
typedef vector<II> VII;
typedef vector<VII> MII;
typedef long long ll;
typedef vector<ll> Vll;
typedef vector<Vll> Mll;
typedef long double ld;
#define X first
#define Y second

const int mod = 1e9+7;
const int inf = 1e9;
const ld eps = 1e-9;

bool eq(ld a, ld b) {
  return (abs(a-b) < eps);
}

int main() {
  cout.precision(9);
  cout.setf(ios::fixed);
  ios_base::sync_with_stdio(false);
  int ncase = 0;
  int T; cin >> T;
  while (T--) {
    int N;
    ld V, X;
    cin >> N >> V >> X;

    bool possible = true;
    ld ans = 0.0;
    if (N == 1) {
      ld r, c;
      cin >> r >> c;
      if (abs(c-X) < eps) {
        ans = V / r;
      }
      else {
        possible = false;
      }
    }
    else {
      ld r[2], c[2];
      cin >> r[0] >> c[0] >> r[1] >> c[1];
      if (eq(c[0], X) && eq(c[1], X)) {
        ans = V / (r[0]+r[1]);
      }
      else {
        if (eq(c[0], c[1])) {
          possible = false;
        }
        else {
          ld a = (X-c[1])/(c[0]-c[1]);
          if (a < -eps || a > 1.0 + eps) possible = false;
          else {
            ans = max(a* (V/r[0]), (1.0-a) * (V/r[1]));
          }
        }
      }
    }
    cout << "Case #" << ++ncase << ": ";
    if (possible) cout << ans << endl;
    else cout << "IMPOSSIBLE" << endl;
  }
   
}
