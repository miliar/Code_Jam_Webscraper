#include <bits/stdc++.h>
#define pb push_back
#define REP(i,n) for (int i=0; i<(int)(n); ++i)
#define ALL(x) x.begin(), x.end()
#define chmax(a, b) a = max(a, b)
#define chmin(a, b) a = min(a, b)

using namespace std;

typedef pair<int, int> pii;
typedef long long ll;
typedef long double ld;
const int INF = 1 << 29;

int R, C;
string grid[100];
map<char, int> ma;
int di[] = {-1, 0, 1, 0};
int dj[] = {0, 1, 0, -1};

bool in(int i, int N) { return 0 <= i && i < N; }

int main(void) {
  int TestCase, TC = 0;
  cin >> TestCase;
  while(TestCase != TC) {
    cout << "Case #" << ++TC << ": ";
    cin >> R >> C;
    REP(i, R) cin >> grid[i];
    ma['^'] = 0; ma['>'] = 1;
    ma['v'] = 2; ma['<'] = 3;
    int res = 0;
    REP(i, R) REP(j, C) if (grid[i][j] != '.') {
      vector<bool> ok(4, false);
      REP(k, 4) {
	int ni = i, nj = j;
	while(true) {
	  ni += di[k];
	  nj += dj[k];
	  if (!in(ni, R) || !in(nj, C)) break;
	  if (grid[ni][nj] != '.') ok[k] = true;
	}
      }
      if (!ok[0] && !ok[1] && !ok[2] && !ok[3]) res = -INF;
      if (ok[ma[grid[i][j]]]) continue;
      res++;
    }
    if (res < 0) cout << "IMPOSSIBLE" << endl;
    else cout << res << endl;
  }
  return 0;
}
