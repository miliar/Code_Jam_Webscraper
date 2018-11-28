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

lli cost(int src, int dst, const lli N)
{
  if (src == dst) return 0;
  lli ret = 0;
  lli dist = dst - src;

  ret += dist * N;
  ret -= (dist - 1) * dist / 2;

  return ret;
}

int main(int argc, char *argv[])
{
  int tc;
  cin >> tc;
  while (tc--) {
    int n, m;
    cin >> n >> m;

    const int N = 100 + 5;
    int p[N][N];
    fill(&p[0][0], &p[N - 1][N - 1] + 1, 0);

    lli sum = 0;

    for (int i = 0; i < m; ++i) {
      lli a, b, c;
      cin >> a >> b >> c;
      --a;
      --b;
      p[a][b] += c;
      sum += cost(a, b, n) * c;
    }

    while (true) {
      bool hata = true;
      for (int a = 0; a < n; ++a) {
        for (int b = a + 1; b < n; ++b) {
          if (p[a][b] == 0) continue;
          for (int x = a; x <= b; ++x) {
            for (int y = x + 1; y < n; ++y) {
              if (p[x][y] == 0) continue;
              if (a == x && b == y) continue;

              lli curr = cost(a, b, n) + cost(x, y, n);
              lli next = cost(a, y, n) + cost(x, b, n);
              if (next < curr) {
                lli mn = min(p[a][b], p[x][y]);

                // cout << a+1 << " <-> " << b+1 << " : " << p[a][b] << endl;
                // cout << x+1 << " <-> " << y+1 << " : " << p[x][y] << endl;
                // cout << endl;

                p[a][b] -= mn;
                p[x][y] -= mn;

                p[a][y] += mn;
                p[x][b] += mn;

                hata = false;
              }
            }
          }
        }
      }
      if (hata) break;
    }

    lli res = 0;
    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < N; ++j) {
        // if (p[i][j]) {
        //   cout << ">: " << i+1 << " <-> " << j+1 << ", " << p[i][j] << endl;
        // }
        res += cost(i, j, n) * p[i][j];
      }
    }
    static int cnt = 0;
    cout << "Case #" << ++cnt << ": " << max(0LL, sum - res) << endl;
  }

  // {
  //   int n = 6;
  //   for (int i = 0; i < n; ++i) {
  //     for (int j = i; j < n; ++j) {
  //       cout << i << ' ' << j << ": " << cost(i, j, n) << endl;
  //     }
  //   }
  // }

  return 0;
}
