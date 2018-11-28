// {{{ template
#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<string> vs;
typedef vector<long long> vll;
typedef vector<pii> vpii;
// }}}

const int dr[] = {-1, 0, 1, 0};
const int dc[] = {0, -1, 0, 1};

const string dir = "^<v>";

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int n, m;
    cin >> n >> m;
    vs grid(n);
    for (int i = 0; i < n; i++) {
      cin >> grid[i];
    }
    bool possible = true;
    int ans = 0;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        if (grid[i][j] == '.') {
          continue;
        }
        vb can(4, true);
        for (int k = 0; k < 4; k++) {
          int pr = i, pc = j;
          while (pr >= 0 && pr < n && pc >= 0 && pc < m) {
            int nr = pr + dr[k], nc = pc + dc[k];
            if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] != '.') {
              break;
            }
            pr = nr;
            pc = nc;
          }
          if (pr < 0 || pr >= n || pc < 0 || pc >= m) {
            can[k] = false;
          }
        }
        int d = find(begin(dir), end(dir), grid[i][j]) - begin(dir);
        if (!can[0] && !can[1] && !can[2] && !can[3]) {
          possible = false;
        } else {
          ans += can[d] == false;
        }
      }
    }
    if (possible) {
      cout << "Case #" << t << ": " << ans << endl;
    } else {
      cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
    }
  }
  return 0;
}

