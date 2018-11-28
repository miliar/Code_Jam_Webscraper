#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>
#include <string>
#include <cstdlib>

#define BUG(x) cerr << #x << ": " << x << endl;
#define FOR(i, n) for (int i = 0; i < n; ++i)
#define FORV(v, i) for (int i = 0; i < int(v.size()); ++i)
#define TR(v, it) for ((typeof v.begin()) it = v.begin(); it != v.end(); ++it)
#define X first
#define Y second

using namespace std;

const int INF = 2e9;

typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vi> vvi;
typedef vector<vd> vvd;
typedef map<int, int> mii;
typedef set<int> si;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<string> vs;
typedef vector<si> vsi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;

#define double long double

int main() {
  ios_base::sync_with_stdio(false);
  srand(231234);
  cout.setf(ios::fixed);
  cout.precision(8);
  int t;
  cin >> t;
  for (int tt = 1; tt <= t; ++tt) {
    cout << "Case #" << tt << ": ";
    double v, x;
    int n;
    cin >> n >> v >> x;
    if (n == 1) {
      double r, xx;
      cin >> r >> xx;
      if (x != xx) cout << "IMPOSSIBLE" << endl;
      else cout << v / r << endl;
    }
    if (n == 2) {
      double r1, t1, r2, t2;
      cin >> r1 >> t1 >> r2 >> t2;
      if (t2 == x and t1 != x) {
        cout << v / r2 << endl;
        continue;
      }
      if (t1 == x and t2 != x) {
        cout << v / r1 << endl;
        continue;
      }
      if (t1 == x and t2 == x) {
        cout << v / (r1 + r2) << endl;
        continue;
      }
      double y2 = (x - t1) * v / (r2 * (t2 - t1));
      double y1 = (v - y2 * r2) / r1;
      if (y1 < 0 or y2 < 0) cout << "IMPOSSIBLE" << endl;
      else cout << max(y1, y2) << endl;
    }
    
  }
  
  
}