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

const int N = 6 + 3;
int n, m;

inline bool read()
{
	if (scanf ("%d%d", &n, &m) != 2)
		return false;

	return true;
}

int a[N][N];

const int dx[4] = {0, 1, 0, -1};
const int dy[4] = {1, 0, -1, 0};

inline bool valid (int x, int y)
{
	return x >= 0 && x < n;
}

vector<vector< vector<int> > > ans;

inline bool good (int x, int y)
{
	int cntF = 0, cntG = 0;

	forn (k, 4)
	{
		int nx = x + dx[k], ny = (y + dy[k] + m) % m;

		if (valid(nx, ny))
		{
			if (a[nx][ny] == -1)
				cntF++;
			if (a[nx][ny] == a[x][y])
				cntG++;
		}
	}

	if (cntG > a[x][y] || cntG + cntF < a[x][y])
		return false;

	return true;
}

void calc (int x, int y)
{
	if (y == m)
	{
		y = 0;
		x++;
	}

	if (x == n)
	{
//		forn (i, n)
//		{
//			forn (j, m)
//				cerr << a[i][j] << ' ';
//			cerr << endl;
//		}
//		cerr << endl;

		vector< vector<int> > cur;
		cur.resize(n);

		forn (i, n)
			forn (j, m)
				cur[i].pb(a[i][j]);

		ans.pb(cur);

		return;
	}

	for (int i = 1; i <= 4; i++)
	{
		int cntF = 0, cntG = 0;

		forn (k, 4)
		{
			int nx = x + dx[k], ny = (y + dy[k] + m) % m;

			if (valid(nx, ny))
			{
				if (a[nx][ny] == -1)
					cntF++;
				if (a[nx][ny] == i)
					cntG++;
			}
		}

		if (cntG > i || cntG + cntF < i)
			continue;

		a[x][y] = i;

		bool ok = 1;

		forn (k, 4)
		{
			int nx = x + dx[k], ny = (y + dy[k] + m) % m;

			if (!valid(nx, ny))
				continue;

			if (a[nx][ny] == -1)
				continue;

			if (!good(nx, ny))
			{
				ok = 0;
				break;
			}
		}

		if (!ok)
		{
			a[x][y] = -1;
			continue;
		}

		calc(x, y + 1);

		a[x][y] = -1;
	}
}

inline bool isSame (const vector< vector<int> >& a, const vector< vector<int> >& b)
{
	forn (sh, m)
	{
		bool ok = 1;
		forn (i, n)
		{
			forn (j, m)
				if (a[i][j] != b[i][ (j + sh) % m ])
				{
					ok = 0;
					break;
				}

			if (!ok)
				break;
		}

		if (ok)
			return true;
	}

	return false;
}

inline void solve(int test)
{
	printf ("Case #%d: ", test + 1);

	memset(a, -1, sizeof a);

	ans.clear();

	calc(0, 0);

	forn (i, sz(ans))
		fore(j, i + 1, sz(ans) - 1)
		{
			if (isSame(ans[i], ans[j]))
			{
				swap(ans[i], ans.back());
				ans.pop_back();

				i--;
				break;
			}
		}

	cout << sz(ans) << endl;
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
