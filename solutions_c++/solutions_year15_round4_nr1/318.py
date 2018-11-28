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
char s[N][N];

inline bool read()
{
	if (scanf ("%d%d", &n, &m) != 2)
		return false;

	forn (i, n)
		assert(scanf ("%s", s[i]) == 1);

	return true;
}

const int dx[4] = {0, 1, 0, -1};
const int dy[4] = {1, 0, -1, 0};
const char dc[4] = {'>', 'v', '<', '^'};

inline bool valid (int x, int y)
{
	return x >= 0 && y >= 0 && x < n && y < m;
}

inline bool correct (int x, int y, int k)
{
	x += dx[k], y += dy[k];

	while (valid(x, y) && s[x][y] == '.')
	{
		x += dx[k], y += dy[k];
	}

	return valid(x, y);
}

inline void solve(int test)
{
	printf ("Case #%d: ", test + 1);

	int ans = 0;
	forn (i, n)
		forn (j, m)
		{
			if (s[i][j] == '.')
				continue;

			int id = -1;
			forn (k, 4)
				if (dc[k] == s[i][j])
				{
					id = k;
					break;
				}

			assert(id != -1);

			if (correct(i, j, id))
				continue;

			bool f = 0;

			forn (k, 4)
				if (k != id && correct(i, j, k))
				{
					f = 1;
					break;
				}

			if (!f)
			{
				puts("IMPOSSIBLE");
				return;
			}

			ans++;
		}

	cout << ans << endl;
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
