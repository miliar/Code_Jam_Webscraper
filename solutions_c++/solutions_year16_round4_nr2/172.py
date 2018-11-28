#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <ctime>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <list>
#include <stack>
#include <bitset>
#include <algorithm>
#include <iomanip>

using namespace std;

#define forn(i,n) for (int i = 0; i < int(n); i++)
#define ford(i,n) for (int i = int(n) - 1; i >= 0; i--)
#define fore(i,l,r) for (int i = int(l); i <= int(r); i++)
#define all(a) a.begin(), a.end()
#define sz(a) int(a.size())
#define mp make_pair
#define pb push_back
#define ft first
#define sc second
#define x first
#define y second

template<typename X> inline X abs(const X& a) { return a < 0 ? -a : a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9;
const ld PI = acosl(ld(-1));

const int N = 200 + 13;
int n, k;
ld p[N];

inline bool read()
{
	if (scanf ("%d%d", &n, &k) != 2)
		return false;
		
	forn (i, n)
	{
		double val;
		assert(scanf ("%lf", &val) == 1);
		
		p[i] = ld(val);
	}

	return true;
}

ld b[N];
ld d[N][N];

inline ld calc ()
{
	forn (i, k + 1)
		forn (it, k + 1)
			d[i][it] = 0;
				
	d[0][0] = 1;
	forn (i, k)
 		forn (cntY, i + 1)
 		{
 			ld dv = d[i][cntY];
 			
 			d[i + 1][cntY + 1] += dv * b[i];
 			d[i + 1][cntY] += dv * (ld(1) - b[i]);
 		}
			
	return d[k][k / 2];
}

inline void solve(int test)
{
	printf ("Case #%d: ", test + 1);

	sort(p, p + n);
	
	ld ans = 0;
	
	forn (cnt0, k + 1)
	{
		int sz = 0;
     	forn (i, cnt0)
     		b[sz++] = p[i];
     	forn (i, k - cnt0)
     		b[sz++] = p[n - 1 - i];
     		
     	ans = max(ans, calc());
    }
	
    printf ("%.15f\n", double(ans));
}

int main()
{
#ifdef SU2_PROJ
	assert(freopen("input.txt", "r", stdin));
	assert(freopen("output.txt", "w", stdout));
#endif

	cout << setprecision(25) << fixed;
	cerr << setprecision(10) << fixed;

	srand(int(time(NULL)));
	
	int testCnt;
	assert(scanf ("%d", &testCnt) == 1);

	forn (test, testCnt)
	{
		assert(read());
		solve(test);
	}

#ifdef SU2_PROJ
	cerr << "TIME: " << clock() << endl;
#endif

	return 0;
}
