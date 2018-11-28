#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

#define DEBUG(x) cerr << #x << " = " << (x) << endl

#define FR first
#define SC second

using namespace std;

typedef long long ll;
typedef long double ld;

template <class Ta, class Tb> inline Tb cast(Ta a) {
  stringstream ss;
  ss << a;
  Tb b;
  ss >> b;
  return b;
};

const int dy[] = {-1, 0, 1, 0};
const int dx[] = {0, 1, 0, -1};

pair<int, int> next_arrow(const vector<vector<int> >& a, int y, int x, int d) {
  int r = int(a.size());
  int c = int(a[0].size());
  for (int k = 1;; ++k) {
    int i = y + k * dy[d];
    int j = x + k * dx[d];
    if (i < 0 || i >= r) return pair<int, int>(-1, -1);
    if (j < 0 || j >= c) return pair<int, int>(-1, -1);
    if (a[i][j] != -1) return pair<int, int>(i, j);
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  int T;
  cin >> T;
  for (int ca = 1; ca <= T; ++ca) {
    int r, c;
    cin >> r >> c;
    vector<vector<int> > a(r, vector<int>(c));
    for (int i = 0; i < r; ++i) {
      for (int j = 0; j < c; ++j) {
        char dir;
        cin >> dir;
        if (dir == '.') a[i][j] = -1;
        else if (dir == '^') a[i][j] = 0;
        else if (dir == '>') a[i][j] = 1;
        else if (dir == 'v') a[i][j] = 2;
        else if (dir == '<') a[i][j] = 3;
      }
    }

    int ans = 0;
    for (int i = 0; i < r && ans != -1; ++i) {
      for (int j = 0; j < c && ans != -1; ++j) if (a[i][j] != -1) {
        int d = a[i][j];
        if (next_arrow(a, i, j, d).FR != -1) continue;
        bool ok = false;
        for (int dir = 0; dir < 4; ++dir) {
          pair<int, int> na = next_arrow(a, i, j, dir);
          if (na.FR != -1) {
            ok = true;
          }
        }
        if (ok) {
          ++ans;
        } else {
          ans = -1;
        }
      }
    }

    cout << "Case #" << ca << ": ";
    if (ans == -1) cout << "IMPOSSIBLE" << endl;
    else cout << ans << endl;
  }
}

