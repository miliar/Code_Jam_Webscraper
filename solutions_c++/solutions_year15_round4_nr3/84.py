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

bool bit(int msk, int i)
{
	return msk & (1 << i);
}

const int nmax = 22;
int n;
vector < int > x[nmax];
map < string, int > ID;
char buf[100005];

int getId(string s)
{
	if (ID.count(s))
		return ID[s];

	int id = sz(ID);
	ID[s] = id;
	return id;
}

void read()
{
	ID.clear();

	scanf("%d\n", &n);
	for (int i = 0; i < n; i ++)
	{
		gets(buf);
		stringstream ss(buf);
		string tmp;
		x[i].clear();
		while (ss >> tmp)
		{
			x[i].pb(getId(tmp));
		}
	}
}

int tt[2][2005], TIMER;

bool solve()
{
	int ans = INF;
	for (int msk = 0; msk < (1 << n); msk ++)
	{
		if (bit(msk, 0) || !bit(msk, 1))
			continue;

		TIMER++;
		for (int i = 0; i < n; i ++)
		{
			int fid = bit(msk, i);
			for (int j = 0; j < sz(x[i]); j ++)
			{
				tt[fid][x[i][j]] = TIMER;
			}
		}

		int cur = 0;
		for (int i = 0; i < sz(ID); i ++)
		{
			cur += tt[0][i] == tt[1][i];
		}
		ans = min(ans, cur);
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
