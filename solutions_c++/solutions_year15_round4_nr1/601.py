#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for(__typeof__((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define mp make_pair
#define pb push_back
#define has(c,i) ((c).find(i) != (c).end())
#define DBG(...) ({ if(1) fprintf(stderr, __VA_ARGS__); })
#define DBGDO(X) ({ if(1) cerr << "DBGDO: " << (#X) << " = " << (X) << endl; })

const int maxRC = 104;

int TC;
int R, C;
string grid[maxRC];

bool valid(int r, int c) {
	return min(r,c) >= 0 && r < R && c < C;
}

struct Dir {
	char c;
	int dr, dc;
};

Dir dir[4] = {
	{'^', -1, 0},
	{'<', 0, -1},
	{'>', 0, 1},
	{'v', 1, 0},
};

int main() {
	ios::sync_with_stdio(false);

	cin >> TC;
	FOR(tc, 1, TC+1) {
		int res = 0;

		cin >> R >> C;
		FOR(r,0,R) cin >> grid[r];

		FOR(sr,0,R) FOR(sc,0,C) {
			if (grid[sr][sc] == '.') continue;
			int r = sr;
			int c = sc;

			int d = 0;
			while (d < 4 && dir[d].c != grid[sr][sc]) d++;
			assert(d < 4);

			int dr = dir[d].dr;
			int dc = dir[d].dc;
			bool ok = false;
			while (true) {
				r += dr; c += dc;
				if (!valid(r,c)) break;
				if (grid[r][c] != '.') {
					ok = true;
					break;
				}
			}
			if (ok) continue;

			FOR(e,0,4) {
				if (e == d) continue;
				r = sr;
				c = sc;
				dr = dir[e].dr;
				dc = dir[e].dc;
				while (true) {
					r += dr; c += dc;
					if (!valid(r,c)) break;
					if (grid[r][c] != '.') {
						ok = true;
						res++;
						break;
					}
				}
				if (ok) break;
			}
			if (!ok) {
				res = -1;
				break;
			}
		}

		if (res < 0)
			printf("Case #%d: IMPOSSIBLE\n", tc);
		else
			printf("Case #%d: %d\n", tc, res);
	}
}
