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
int n;
ld v, x;
ld r[N], c[N];

inline void readDouble (ld& a)
{
	assert(cin >> a);
}

inline bool read()
{
	if (scanf ("%d", &n) != 1)
		return false;

	readDouble(v);
	readDouble(x);

	forn (i, n)
	{
		readDouble(r[i]);
		readDouble(c[i]);
	}

	return true;
}

inline void solve(int test)
{
	printf ("Case #%d: ", test + 1);

	if (n == 1)
	{
		if (abs(c[0] - x) < EPS)
		{
			ld ans = v / r[0];

			printf ("%.15f\n", double(ans));
		}
		else
		{
			puts("IMPOSSIBLE");
		}

		return;
	}

	if (abs(c[0] - c[1]) < EPS)
	{
		if (abs(c[0] - x) < EPS)
		{
			ld ans = v / (r[0] + r[1]);

			printf ("%.15f\n", double(ans));
		}
		else
		{
			puts("IMPOSSIBLE");
		}

		return;
	}

	ld v0 = v * (x - c[1]) / (c[0] - c[1]);
	ld v1 = v - v0;

	if (v0 < -EPS || v1 < -EPS)
	{
		puts("IMPOSSIBLE");
		return;
	}

	ld ans = max(v0 / r[0], v1 / r[1]);

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
