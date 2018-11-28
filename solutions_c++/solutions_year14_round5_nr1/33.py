#undef NDEBUG
#ifdef SU2_PROJ
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
#include <ctime>
#include <cmath>
#include <cassert>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <utility>
#include <numeric>
#include <functional>

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

int n, p, q, r, s;

inline bool read()
{
	return scanf("%d%d%d%d%d", &n, &p, &q, &r, &s) == 5;
}

const int N = 1000 * 1000 + 13;

li sum[N];

inline li ssum(int lf, int rg)
{
	if (lf > rg) return 0;
	return sum[rg] - (lf == 0 ? 0 : sum[lf - 1]);
}

inline void solve(int test)
{
	printf("Case #%d: ", test + 1);	
	forn(i, n) sum[i] = (i * 1ll * p + q) % r + s;
	
	forl(i, n - 1) sum[i] += sum[i - 1];
	
	ld ans = 0;
	
	int p = 0;
	
	forn(i, n)
	{
		while (p + 1 < n)
		{
			li curmax = max(max(ssum(0, i - 1), ssum(i, p)), ssum(p + 1, n - 1));
			li nextmax = max(max(ssum(0, i - 1), ssum(i, p + 1)), ssum(p + 2, n - 1));
			
			if (nextmax < curmax)
				p++;
			else
				break;
		}
		
		ans = max(ans, 1.0 - ld(max(max(ssum(0, i - 1), ssum(i, p)), ssum(p + 1, n - 1))) / ld(ssum(0, n - 1)));
	}
		
	cout << ans << endl;
}

int main()
{
#ifdef SU2_PROJ
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif
    
    cout << setprecision(10) << fixed;
    cerr << setprecision(5) << fixed;
    
    int testCount;
    cin >> testCount;
    
    forn(test, testCount)
    {
	    assert(read());
    	solve(test);
    }
    
#ifdef SU2_PROJ
    cerr << "== TIME: " << clock() << " ==" << endl;
#endif

    return 0;
}
