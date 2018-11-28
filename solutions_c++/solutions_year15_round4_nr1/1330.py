#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <iomanip>
#include <cmath>
#include <string>
#include <cstring>
#include <algorithm>
using namespace std;

typedef long long ll;

#define all(x) x.begin(), x.end()

#ifdef VOIT_LOCAL
#define debug(x) cerr << x << endl;
#else
#define debug(x)
#endif

const int MAXN = 200;
int a[MAXN][MAXN];
pair<int, int> dp[MAXN][MAXN][4];

#define left asd
#define right asdasd

enum state
{
  down, up, right, left, none
};

state convert(char c)
{
  if (c == '.') return none;
  if (c == '>') return right;
  if (c == '<') return left;
  if (c == '^') return up;
  if (c == 'v') return down;
  abort();
}

void solve(int t)
{
  int n, m;
  cin >> n >> m;
  for (int i = 0; i < n; i++) {
    string s;
    cin >> s;
    for (int j = 0; j < m; j++) {
      a[i][j] = convert(s[j]);
    }
  }

  const int DX[] = {1, -1, 0, 0};
  const int DY[] = {0, 0, 1, -1};
  memset(dp, -1, sizeof dp);
  vector<pair<int, int> > st;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (a[i][j] == none) {
        continue;
      }

      if (i == 0 || i == n - 1 || j == 0 || j == m - 1) st.emplace_back(i, j);

      for (int k = 0; k < 4; k++) {
        int dx = DX[k];
        int dy = DY[k];

        int sx = i + dx;
        int sy = j + dy;
        while (sx >= 0 && sy >= 0 && sx < n && sy < m) {
          if (a[sx][sy] != none) {
            dp[i][j][k] = {sx, sy};
            break;
          }
          sx += dx;
          sy += dy;
        }
      }
    }
  }

  cout << "Case #" << t << ": ";
  int ans = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (a[i][j] != none && dp[i][j][a[i][j]].first == -1) {
        int mx = -1;
        for (int k = 0; k < 4; k++) {
          mx = max(mx, dp[i][j][k].first);
        }
        if (mx != -1) {
          ans++;
        } else {
          cout << "IMPOSSIBLE\n";
          return;
        }
      }
    }
  }

  cout << ans << endl;
}

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cin.exceptions(istream::failbit | istream::badbit);

  try {
    int test_count = 0;
    int te;
    cin >> te;
    for (int t = 0; t < te; t++) {
      time_t start = clock();
      solve(t + 1);
      debug("\n===== Test " << ++test_count << " solved in "
            << (int) ((clock() - start) * 1000.0 / CLOCKS_PER_SEC)
            << "ms =====");
    }
  } catch (istream::failure e) {
    // no more tests
  }
}
