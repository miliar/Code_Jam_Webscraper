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

int n, cnt[3];

bool read() {
	return !!(cin >> n >> cnt[0] >> cnt[1] >> cnt[2]);
}

string alp = "RPS";

string sort(string s) {
	if (sz(s) == 1) return s;
	string a = sort(string(s.substr(0, sz(s) / 2)));
	string b = sort(string(s.substr(sz(s) / 2)));
	return min(a + b, b + a);
}

string gen(string s) {
	forn(i, n) {
		vector<string> ns;
		forn(j, sz(s)) {
			if (s[j] == 'R') ns.pb("RS");
			else if (s[j] == 'S') ns.pb("PS");
			else if (s[j] == 'P') ns.pb("PR");
			else throw;
		}
		s = accumulate(all(ns), string(""));
	}
	return sort(s);
}

void solve(int test) {
	printf("Case #%d: ", test + 1);

	string ans;
	forn(i, 3) {
		string s = gen(string(1, alp[i]));
		assert(sz(s) == (1 << n));
		//cerr << "alp[i]=" << alp[i] << " s=" << s << endl;
		bool ok = true;
		forn(j, 3)
			if (count(all(s), alp[j]) != cnt[j])
				ok = false;
		if (ok) {
			if (ans.empty() || ans > s)
				ans = s;
		}
	}
	if (!ans.empty()) puts(ans.c_str());
	else puts("IMPOSSIBLE");
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
