/* 
  2014.03.26 15:10
  http://codeforces.ru/gym/100289/
*/


#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cmath>
#include <memory.h>
#include <cmath>
#include <string> 
#include <ctime>

using namespace std;

// #undef Fdg_Home

int n, m;
vector<vector<int>> v;

set<vector<vector<int>>> f;

vector<vector<int>> shift(vector<vector<int>> v) {
  auto ret = v;
  for (int j = 0; j + 1 < v[0].size(); ++j) {
    for (int i = 0; i < v.size(); ++i)
      swap(ret[i][j], ret[i][j + 1]);
  }
  return ret;
}

int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};

bool ok(vector<vector<int>> v) {
  for (int i = 0; i < v.size(); ++i) {
    for (int j = 0; j < v[i].size(); ++j) {
      if (v[i][j] == 0) continue;
      int eq = 0, zr = 0;
      for (int t = 0; t < 4; ++t) {
        int nx = i + dx[t], ny = (j + dy[t] + m) % m;
        if (nx < 0 || nx >= n) continue;
        if (v[nx][ny] == 0) ++zr;
        if (v[nx][ny] == v[i][j]) ++eq;
      }
      // if (v[i][j] == 0) {
      //   cout << eq << " " << zr << endl; 
      // }
      if (eq <= v[i][j] && v[i][j] <= eq + zr);
      else return false;
    }
  }
  return true;
}

void go(int x, int y) {
  if (x == n) {
    if (ok(v)) {
      auto ret = v, cur = v;
      for (int i = 0; i < m; ++i) {
        cur = shift(cur);
        ret = min(ret, cur);
      }
      f.insert(ret);
      // for (int i = 0; i < n; ++i) {
      //   for (int j = 0; j < m; ++j) {
      //     cout << ret[i][j] << "  ";
      //   }
      //   cout << endl;
      // }
      // cout << endl;
    }
    return;
  }
  int nx = x, ny = y + 1;
  if (ny == m) ++nx, ny = 0;
  for (int i = 1; i <= 3; ++i) {
    v[x][y] = i;
    if (ok(v))
      go(nx, ny);
    v[x][y] = 0;
  }
}

int solve() {
  f.clear();
  v = vector<vector<int>>(n, vector<int>(m, 0));
  go(0, 0);
  return f.size();
}

void solveTest(int CS) {
  printf("Case #%d: ", CS);
  cin >> n >> m;
  // for (n = 1; n <= 6; ++n)
  //   for (m = 1; m <= 6; ++m)
  printf("%d\n", solve());
}

int main() {
// #ifndef Fdg_Home
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
// #endif
  int T;
  scanf("%d\n", &T);
  for (int test = 1; test <= T; ++test) {
    solveTest(test);
  }
  return 0;
}