#undef NDEBUG
#ifdef SU2_PROJ
#define _GLIBCXX_DEBUG
#endif

#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define forl(i, n) for (int i = 1; i <= int(n); i++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define fore(i, l, r) for (int i = int(l); i <= int(r); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(x, y) make_pair((x), (y))
#define x first
#define y second

using namespace std;

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9, PI = 3.1415926535897932384626433832795;

const int N = 100 + 3;

int n, m;
char a[N][N];

inline bool read() {
	if (!(cin >> n >> m)) return false;
	forn(i, n) assert(scanf("%s", a[i]) == 1);
	return true;
}
bool bad(int x, int y, int dir) {
	static int dx[] = { -1, 0, 1, 0 };
	static int dy[] = { 0, -1, 0, 1 };
	for (int i = 1; ; i++) {
		int xx = x + dx[dir] * i;
		int yy = y + dy[dir] * i;
		if (!correct(xx, yy, n, m))  {
			return true;
		}
		if (a[xx][yy] != '.') return false;
	}
}

inline void solve() {
	int ans = 0;
	forn(x, n)
		forn(y, m) {
			int dir;
			switch (a[x][y]) {
				case '<': dir = 1; break;
				case '>': dir = 3; break;
				case 'v': dir = 2; break;
				case '^': dir = 0; break;
				default: continue;
			}
			if (bad(x, y, dir)) {
				bool can = false;
				forn(i, 4) can |= !bad(x, y, i);
				if (!can) {
					puts(" IMPOSSIBLE");
					return;
				}
				ans++;
			}
		}
	cout << ' ' << ans << endl;
}

int main() {
#ifdef SU2_PROJ
    assert(freopen("input.txt", "rt", stdin));
    assert(freopen("output.txt", "wt", stdout));
#endif
    
    cout << setprecision(10) << fixed;
    cerr << setprecision(5) << fixed;

	int tc;
	cin >> tc;
	forn(tt, tc) {
		assert(read());
		printf("Case #%d:", tt + 1);
		solve();
	}
	
    return 0;
}
