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

const int N = 100 + 3;

int n, m;
string s[N];
char buf[N];

inline bool read()
{
	if (scanf("%d%d", &n, &m) != 2)
		return false;

	forn(i, n)
	{
		assert(scanf("%s", buf) == 1);
		s[i] = string(buf);
	}

    return true;
}

int dx[] = { -1, 0, 1, 0 };
int dy[] = { 0, 1, 0, -1 };
string op = "^>v<";

inline bool checkOk(int x, int y)
{
	if (s[x][y] == '.')
		return true;

	forn(i, 4)
	{
		bool was = false;

		int xx = x, yy = y;
		while(true)
		{
			xx += dx[i];
			yy += dy[i];

			if (!correct(xx, yy, n, m))
				break;

			if (s[xx][yy] != '.')
			{
				was = true;
				break;
			}
		}

		if (was)
			return true;
	}

	return false;
}

inline int getDir(int x, int y)
{
	int idx = op.find(s[x][y]);
	assert(idx != -1);
	return idx;
}

inline int out(int x, int y)
{
	if (s[x][y] == '.')
		return 0;

	int dir = getDir(x, y);

	while(true)
	{
		x += dx[dir];
		y += dy[dir];

		if (!correct(x, y, n, m))
			return 1;

		if (s[x][y] != '.')
			return 0;
	}

	throw;
}

inline void solve(int test)
{
	printf("Case #%d: ", test + 1);

	bool ok = true;

	forn(i, n)
		forn(j, m)
			ok &= checkOk(i, j);

	if (!ok)
	{
		puts("IMPOSSIBLE");
		return;
	}

	int ans = 0;

	forn(i, n)
		forn(j, m)
			ans += out(i, j);

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

