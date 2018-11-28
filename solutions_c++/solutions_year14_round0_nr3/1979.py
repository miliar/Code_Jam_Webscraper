#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <numeric>

using namespace std;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)

int T, R, C, M;
bool grid[5][5], reveal[5][5];
int dx[] = {-1, -1, -1, 0, 0, 1, 1, 1};
int dy[] = {1, -1, 0, 1, -1, 1, -1, 0};

void rec(int r, int c) {
  if (reveal[r][c]) return;
  reveal[r][c] = true;
  bool zero = true;
  FOR(d, 0, 8) {
    int rr = r + dx[d], cc = c + dy[d];
    if (rr < 0 || rr >= R || cc < 0 || cc >= C) continue;
    if (grid[rr][cc]) {
      zero = false;
      break;
    }
  }
  if (zero) {
    FOR(d, 0, 8) {
      int rr = r + dx[d], cc = c + dy[d];
      if (rr < 0 || rr >= R || cc < 0 || cc >= C) continue;
      rec(rr, cc);
    }
  }
}

int main() {
  cin >> T;
  FOR(cs, 1, T+1) {
    cin >> R >> C >> M;
    bool res = false;
    int fr = -1, fc = -1;
    FOR(i, 0, 1 << (R*C)) {
      int cnt = 0;
      FOR(j, 0, (R*C)) if (i & (1 << j)) cnt++;
      if (cnt != M) continue;
      FOR(j, 0, R) FOR(k, 0, C) {
        grid[j][k] = (i & (1 << (j*C + k)));
      }
      if (M == R*C-1) {
        FOR(j, 0, R) FOR(k, 0, C) if (!grid[j][k]) {
          fr = j;
          fc = k;
        }
        res = true;
        break;
      }
      memset(reveal, 0, sizeof(reveal));
      bool found = false;
      FOR(j, 0, R) FOR(k, 0, C) {
        if (grid[j][k]) continue;
        bool zero = true;
        FOR(d, 0, 8) {
          int jj = j + dx[d], kk = k + dy[d];
          if (jj < 0 || jj >= R || kk < 0 || kk >= C) continue;
          if (grid[jj][kk]) {
            zero = false;
            break;
          }
        }
        if (zero) {
          rec(j, k);
          fr = j;
          fc = k;
          found = true;
          goto end;
        }
      }
end:
      if (!found) continue;
      int numrev = 0;
      FOR(j, 0, R) FOR(k, 0, C) if (reveal[j][k]) numrev++;
      if (numrev == R*C - M) {
        res = true;
        break;
      }
    }
    cout << "Case #" << cs << ":" << endl;
    if (res) {
      FOR(i, 0, R) {
        FOR(j, 0, C) {
          if (i == fr && j == fc) {
            cout << 'c';
          } else if (grid[i][j]) {
            cout << '*';
          } else {
            cout << '.';
          }
        }
        cout << endl;
      }
    } else {
      cout << "Impossible" << endl;
    }
  }
	return 0;
}
