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

const int N = 111, M = 6;

int n, m;
int p[N];
vector<int> g[N];
string name;
char buf[N];
string z[M];

bool read() {
	if (!(cin >> n)) return false;
	forn(i, n) g[i].clear();
	forn(i, n) {
		assert(scanf("%d", &p[i]) == 1);
		p[i]--;
		if (p[i] != -1) g[p[i]].pb(i);
	}
	assert(cin >> name);
	assert(cin >> m);
	forn(i, m) {
		assert(scanf("%s", buf) == 1);
		z[i] = buf;
	}
	return true;
}

int cnt[N];

int dfs(int v) {
	cnt[v] = 1;
	for (auto to : g[v]) cnt[v] += dfs(to);
	return cnt[v];
}

void solve(int test) {
	printf("Case #%d:", test + 1);
	//cerr << "name: " << name << endl;
	
	forn(i, n) if (p[i] == -1) dfs(i);

	const int M = 40 * 1000;
	vector<int> ans(m, 0);
	forn(tt, M) {
		vector<int> cur;
		cur.reserve(n);
		forn(i, n) if (p[i] == -1) cur.pb(i);

		string s;
		s.reserve(n);
		while (!cur.empty()) {
			//cerr << "s: " << s << endl;

			int sum = 0;
			forn(i, sz(cur)) sum += cnt[cur[i]];

			int idx = -1;
			int val = rand() % sum;
			forn(i, sz(cur)) {
				//cerr << "i: " << i << ", cur[i]: " << cur[i] << endl;
				if (val >= cnt[cur[i]]) {
					val -= cnt[cur[i]];
				} else {
					idx = i;
					break;
				}
			}
			assert(idx != -1);

			//cerr << "sum: " << sum << endl;
			//cerr << "val: " << val << endl;

			int v = cur[idx];
			swap(cur[idx], cur.back());
			cur.pop_back();

			s.pb(name[v]);
			forn(i, sz(g[v])) cur.pb(g[v][i]);
		}
		assert(sz(s) == n);

		//cerr << "s: " << s << endl;
		forn(i, m) if (s.find(z[i]) != string::npos) ans[i]++;
	}

	forn(i, m) cout << ' ' << ld(ans[i]) / M;
	cout << endl;
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
