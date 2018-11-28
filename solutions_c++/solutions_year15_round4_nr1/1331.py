#include <iostream>
#include <vector>
using namespace std;

const int GOOD = 1;
const int BAD = -1;
const int EMPTY = 2;
const int UNKNOWN = 0;
const int WAS = 3;

int n;
int m;
int ans;
vector<vector<int>> f;
bool imp;
const int dx[] = {-1,0,1,0};
const int dy[] = {0,-1,0,1};
const char dc[] = {'^', '<', 'v', '>'};


bool go(int x, int y, vector<string>&a, int d) {
  do {
    x += dx[d];
    y += dy[d];
    if (x < 0 || y < 0 || x >= n || y >= m) { break; }
    if (a[x][y] != '.') return true;
  } while (true);
  return false;
}



string solve(vector<string>& a) {
  ans = 0;
  imp = false;
  n = a.size();
  m = a.front().size();
  for (int i = 0; i < n; ++i)
    for (int j= 0; j < m; ++j) {
      if (a[i][j] =='.') continue;
      int d = 0;
      for (d = 0; d < 4; ++d) if (a[i][j] == dc[d]) break;
      if (!go(i,j,a,d)) {
        ans ++;
        if (!(go(i,j,a,0) ||
        go(i,j,a,1) ||
        go(i,j,a,2) ||
        go(i,j,a,3))) {
          return "IMPOSSIBLE";
        }
      }
    }
  return to_string(ans);
}

int main() {
  int tc;
  cin >> tc;
  for (int t = 1; t <= tc; ++t) {
    int x,y;
    cin >> x >> y;
    vector<string> a(x);
    for (auto& s : a) cin >> s;
    cout << "Case #" << t << ": " <<  solve(a) << endl;

  }
}
