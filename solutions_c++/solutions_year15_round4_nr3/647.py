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

const int N = 10100 + 3;

int n;
vector<string> a[N];

inline bool read() {
	if (!(cin >> n)) return false;
	static char buf[1000 * 1000];
	assert(gets(buf));
	forn(k, n) {
		assert(gets(buf));
		int l = int(strlen(buf));
		a[k].clear();
		for (int i = 0, j = 0; i < l; i = j) {
			while (j < l && isalpha(buf[j])) j++;
			a[k].pb(string(buf + i, buf + j));
			j++;
			//cerr << a[k].back() << ' ';
		}
		//cerr << endl;
	}
	return true;
}

map<string, int> id;

int getId(const string& s) {
	if (!id.count(s)) {
		int c = sz(id);
		id[s] = c;
	}
	return id[s];
}

int u = 0, us1[N], us2[N];

vector<int> b[N];

inline void solve() {
	id.clear();

	forn(i, n) {
		b[i].clear();
		forn(j, sz(a[i])) b[i].pb(getId(a[i][j]));
	}

	int ans = INF;
	forn(mask, (1 << n)) {
		if (!(mask & 1)) continue;
		if (mask & 2) continue;
		u++;
		forn(i, n)
			forn(j, sz(a[i]))
				if (mask & (1 << i))
					us1[b[i][j]] = u;
				else
					us2[b[i][j]] = u;
		int v = 0;
		forn(i, sz(id)) v += us1[i] == u && us2[i] == u;
		ans = min(ans, v);
	}
	cout << ans << endl;
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
		printf("Case #%d: ", tt + 1);
		solve();
		cerr << tt + 1 << endl;
	}
	
    return 0;
}
