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

const int nmax = 1000005;

int n;
int dist[nmax];
queue < int > q;

int rev(int x)
{
	char s[20];
	sprintf(s, "%d", x);
	reverse(s, s + strlen(s));
	sscanf(s, "%d", &x);
	return x;
}

void upd(int x, int val)
{
	if (x < nmax && dist[x] == -1)
	{
		dist[x] = val;
		q.push(x);
	}
}

void precalc()
{
	_(dist, -1);
	upd(1, 1);
	while (!q.empty())
	{
		int x = q.front();
		q.pop();

		if (x == 12)
		{
			int xx = -1;
		}

		upd(x + 1, dist[x] + 1);
		upd(rev(x), dist[x] + 1);
	}
}

void read()
{
	scanf("%d", &n);
}

bool solve()
{
	printf("%d\n", dist[n]);
	return false;
}

int main()
{
	prepare();

	precalc();

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
