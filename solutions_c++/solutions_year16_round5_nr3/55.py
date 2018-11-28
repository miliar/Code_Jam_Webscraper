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

struct pt3 {
	int x, y, z;
};

const int N = 1010;

int n, s;
pt3 a[N], v[N];

bool read() {
	if (!(cin >> n >> s)) return false;
	forn(i, n) {
		assert(scanf("%d%d%d", &a[i].x, &a[i].y, &a[i].z) == 3);
		assert(scanf("%d%d%d", &v[i].x, &v[i].y, &v[i].z) == 3);
	}
	return true;
}

inline int sqr_dist(int i, int j) {
	return sqr(a[i].x - a[j].x) +
			sqr(a[i].y - a[j].y) +
			sqr(a[i].z - a[j].z);
}

int d[N];

void solve(int test) {
	printf("Case #%d: ", test + 1);

	/*forn(i, n)
		forn(j, i)
			cerr << "i: " << i << " j: " << j << " d: " << sqr_dist(i, j) << endl;*/

	forn(i, n) d[i] = INT_MAX;
	queue<int> q;

	d[0] = 0;
	q.push(0);

	while (!q.empty()) {
		int v = q.front();
		q.pop();

		forn(i, n) {
			int nd = max(d[v], sqr_dist(v, i));
			if (d[i] > nd) {
				d[i] = nd;
				q.push(i);
			}
		}
	}

	cout << sqrtl(d[1]) << endl;
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
		cerr << "Test: " << tt + 1 << ", time: " << gett() - stime << endl;
		//break;
	}
	
    return 0;
}
