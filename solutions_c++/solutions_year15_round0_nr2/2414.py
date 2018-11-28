#pragma comment(linker, "/stack:128000000")

#include <algorithm>
#include <iostream>
#include <cassert>
#include <iomanip>
#include <climits>
#include <utility>
#include <cstring>
#include <complex>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <bitset>
#include <string>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <set>
#include <map>

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define forl(i, n) for (int i = 1; i <= int(n); i++)
#define fore(i, l, r) for (int i = int(l); i <= int(r); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(a, b) make_pair((a), (b))
#define x first
#define y second
#define ft first
#define sc second

using namespace std;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = INT_MAX / 2;
const ld EPS = 1e-9;
const ld PI = 3.1415926535897932384626433832795;

const int N = 1000 + 3;

int n;
int a[N];

inline bool read()
{
	if (scanf("%d", &n) != 1)
		return false;

	forn(i, n)
		assert(scanf("%d", &a[i]) == 1);

    return true;
}

int z[N][N];

inline int solve(int from, int to)
{
	int& ans = z[from][to];

	if (ans != -1)
		return ans;

	if (from <= to)
		return ans = 0;

	ans = INF;

	int rg = from >> 1;
	fore(a, 1, rg)
	{
		int b = from - a;
		ans = min(ans, 1 + solve(a, to) + solve(b, to));
	}

	return ans;
}

inline void precalc()
{
	memset(z, -1, sizeof(z));

	forn(i, N)
		fore(j, 0, i)
			solve(i, j);

	forn(i, N)
	{
		int minv = INF;
		fore(j, 0, i)
		{
			minv = min(minv, z[i][j]);
			z[i][j] = minv;
		}
	}
}

inline void solve(int test)
{
	sort(a, a + n);

	printf("Case #%d: ", test + 1);
	
	int maxv = 0;
	forn(i, n)
		maxv = max(maxv, a[i]);

	int ans = INF;

	fore(last, 1, maxv)
	{
		int cur = last;
		
		ford(i, n)
			if (a[i] > last)
				cur += z[ a[i] ][last]; //solve(a[i], last);
			else
				break;

		ans = min(ans, cur);
	}

	cout << ans << endl;
}

int main()
{
#ifdef HP
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif

	precalc();

	int testCnt;
	assert(scanf("%d", &testCnt) == 1);

	forn(test, testCnt)
	{
	    assert(read());
    	solve(test);
	}

    return 0;
}

