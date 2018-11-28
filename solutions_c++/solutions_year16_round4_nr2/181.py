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
//#define CHECK
//#define GEN
#endif

const int N = 222;

int n, k;
ld p[N];

bool read() {
#ifdef GEN
	n = 200;
	k = 200;
	forn(i, n) p[i] = 0.5;
	return true;
#endif
	if (!(cin >> n >> k)) return false;
	forn(i, n) assert(cin >> p[i]);
	return true;
}

ld z[N][N];

ld calc(vector<ld> p) {
	memset(z, 0, sizeof(z));

	z[0][0] = 1;
	forn(i, sz(p))
		forn(j, i + 1) {
			z[i + 1][j] += z[i][j] * p[i];
			z[i + 1][j + 1] += z[i][j] * (1 - p[i]);
		}

	return z[sz(p)][sz(p) / 2];
}

ld solve(int test) {
	printf("Case #%d: ", test + 1);

	sort(p, p + n);

	ld ans = 0;
	/*forn(i, n - k + 1) {
		vector<ld> a;
		forn(j, k) a.pb(p[i + j]);
		ans = max(ans, calc(a));
	}

	forn(i1, n - k + 1) {
		fore(i2, i1 + k / 2, n - k / 2 + 1) {
			vector<ld> a;
			forn(j, k / 2) {
				a.pb(p[i1 + j]);
				a.pb(p[i2 + j]);
			}
			//assert(sz(a) == k);
			//cerr << "a=" << a << endl;
			//cerr << "cur=" << cur << endl;
			//exit(0);
			//if (i1 == 0 && i2 + k / 2 == n) cerr << "i1=" << i1 << " i2=" << i2 << " a=" << a << endl;
			ld cur = calc(a);
			ans = max(ans, cur);
		}
	}

	if (1) {
		vector<ld> a;
		forn(i, k / 2) {
			a.pb(p[i]);
			a.pb(p[n - 1 - i]);
		}
		ans = max(ans, calc(a));
	}*/

	forn(cnt, k + 1) {
		vector<ld> a;
		forn(i, cnt) a.pb(p[i]);
		forn(i, k - cnt) a.pb(p[n - 1 - i]);
		ans = max(ans, calc(a));
	}

	cout << ans << endl;
	return ans;
}

ld naive() {
	ld ans = -1;
	int ansmask = -1;
	forn(mask, (1 << n)) {
		vector<ld> a;
		forn(i, n) if (mask & (1 << i)) a.pb(p[i]);
		if (sz(a) != k) continue;
		ld cur = calc(a);
		if (ans < cur) {
			ans = cur;
			ansmask = mask;
		}
	}
	assert(ansmask != -1);
	//cerr << "p=" << mp(p, n) << endl;
	//forn(i, n) if (ansmask & (1 << i)) cerr << p[i] << ' '; cerr << endl;
	return ans;
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
		ld ans1 = solve(tt);
#ifdef CHECK
		ld ans2 = naive();
		if (abs(ans1 - ans2) > EPS) {
			cerr << "exp: " << ans2 << " rec: " << ans1 << endl;
		}
#endif
		cerr << "Time: " << gett() - stime << endl;
		//break;
	}
	
    return 0;
}
