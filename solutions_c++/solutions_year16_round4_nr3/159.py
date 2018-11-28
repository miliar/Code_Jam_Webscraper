#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define nfor(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define fore(i, l, r) for (int i = int(l); i < int(r); i++)
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
typedef pair<int, int> pti;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

template<typename A, typename B> inline ostream& operator<< (ostream& out, const pair<A, B>& p) { return out << "(" << p.x << ", " << p.y << ")"; }
template<typename T> inline ostream& operator<< (ostream& out, const vector<T>& a) { out << "["; forn(i, sz(a)) { if (i) out << ','; out << ' ' << a[i]; } return out << " ]"; } 
template<typename T> inline ostream& operator<< (ostream& out, const set<T>& a) { return out << vector<T>(all(a)); }
template<typename X, typename Y> inline ostream& operator<< (ostream& out, const map<X, Y>& a) { return out << vector<pair<X, Y>>(all(a)); }
template<typename T> inline ostream& operator<< (ostream& out, const pair<T*, int>& a) { return out << vector<T>(a.x, a.x + a.y); }

inline ld gett() { return ld(clock()) / CLOCKS_PER_SEC; }

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9, PI = 3.1415926535897932384626433832795;

#ifdef SU1
//#define LOG
#endif

const int N = 200;

int n, m;
int perm[N];

bool read() {
	if (!(cin >> n >> m)) return false;
	forn(i, 2 * (n + m)) {
		assert(scanf("%d", &perm[i]) == 1);
		perm[i]--;
	}
	return true;
}

inline int getNum(int x, int y) {
	if (x == -1 && 0 <= y && y < m) return y;
	if (y == m && 0 <= x && x < n) return m + x;
	if (x == n && 0 <= y && y < m) return m + n + (m - 1 - y);
	if (y == -1 && 0 <= x && x < n) return m + n + m + (n - 1 - x);
	return -1;
}

inline int getp(const pti& p) {
	if (p.x < 0) return 2;
	if (p.y >= m) return 3;
	if (p.x >= n) return 0;
	if (p.y < 0) return 1;
	return -1;
}

int dx[] = { -1, 0, 1, 0 };
int dy[] = { 0, 1, 0, -1 };

struct state {
	int x, y, p;
	state() {
	}
	state(int x, int y): x(x), y(y) {
		p = getp(mp(x, y));
		assert(p != -1);
	}
	state(int x, int y, int p): x(x), y(y), p(p) {
	}
	state same() {
		return state(x + dx[p], y + dy[p], (p + 2) % 4);
	}
};

inline bool operator== (const state& a, const state& b) {
	return a.x == b.x && a.y == b.y && a.p == b.p;
}

inline ostream& operator<< (ostream& out, const state& a) { return out << "(" << a.x << ", " << a.y << ", " << a.p << ")"; }

char a[N][N];
int u, used[N][N][4];
int good[N * N];
int CNT;

bool dfs(state v) {
	int& cused = used[v.x + 1][v.y + 1][v.p];
	if (cused == u) return true;
	cused = u;

	int vv = getNum(v.x, v.y);
	CNT += vv != -1;

#ifdef LOG
	cerr << "v=" << v << endl;
	cerr << "vv=" << vv << endl;
#endif

	if (vv != -1 && !good[vv]) return false;
	
	if (!dfs(v.same())) return false;

	if (vv == -1) {
		state nv(v);
		if (a[v.x][v.y] == '\\') {
			nv.p ^= 1;
			if (!dfs(nv)) return false;
		} else {
			nv.p = (nv.p + 2) % 4;
			nv.p ^= 1;
			//cerr << "nv=" << nv << endl;
			if (!dfs(nv)) return false;
		}
	}

	return true;
}

bool bfs(int s, int t) {
	state spos(-1, -1, -1);
	fore(x, -1, n + 1)
		fore(y, -1, m + 1) {
			if (getNum(x, y) == s) spos = state(x, y);
			//if (getNum(x, y) == t) tpos = state(x, y);
		}

	forn(i, 2 * (n + m)) good[i] = false;
	good[s] = good[t] = true;

#ifdef LOG
	cerr << "New dfs" << endl;
#endif

	u++;
	CNT = 0;
	if (!dfs(spos)) return false;
	return CNT == 2;
}

bool check() {
#ifdef LOG
	forn(i, n) {
		forn(j, m) cerr << a[i][j];
		cerr << endl;
	}
#endif

	forn(i, n + m)
		if (!bfs(perm[2 * i], perm[2 * i + 1]))
			return false;

	forn(i, n) {
		forn(j, m) putchar(a[i][j]);
		puts("");
	}

	return true;
}

void solve(int test) {
	/*fore(x, -1, n + 1) {
		fore(y, -1, m + 1)
			cerr << setw(3) << getNum(x, y);
		cerr << endl;
	}*/

	printf("Case #%d:\n", test + 1);
	forn(mask, (1 << (n * m))) {
		//if (!mask) continue; // WAAAAAAAAAAAAAAAARNING

		forn(i, n)
			forn(j, m) {
				if (mask & (1 << (i * m + j))) a[i][j] = '/';
				else a[i][j] = '\\';
			}
		//check();
		if (check()) return;
	}
	puts("IMPOSSIBLE");
}

int main() {
#ifdef SU1
    assert(freopen("input.txt", "rt", stdin));
    assert(freopen("output.txt", "wt", stdout));
#endif
    
    cout << setprecision(10) << fixed;
    cerr << setprecision(5) << fixed;

	int tc;
	assert(cin >> tc);
	forn(tt, tc) {
		assert(read());
		ld stime = gett();
		solve(tt);
		cerr << "Time: " << gett() - stime << endl;
		//break;
	}
	
    return 0;
}
