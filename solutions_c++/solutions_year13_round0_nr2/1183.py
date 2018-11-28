#include <algorithm>
#include <complex>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#define REP(i, n) for(int i=0; i<(int)n; ++i)
#define FOR(i, c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(),(c).end()
#define each(i, c) FOR(i, c)

#define unless(cond) if (!(cond))

using namespace std;

typedef long long int lli;
typedef unsigned long long ull;
typedef complex<double> point;

const int N = 100;
int g[N][N];

bool f(int h, int w)
{
  const int dir = 4;
  const int di[dir] = {0, 0, -1, +1};
  const int dj[dir] = {-1, +1, 0, 0};

  for (int i = 0; i < h; ++i) {
    for (int j = 0; j < w; ++j) {
      bool flg = false;
      for (int d = 0; d < dir; ++d) {
        bool hata = true;
        // if (i == 1 && j == 1 && h == 5 && w == 5) {
        //   cout << d << endl;
        // }
        for (int len = 1; len < N; ++len) {
          int xi = i + (di[d] * len);
          int xj = j + (dj[d] * len);
          int yi = i - (di[d] * len);
          int yj = j - (dj[d] * len);
          // if (i == 1 && j == 1 && h == 5 && w == 5) {
          //   if (0 <= xi && xi < h && 0 <= xj && xj < w) cout << xi << ' ' << xj << " : " << g[xi][xj] << ' ' << d << ' ' << len << endl;
          //   if (0 <= yi && yi < h && 0 <= yj && yj < w) cout << yi << ' ' << yj << " : " << g[yi][yj] << endl;
          // }
          if (0 <= xi && xi < h && 0 <= xj && xj < w) hata = hata && (g[xi][xj] <= g[i][j]);
          if (0 <= yi && yi < h && 0 <= yj && yj < w) hata = hata && (g[yi][yj] <= g[i][j]);
        }
        flg = flg || hata;
      }
      if (!flg) return false;
    }
  }
  return true;
}

int main(int argc, char *argv[])
{
  int tc = 0;
  cin >> tc;
  while (tc--) {
    int h, w;
    cin >> h >> w;
    for (int i = 0; i < h; ++i) {
      for (int j = 0; j < w; ++j) {
        cin >> g[i][j];
      }
    }
    static int TC = 0;
    cout << "Case #" << ++TC << ": " << (f(h, w) ? "YES" : "NO") << endl;
  }
  return 0;
}
