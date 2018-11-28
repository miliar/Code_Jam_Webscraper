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
#define LOG
#endif

const int N = 7;

int n;
char a[N][N];

bool read() {
	if (!(cin >> n)) return false;
	forn(i, n) assert(scanf("%s", a[i]) == 1);
	return true;
}

int g[N][N];
int u, used[N];
int p[N];
int bad;

bool kuhn(int v) {
	if (used[v] == u) return false;
	used[v] = u;

	forn(i, n) {
		if (i == bad) continue;
		if (g[i][v] && (p[i] == -1 || kuhn(p[i]))) {
			p[i] = v;
			return true;
		}
	}
	return false;
}

bool good() {
	forn(i, n) {
		bad = i;

		bool have = false;
		memset(p, -1, sizeof(p));
		forn(j, n) 
			if (g[i][j]) {
				u++;
				if (!kuhn(j)) have = true;
			}
		if (!have) return false;
	}
	return true;
}

void solve(int test) {
	printf("Case #%d: ", test + 1);

	int ans = INF;
	forn(mask, (1 << (n * n))) {
		bool bad = false;
		int cost = 0;
		forn(i, n)
			forn(j, n) {
				if (mask & (1 << (i * n + j))) {
					g[i][j] = 1;
					cost += a[i][j] == '0';
				} else {
					g[i][j] = 0;
					if (a[i][j] == '1') bad = true;
				}
			}

		if (bad) continue;

		//if (cost) continue;

		if (good()) {
			ans = min(ans, cost);
			/*if (cost == 2) {
				forn(i, n) {
					forn(j, n)
						cerr << char('0' + g[i][j]);
					cerr << endl;
				}
				exit(0);
			}*/
		}
	}
	assert(ans != INF);

	cout << ans << endl;
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
