#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cinttypes>
#include <cstdint>
#include <cassert>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <deque>
#include <bitset>
#include <complex>
#include <functional>
#include <numeric>
#include <limits>
#include <utility>

#include <array>
#include <unordered_map>
#include <unordered_set>
#include <tuple>

using namespace std;

typedef long long ll;

const int MAX_L = 110;
const string ds = "^>v<";
const int dx[] = {0, 1, 0, -1};
const int dy[] = {-1, 0, 1, 0};
int n, m;
char a[MAX_L][MAX_L];

bool has_arrow(int i, int j, int k) {
  for (int ni = i + dy[k], nj = j + dx[k];
       0 <= ni && ni < n && 0 <= nj && nj < m;
       ni += dy[k], nj += dx[k]) {
    if (a[ni][nj] != '.') return true;
  }
  return false;
}

int solve() {
  int r = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (ds.find(a[i][j]) != string::npos) {
        int k = ds.find(a[i][j]);
        if (!has_arrow(i, j, k)) {
          bool ok = false;
          for (int k = 0; k < 4; k++) {
            if (has_arrow(i, j, k)) {
              ok = true;
              break;
            }
          }
          if (!ok) {
            return -1;
          }
          r++;
        }
      }
    }
  }
  return r;
}

int main() {
  ll T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    cout << "Case #" << t << ": ";
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        cin >> a[i][j];
      }
    }
    int r = solve();
    if (r == -1) {
      cout << "IMPOSSIBLE" << endl;
    } else {
      cout << r << endl;
    }
  }
}
