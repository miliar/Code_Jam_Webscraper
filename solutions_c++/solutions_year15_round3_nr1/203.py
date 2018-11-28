#ifdef MG
#define _GLIBCXX_DEBUG
#endif

#include <iostream>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <climits>
#include <cstring>
#include <cassert>
#include <ctime>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define forl(i, n) for (int i = 1; i <= int(n); i++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define fore(i, l, r) for (int i = int(l); i <= int(r); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(x, y) make_pair((x), (y))
#define ft first
#define sc second
#define x first
#define y second

using namespace std;

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

template<typename X> inline X abs(const X &a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X &a) { return a * a; }
template<typename X, typename Y> inline ostream& operator<< (ostream& out, const pair <X, Y>& p) { return out << '(' << p.x << ", " << p.y << ')'; }
template<typename X> inline ostream& operator<< (ostream& out, const vector<X>& p) { forn(i, sz(p)) { if (i != 0) out << ' '; out << p[i]; } return out; }

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9, PI = acosl(ld(-1));

int n, m, k;

inline bool read()
{
	return scanf("%d%d%d", &n, &m, &k) == 3;
}

inline void solve(int test)
{
	printf("Case #%d: ", test + 1);
	
	int ans = 0;
	for (int i = k - 1; i < m; i += k)
		ans = max(ans, (i + 1) / k + k - (i + 1 == m));

	ans += (n - 1) * (m / k);	
	printf("%d\n", ans);
}

int main()
{
#ifdef MG
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	
	cout << setprecision(10) << fixed;
	cerr << setprecision(5) << fixed;
	
	int T;
	cin >> T;
	
	forn(t, T)
	{
		assert(read());
		solve(t);
	}
	
#ifdef MG
	cerr << "=== TIME: " << clock() << " ===" << endl;
#endif

	return 0;
}
