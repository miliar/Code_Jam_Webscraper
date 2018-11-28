#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker,"/STACK:64000000")
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <memory.h>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <cassert>
#include <time.h>
#include <bitset>

using namespace std;

#define mp make_pair
#define pb push_back
#define _(a,b) memset( (a), b, sizeof( a ) )
#define all(a) a.begin(), a.end()
#define sz(a) (int)a.size()
#ifdef WIN32
#define dbg(...) {fprintf(stderr, __VA_ARGS__); fflush(stderr);}
#define dbgx(x) {cerr << #x << " = " << x << endl;}
#define dbgv(v) {cerr << #v << " = {"; for (typeof(v.begin()) it = v.begin(); it != v.end(); it ++) cerr << *it << ", "; cerr << "}"; cerr << endl;}
#else
#define dbg(...) { }
#define dbgx(x) { }
#define dbgv(v) { }
#endif

typedef unsigned long long ull;
typedef long long lint;
typedef pair < int , int > pii;
typedef long double ld;

const int INF = 1000 * 1000 * 1000;
const lint LINF = 1000000000000000000LL;
const double eps = 1e-9;

void prepare()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
}

const int nmax = 105;
int n, m;
int dx[] = { -1, 0, +1, 0 };
int dy[] = { 0, -1, 0, +1 };
string alpha = "^<v>";
char s[nmax][nmax];

int getDir(char c)
{
	return alpha.find(c);
}

void read()
{
	scanf("%d%d",&n,&m);
	for (int i = 0; i < n; i ++)
	{
		scanf("%s", s[i]);
	}
}

bool in(int x, int y)
{
	return 0 <= x && x < n && 0 <= y && y < m;
}

bool isBad(int x, int y)
{
	if (s[x][y] == '.') 
		return false;

	int dir = getDir(s[x][y]);
	for (int cx = x + dx[dir], cy = y + dy[dir]; ; cx += dx[dir], cy += dy[dir])
	{
		if (!in(cx,cy))
			return true;
		if (s[cx][cy] != '.')
			return false;
	}
}

bool noWay(int x, int y)
{
	assert(s[x][y] != '.');

	for (int i = 0; i < 4; i ++)
	{
		s[x][y] = alpha[i];
		if (!isBad(x, y))
			return false;
	}
	return true;
}

bool solve()
{
	int ans = 0;
	for (int i = 0; i < n; i ++)
	{
		for (int j = 0; j < m; j ++)
		{
			if (isBad(i,j))
			{
				if (noWay(i,j))
				{
					printf("IMPOSSIBLE\n");
					return false;
				}
				ans++;
			}
		}
	}
	printf("%d\n", ans);
	return false;
}

int main()
{
	prepare();
	int t;
	scanf("%d",&t);
	for (int i = 0; i < t; i ++)
	{
		dbg("Test %d\n", i);
		printf("Case #%d: ", i + 1);
		read();
		solve();
	}
	return 0;
}
