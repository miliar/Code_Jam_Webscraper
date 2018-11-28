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
#define eprintf(...) fprintf(stderr, __VA_ARGS__)

using namespace std;

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9, PI = 3.1415926535897932384626433832795;

int n, mask;

inline bool read()
{
	string s;
	assert(cin >> s);
	
	n = sz(s);
	mask = 0;
	forn(i, n) if (s[i] == 'X') mask |= (1 << i);
	
    return true;
}

ld z[(1 << 20) + 3];

ld solve(int mask)
{
	ld& ans = z[mask];
	
	if (ans > -0.5) return ans;
	if (mask == (1 << n) - 1) return ans = 0;
	
	ans = 0;
	
	forn(i, n)
	{
		int j = i, c = n;
		while (mask & (1 << j))
		{
			c--;
			(++j == n) && (j = 0);
		}
		ans += c + solve(mask | (1 << j));
	}
	
	ans /= n;
	return ans;
}

inline void _solve(int test)
{
	printf("Case #%d: ", test + 1);
	
	forn(i, (1 << n)) z[i] = -1;
	cout << solve(mask) << endl;
}

int main()
{
#ifdef SU2_PROJ
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif
    
    cout << setprecision(20) << fixed;
    cerr << setprecision(5) << fixed;
    
    int testCount;
    cin >> testCount;
    
    forn(test, testCount)
    {
        assert(read());
        _solve(test);
		cerr << test + 1 << endl;
    }
    
    return 0;
}
