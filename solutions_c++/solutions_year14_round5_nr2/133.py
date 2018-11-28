#undef NDEBUG
#ifdef SU2_PROJ
#define _GLIBCXX_DEBUG
#endif

#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

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

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }
inline ostream& operator<< (ostream& out, const pt& p) { return out << '(' << p.x << ", " << p.y << ')'; }

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9, PI = 3.1415926535897932384626433832795;

const int N = 100 + 3;
const int M = 10 * 100 + 3;

int P, Q, n;
int a[N], b[N];
int d[N][M];

inline bool read()
{
	if (scanf("%d%d%d", &P, &Q, &n) != 3) return false;
	
	forn(i, n) assert(scanf("%d%d", &a[i], &b[i]) == 2);
	
	return true;
}

inline void solve(int test)
{
	printf("Case #%d: ", test);
	
	memset(d, -1, sizeof(d));
	d[0][1] = 0;
	
	forn(i, n) forn(add, M)
	{
		const int& dv = d[i][add];
		if (dv < 0) continue;
		
		int c1 = (a[i] + Q - 1) / Q;
		
		d[i + 1][add + c1] = max(d[i + 1][add + c1], dv);
		
		c1--;
		
		int rem = a[i] - c1 * Q;
		
		int c2 = (rem + P - 1) / P;
		
		if (add >= c2 - c1)
			d[i + 1][add + c1 - c2] = max(d[i + 1][add + c1 - c2], dv + b[i]);
	}
	
	int ans = 0;
	
	forn(i, M) ans = max(ans, d[n][i]);
	
	cout << ans << endl;
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	cout << setprecision(10) << fixed;
	cerr << setprecision(5) << fixed;
	
	int testCount;
	cin >> testCount;
	
	forl(test, testCount)
	{
		assert(read());
		solve(test);
#ifdef SU2_PROJ
		cerr << "test = " << test << ", clock = " << clock() << endl;
#endif
	}
	
	return 0;
}
