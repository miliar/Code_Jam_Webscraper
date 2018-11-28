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

const int N = 6;

int n, m;
int a[N][N];

inline bool read()
{
	if (scanf("%d%d", &n, &m) != 2)
		return false;

    return true;
}

int ans;

int dx[] = { -1, 0, 1, 0 };
int dy[] = { 0, -1, 0, 1 };

inline bool check(int x, int y)
{
	int val = a[x][y];
	assert(x >= 0 && y >= 0 && x < n && y < m);

	int cnt = 0;

	forn(i, 4)
	{
		int nx = x + dx[i];

		if (nx < 0 || nx >= n)
			continue;

		int ny = y + dy[i];
		if (ny < 0)
			ny += m;
		if (ny >= m)
			ny -= m;

		cnt += (a[nx][ny] == val);

		if (cnt > val)
			break;
	}

	return cnt == val;
}

inline bool checkCol(int y)
{
	int cmp = 0;
	forn(x, n)
	{
		if (a[x][0] < a[x][y])
			cmp = -1;
		else
		if (a[x][0] > a[x][y])
			cmp = 1;

		if (cmp != 0)
			break;
	}

	return cmp <= 0;
}

vector < vector< vector<int> > > ANS;

inline void solve(int x, int y)
{
	if (y == m)
	{
		forn(x, n)
			if (!check(x, 0) || !check(x, m - 1))
				return;

		/*forn(i, n)
		{
			forn(j, m)
				cerr << a[i][j];
			cerr << endl;
		}
		cerr << endl;*/

		vector< vector<int> > cur;
		forn(x, n)
		{
			vector<int> row;
			row.reserve(m);
			forn(y, m)
				row.pb(a[x][y]);
			cur.pb(row);
		}

		ANS.pb(cur);

		ans++;

		return;
	}

	int nx = x + 1, ny = y;
	if (nx == n)
		ny++, nx = 0;

	fore(v, 1, 4)
	{
		a[x][y] = v;

		if (y >= 2 && !check(x, y - 1))
			continue;

		if (x == n - 1 && y >= 1 && !checkCol(y))
			continue;

		solve(nx, ny);
	}
}

const int M = 1000 + 3;

int used[M];

inline bool eq(const vector< vector<int> >& a, const vector< vector<int> >& b)
{
	forn(sh, m)
	{
		vector< vector<int> > aa;

		forn(x, n)
		{
			vector<int> row;
			row.reserve(m);

			forn(y, m)
			{
				int yy = (y + sh) % m;
				row.pb(a[x][yy]);
			}

			aa.pb(row);
		}

		if (aa == b)
			return true;
	}

	return false;
}

inline int getAns()
{
	memset(used, 0, sizeof(used));
	assert(M >= sz(ANS));

	int val = 0;

	forn(i, sz(ANS))
	{
		if (used[i])
			continue;

		val++;

		fore(j, i + 1, sz(ANS) - 1)
			if (eq(ANS[i], ANS[j]))
				used[j] = true;
	}

	return val;
}

inline void solve(int test)
{
	printf("Case #%d: ", test + 1);
	cerr << test << " " << n << " " << m << endl;

	ANS.clear();
	ans = 0;
	solve(0, 0);

	//ans = sz(ANS);
	ans = getAns();

	cout << ans << endl;
}

int main()
{
#ifdef HP
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif

	int testCnt;
	assert(cin >> testCnt);

	forn(test, testCnt)
	{
    	assert(read());
    	solve(test);
	}

    return 0;
}

