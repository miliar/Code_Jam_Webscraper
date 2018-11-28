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

const int N = 20 * 1000 + 3;
int n;
char s[N];

inline void gen()
{
	n = 20 * 1000;
	forn (i, n / 2)
	{
		if (i & 1)
			s[i] = s[n - i - 1] = 'C';
		else
			s[i] = s[n - i - 1] = 'J';
	}
}

inline bool read()
{
	//gen();
	//return true;
	
	if (scanf ("%s", s) != 1)
		return false;
		
	n = int(strlen(s));

	return true;
}

/*inline int get (char a, char b)
{
	if (a == b)
		return 10;
		
	return 5;
}

int d[N][N];

int calc (int l, int r)
{
	if (l > r)
		return 0;

	if (d[l][r] != -1)
		return d[l][r];
		
   	for (int i = l + 1; i <= r; i += 2)
    	d[l][r] = max(d[l][r], calc(l + 1, i - 1) + calc(i + 1, r) + get(s[l], s[i]));	
		
	return d[l][r];
}

#define next ___next*/

int dsu[N];

int getP(int v)
{
	if (dsu[v] == v)
		return v;
		
	return dsu[v] = getP(dsu[v]);
}

inline void solve(int test)
{
	printf ("Case #%d: ", test + 1);
	
	forn (i, n + 1)
		dsu[i] = i;
		
	int cnt = n;
	
	bool f = 1;
	while (f)
	{
		f = 0;
		
		int i = getP(0);
		while (i + 1 < n)
		{
			int ni = getP(i + 1);
			
			if (ni != n && s[i] == s[ni])
			{
				int val = getP(ni + 1);
				dsu[ni] = val;
				dsu[i] = val;
				
				f = 1;
				cnt -= 2;
			}
			
			i = getP(i + 1);
		}
	}
	
	printf ("%d\n", cnt / 2 * 5 + (n - cnt) * 5);
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
		cerr << test << endl;
		assert(read());
		solve(test);
	}

#ifdef SU2_PROJ
	cerr << "TIME: " << clock() << endl;
#endif

	return 0;
}
