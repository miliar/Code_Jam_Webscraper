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

string s;
int k;

bool read() {
	return !!(cin >> s >> k);
}

void solve(int tt) {
  printf("Case #%d: ", tt + 1);

  int ans = 0;
  forn(i, sz(s) - k + 1) {
    if (s[i] == '-') {
      ans++;
      forn(j, k)
        s[i + j] = s[i + j] == '-' ? '+' : '-';
    }
  }
  forn(i, sz(s))
    if (s[i] == '-') {
      puts("IMPOSSIBLE");
      return;
    }
  printf("%d\n", ans);
}

int main() {
#ifdef SU1
  assert(freopen("input.txt", "rt", stdin));
  assert(freopen("output.txt", "wt", stdout));
#endif

  cout << setprecision(10) << fixed;
  cerr << setprecision(5) << fixed;

  int tc;
  cin >> tc;
  forn(tt, tc) {
    cerr << "Case #" << tt + 1 << endl;
    assert(read());
    ld stime = gett();
    solve(tt);
    cerr << "Time: " << gett() - stime << endl;
    //break;
  }

  return 0;
}
