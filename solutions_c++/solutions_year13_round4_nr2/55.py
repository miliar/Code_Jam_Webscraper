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

int n;
li p;

inline bool read()
{
	return cin >> n >> p;
}

inline bool two(li x) { return (x & (x - 1)) == 0; }

bool check2(li le, li gr, li p)
{
	//cerr << le << ' ' << gr << ' ' << p << endl;
	
	if (p <= 0) return false;
	if (gr < p) return true;
	
	assert(two(le + gr + 1));
	li v = (le + gr + 1) >> 1;
	
	if (le > 0)
	{
		li nle = (le - 1) >> 1;
		li ngr = (gr + 1) >> 1;
		return check2(nle, ngr, p);
	}
	
	li nle = le;
	li ngr = ((gr + 1) >> 1) - 1;
	return check2(nle, ngr, p - v);
}

bool check1(li le, li gr, li p)
{
	if (p <= 0) return false;
	if (gr == 0) return true;
	
	assert(two(le + gr + 1));
	li v = (le + gr + 1) >> 1;
	
	if (gr > 0)
	{
		li nle = (le + 1) >> 1;
		li ngr = (gr - 1) >> 1;
		return check1(nle, ngr, p - v);
	}
	
	li nle = (le + 1) >> 1;
	li ngr = gr;
	return check1(nle, ngr, p);
}

inline void solve(int test)
{
	printf("Case #%d: ", test + 1);
	
	//forn(i, 1 << n) cerr << check2((1ll << n) - i - 1, i, p) << endl;
	//exit(0);
	
	li lf = 0, rg = (1ll << n) - 1;
	
	while (lf != rg)
	{
		li mid = (lf + rg + 1) >> 1;
		
		if (check1((1ll << n) - mid - 1, mid, p)) lf = mid;
		else rg = mid - 1;
	}
	
	printf("%I64d ", lf);
	
	lf = 0, rg = (1ll << n) - 1;
	
	while (lf != rg)
	{
		li mid = (lf + rg + 1) >> 1;
		
		if (check2((1ll << n) - mid - 1, mid, p)) lf = mid;
		else rg = mid - 1;
	}
	
	printf("%I64d\n", lf);
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
	
    return 0;
}
