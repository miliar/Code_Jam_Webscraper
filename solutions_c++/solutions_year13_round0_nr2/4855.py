#pragma comment(linker, "/stack:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES

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
#include <cmath>
#include <ctime>
#include <set>
#include <map>

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define forl(i, n) for (int i = 1; i <= int(n); i++)
#define for1(i, n) for (int i = 1; i <= int(n); i++)
#define forn1(i, n) for (int i = 1; i <= int(n); i++)
#define fore(i, l, r) for (int i = int(l); i <= int(r); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define debug(x) cerr << #x << " = " << x << endl;
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(a, b) make_pair((a), (b))
#define X first
#define Y second
#define fs first
#define ft first
#define sc second

using namespace std;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;
typedef pair<ld, ld> ptd;
typedef unsigned char byte;
typedef vector<vector<int> > matrix;

const int INF = INT_MAX / 2;
const ld EPS = 1e-9;
const ld PI = 3.1415926535897932384626433832795;

const int N = 100 + 3;

int n, m;
int a[N][N];

inline bool read()
{
	if (scanf("%d%d", &n, &m) != 2)
		return false;

	forn(i, n)
		forn(j, m)
			assert(scanf("%d", &a[i][j]) == 1);

	return true;
}

int b[N][N];

int used[N][N];

int sz = 0;
pair<int, pt> z[N * N];

inline bool checkRow(int x, int y, int val)
{
	fore(yy, 0, m - 1)
		if (used[x][yy] && b[x][yy] > val)
			return false;

	return true;
}

inline void paintRow(int x, int y, int val)
{
	fore(yy, 0, m - 1)
		b[x][yy] = val;
}

inline bool checkCol(int x, int y, int val)
{
	fore(xx, 0, n - 1)
		if (used[xx][y] && b[xx][y] > val)
			return false;

	return true;
}

inline void paintCol(int x, int y, int val)
{
	fore(xx, 0, n - 1)
		b[xx][y] = val;
}

inline void solve(int test)
{
	printf("Case #%d: ", test + 1);

	sz = 0;

	forn(i, n)
		forn(j, m)
		{
			z[sz++] = mp(a[i][j], mp(i, j));
			b[i][j] = INF;
			used[i][j] = false;
		}

	sort(z, z + sz);
	reverse(z, z + sz);

	bool ans = true;

	forn(it, sz)
	{
		int x = z[it].sc.ft;
		int y = z[it].sc.sc;

		if (b[x][y] == a[x][y])
		{
			used[x][y] = true;
			continue;
		}

		/*cerr << x << " " << y << " " << a[x][y] << endl;
		forn(i, n)
		{
			forn(j, m)
				cerr << b[i][j] << " ";
			cerr << endl;
		}*/

		if (checkRow(x, y, a[x][y])) 
			paintRow(x, y, a[x][y]);
		else
		if (checkCol(x, y, a[x][y]))
			paintCol(x, y, a[x][y]);
		else
			ans = false;

		if (!ans)
			break;

		used[x][y] = true;
	}

	puts(ans? "YES": "NO");
}

int main()
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int testCnt;

    assert(scanf("%d\n", &testCnt) == 1);

    forn(test, testCnt)
    {
    	assert(read());
		solve(test);
	}

    return 0;
}
