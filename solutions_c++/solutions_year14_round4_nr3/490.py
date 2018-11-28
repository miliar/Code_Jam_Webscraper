#include <cassert>
#include <complex>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <fstream>
#include <iostream>
#include <iterator>
#include <limits>
#include <numeric>
#include <sstream>
#include <utility>

#include <algorithm>
#include <bitset>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

#include <memory.h>
using namespace std;

#define Pi 3.141592653589793
#define all(c) (c).begin(), (c).end()
typedef long long ll;

int arr[128][512];

int dx[4][4] = {
  {0, 1, -1, 0},
  {1, 0, 0, -1},
  {-1, 0, 0, 1},
  {0, -1, 1, 0},
};

int dy[4][4] = {
  {-1, 0, 0, 1},
  {0, 1, -1, 0},
  {0, -1, 1, 0},
  {1, 0, 0, -1},
};

int get_dir(int ddx, int ddy) {
  if (ddx == 0) {
    return ddy == -1 ? 1 : 2;
  } else {
    return ddx == -1 ? 0 : 3;
  }
}

struct MV {
  int x;
  int y;
  int d;
  MV (int xx, int yy, int dd) {
    x = xx;
    y = yy;
    d = dd;
  }
};

bool dfs(int xx, int yy, int w, int h) {
  stack<MV> q;
  q.push(MV(xx, yy, 2));
  while (!q.empty()) {
    MV mv = q.top();
    q.pop();
    if (arr[mv.x][mv.y]) {
      continue;
    }
    arr[mv.x][mv.y] = 1;
    if (mv.y == h - 1) {
      return true;
    }
    for (int idx = 3; idx >= 0; --idx) {
      int nx = mv.x + dx[mv.d][idx];
      int ny = mv.y + dy[mv.d][idx];

      if (nx == -1 || nx == w || ny == -1 || arr[nx][ny]) {
        continue;
      }
      int ndir = get_dir(dx[mv.d][idx], dy[mv.d][idx]);
      q.push(MV(nx, ny, ndir));
    }
  }
  return false;
}

int main() {
#ifdef LOCAL_HOST
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
#endif

  int TT; cin >> TT;
  for (int tt = 1; tt <= TT; ++tt) {
    int w, h, b;
    cin >> w >> h >> b;
    memset(arr, 0, sizeof(arr));
    for (int i = 0; i < b; ++i) {
      int x1, y1, x2, y2;
      cin >> x1 >> y1 >> x2 >> y2;
      for (int j = x1; j <= x2; ++j) {
        for (int k = y1; k <= y2; ++k) {
          arr[j][k] = 1;
        }
      }
    }

    int res = 0;
    for (int i = 0; i < w; ++i) {
      if (!arr[i][0] && dfs(i, 0, w, h)) {
        ++res;
      }
    }

    printf("Case #%d: %d\n", tt, res);
  }

  return 0;
}
