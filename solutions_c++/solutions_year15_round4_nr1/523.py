#include <bits/stdc++.h>

using namespace std;

#define forn(i,n) for (int i = 0; i < int(n); i++)
#define ford(i,n) for (int i = int(n) - 1; i >= 0; i--)
#define fore(i,l,r) for (int i = int(l); i <= int(r); i++)
#define all(a) a.begin(), a.end()
#define sz(a) int(a.size())
#define mp make_pair
#define pb push_back
#define ft first
#define sc second
#define x first
#define y second

template<typename X> inline X abs(const X& a) { return a < 0 ? -a : a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9;
//const ld PI = acosl(ld(-1));

const int N = 100 + 13;

char a[N][N];
int n, m;

inline bool read() {
	assert(scanf("%d%d", &n, &m) == 2);
	forn(i, n) {
		assert(scanf("%s", a[i]) == 1);
	}
    return true;
}

int dx[] = {-1, 0, 1, 0};
int dy[] = {0, -1, 0, 1};
string dirs = "^<v>";

inline bool ok(int i, int j) {
	return 0 <= i && i < n && 0 <= j && j < m;
}

inline pt check(int i, int j, int d) {
	pt res = mp(-1, -1);
	for(;;) {
		if (!ok(i, j))
			return res;
		if (a[i][j] != '.') {
			return mp(i, j);
		}
		i += dx[d];
		j += dy[d];
	}
}

inline bool check(int i, int j, int d, pt& idx) {
	idx = check(i, j, d);
	if (idx.ft == -1)
		return false;
	int di = dirs.find(a[idx.ft][idx.sc]);
	
	return ((di + 2) & 3) == d;
}

inline bool check(pt idx) {
	forn(i, 4) {
		pt res = check(idx.ft + dx[i], idx.sc + dy[i], i);
		if (res.ft != -1)
			return true;
	}
	return false;
}

inline void solve(int test) {
	printf("Case #%d: ", test);
	int ans = 0;
	forn(i, n) {
		pt idx;
		if (check(i, 0, 3, idx)) {
			if (!check(idx)) {
				puts("IMPOSSIBLE");
				return;
			}
			ans++;
		}
		if (check(i, m - 1, 1, idx)) {
			if (!check(idx)) {
				puts("IMPOSSIBLE");
				return;
			}
			ans++;
		}
	}
	forn(j, m) {
		pt idx;
		if (check(0, j, 2, idx)) {
			if (!check(idx)) {
				puts("IMPOSSIBLE");
				return;
			}
			ans++;
		}
		if (check(n - 1, j, 0, idx)) {
			if (!check(idx)) {
				puts("IMPOSSIBLE");
				return;
			}
			ans++;
		}
	}
	printf("%d\n", ans);
}

int main()
{
#ifdef SU2_PROJ
    assert(freopen("input.txt", "r", stdin));
    assert(freopen("output.txt", "w", stdout));
#endif

    cout << setprecision(25) << fixed;
    cerr << setprecision(10) << fixed;

    srand(int(time(NULL)));

    int n;
    assert(scanf("%d", &n) == 1);
    forn(i, n) {
	    assert(read());
    	solve(i + 1);
    }

#ifdef SU2_PROJ
    cerr << "TIME: " << clock() << endl;
#endif

    return 0;
}