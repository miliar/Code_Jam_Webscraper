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

const int N = 100 + 13;
int n, m;
char g[N][N], b[N];

inline bool read()
{
	if (scanf ("%d%d", &n, &m) != 2)
		return false;
		
	forn (i, n)
		assert(scanf ("%s", g[i]) == 1);
		
	assert(scanf ("%s", b) == 1);

	return true;
}

inline void solve(int test)
{
	printf ("Case #%d: ", test + 1);
	
	forn (i, n)
	{
		bool ok = 1;
		forn (j, m)
			if (g[i][j] != '1')
			{
				ok = 0;
				break;
			}
			
		if (ok)
		{
			puts("IMPOSSIBLE");
			return;
		}
	}
	
	if (m == 1)
	{
		puts ("? 0");
		return;	
	}	
	
	forn (i, m - 1)
		putchar('?');
	putchar(' ');
	putchar('1');
	putchar('0');
	putchar('?');

	forn (i, 55)
	{
		putchar('1');		
		putchar('0');		
	}
	
	puts("");
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
