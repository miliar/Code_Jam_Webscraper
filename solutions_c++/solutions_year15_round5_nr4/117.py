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

const int N = 1000 * 1000 + 13;
int n, p;
pt a[N];

inline bool read()
{
	if (scanf ("%d", &p) != 1)
		return false;

	forn (i, p)
		assert(scanf ("%d", &a[i].ft) == 1);

	int cnt = 0;
	forn (i, p)
	{
		assert(scanf ("%d", &a[i].sc) == 1);

		cnt += a[i].sc;
	}

	n = 0;
	while ((1 << n) < cnt)
		n++;

	return true;
}

int ans[N], szans;
map<int, int> q;

inline void del (int v)
{
	assert(q.count(v));

	q[v]--;

	if (q[v] == 0)
		q.erase(v);
}

inline void solve(int test)
{
	printf ("Case #%d:", test + 1);

	szans = 0;
	q.clear();

	forn (i, p)
		q[ a[i].ft ] = a[i].sc;

	del(0);

	forn (i, n)
	{
		ans[i] = q.begin()->ft;
		del(ans[i]);

		for (int mask = 1; mask < (1 << i); mask++)
		{
			int sum = ans[i];
			forn (j, i)
				if ((mask >> j) & 1)
					sum += ans[j];

			del(sum);
		}
	}

	assert(q.empty());

	forn (i, n)
		printf (" %d", ans[i]);
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
