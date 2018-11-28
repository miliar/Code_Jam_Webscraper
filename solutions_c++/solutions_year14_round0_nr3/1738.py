#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <vector>
#include <memory.h>
#include <map>
#include <set>
#include <bitset>
#include <algorithm>
#include <cmath>
#include <stack>
#include <string>
#include <cstring>
#include <string.h>
#include <sstream>
#include <cmath>
#include <math.h>
#include <queue>
#include <deque>
#include <cassert>
#include <time.h>

#define forn(i,n) for (int i = 0; i < (int)n; i++)
#define fornd(i, n) for (int i = (int)n - 1; i >= 0; i--)
#define forab(i,a,b) for (int i = (int)a; i <= (int)b; i++)
#define forabd(i, b, a) for (int i = (int)(b); i >= (int)(a); i--)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define zero(a) memset (a, 0, sizeof (a))
#define last(v) (int)v.size() - 1
#define _(a, val) memset (a, val, sizeof (a))
#define sz(a) (int)(a).size()
#define pb push_back
#define mp make_pair
#define all(v) (v).begin(), (v).end()

#ifdef _DEBUG
#define dbg(...) {fprintf(stderr, __VA_ARGS__); fflush(stderr);}
#define dbgx(x) {cerr << #x << " = " << x << endl;}
#define dbgv(v) {cerr << #v << " = {"; for (typeof(v.begin()) it = v.begin(); it != v.end(); it ++) cerr << *it << ", "; cerr << "}"; cerr << endl;}
#else
#define dbg(...) { }
#define dbgx(x) { }
#define dbgv(v) { }
#endif

typedef long long lint;
typedef unsigned long long ull;
typedef long double ld;

const lint LINF = 1000000000000000000LL;
const int INF = 1000000000;
const long double eps = 1e-9;
const long double PI = 3.1415926535897932384626433832795l;

using namespace std;

void prepare (string s)
{
#ifdef _DEBUG
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);
#else
	if (s.length() != 0)
	{
		freopen ((s + ".in").c_str(), "r", stdin);
		freopen ((s + ".out").c_str(), "w", stdout);
	}
#endif
}


const int NMAX = 55;
vector<int> g[NMAX];
char a[NMAX][NMAX];
int n, m, k;

void read()
{
	scanf("%d %d %d", &n, &m, &k);
}

int bit(int msk, int i)
{
	return (msk >> i) & 1;
}

int cnt_bit(int msk)
{
	int r = 0;
	forn(i, 30)
		if (bit(msk, i))
			r ++;
	return r;
}

void print()
{
	forn(i, n)
	{
		forn(j, m)
			printf("%c", a[i][j]);
		printf("\n");
	}
}

bool ok(int nx, int ny)
{
	return 0 <= nx && nx < n && 0 <= ny && ny < m;
}

int dx[] = {-1, -1, -1, 0, 0, 1, 1, 1};
int dy[] = {-1, 0, 1, -1, 1, -1, 0, 1};

int count_stars(int x, int y)
{
	int r = 0;
	forn(i, 8)
	{
		int nx, ny;
		nx = x + dx[i];
		ny = y + dy[i];
		if (ok(nx, ny) && a[nx][ny] == '*')
			r ++;
	}	
	return r + ((a[x][y] == '*')? 1 : 0);
}

bool go(int msk, int pos)
{
	int d[NMAX][NMAX];
	_(d, -1);
	forn(i, n) forn(j, m) a[i][j] = '.';
	int x, y;
	forn(i, n*m)
	{
		if (bit(msk, i))
		{
			x = i / m;
			y = i % m;
			a[x][y] = '*';
		}
	}
	
	x = pos / m;
	y = pos % m;
	a[x][y] = 'c';
	d[x][y] = count_stars(x, y);
	queue<int> q;
	q.push(pos);
	while(!q.empty())
	{
		x = q.front() / m;
		y = q.front() % m;
		q.pop();
		forn(i, 8)
		{
			int nx, ny;
			nx = x + dx[i];
			ny = y + dy[i];
			if (ok(nx, ny) && d[x][y] == 0)
			{
				if (d[nx][ny] == -1 && count_stars(nx, ny) == 0)
					q.push(nx*m + ny);
				d[nx][ny] = count_stars(nx, ny);
			}
		}
	}
	
	forn(i, n*m)
		if (!bit(msk, i))
			if (d[i / m][i % m] == -1)
				return false;
	return true;
}

void solve()
{
	int area = n*m;
	forn(id, sz(g[k]))
	{
		int msk = g[k][id];
		if (msk >= (1 << area)) continue;
		assert( cnt_bit(msk) == k );
		forn(pos, area)
		{
			if (!bit(msk, pos))
			{
				if (go( msk, pos ))
				{
					print();
					return;
				}
			}
		}
	}
	printf("Impossible\n");
}

int main ()
{
	prepare ("");

	forn(i, 1 << 25)
		g[cnt_bit(i)].pb ( i );
	
	int t;
	scanf("%d", &t);
	forn(i, t)
	{
		printf("Case #%d:\n", i + 1);
		read();
		solve();
	}

	return 0;
}
