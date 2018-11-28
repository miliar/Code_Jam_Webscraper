#include <bits/stdc++.h>

#define each(i, c) for (auto& i : c)
#define unless(cond) if (!(cond))

using namespace std;

typedef long long int lli;
typedef unsigned long long ull;
typedef complex<double> point;

template<typename P, typename Q>
ostream& operator << (ostream& os, pair<P, Q> p)
{
  os << "(" << p.first << "," << p.second << ")";
  return os;
}

int main(int argc, char *argv[])
{
  int tc;
  cin >> tc;
  while (tc--) {
    int h, w, n;
    cin >> h >> w >> n;
    bool g[h][w];
    const int inf = 1 << 29;
    int mn = inf;
    for (int bit = 0; bit < (1 << (h * w)); ++bit) {
      if (__builtin_popcount(bit) != n) continue;
      fill(&g[0][0], &g[h - 1][w - 1] + 1, false);
      int m = bit;
      for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) {
          g[i][j] = (m & 1);
          m /= 2;
        }
      }
      int cnt = 0;
      for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) {
          for (int d = 0; d < 2; ++d) {
            const int di[] = {0, +1};
            const int dj[] = {+1, 0};
            int ni = i + di[d];
            int nj = j + dj[d];
            unless (0 <= ni && ni < h) continue;
            unless (0 <= nj && nj < w) continue;
            cnt += (g[i][j] && g[ni][nj]);
          }
        }
      }
      mn = min(mn, cnt);
    }
    static int cnt = 0;
    cout << "Case #" << ++cnt << ": " << mn << endl;
  }
  return 0;
}
