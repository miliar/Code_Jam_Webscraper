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

const int nmax = 4;

int a[2][nmax][nmax], row[2];
int cnt[20];

bool solve()
{
	_(cnt, 0);
	for (int it = 0; it < 2; it ++)
	{
		scanf("%d",&row[it]);
		row[it]--;
		for (int i = 0; i < 4; i ++)
		{
			for (int j = 0; j < 4; j ++)
			{
				scanf("%d",&a[it][i][j]);
				if (row[it] == i)
					cnt[a[it][i][j]]++;
			}
		}
	}
	int ans = 0;
	for (int i = 0; i < 20; i ++)
	{
		if (cnt[i] == 2)
		{
			if (ans > 0)
			{
				ans = -1;
				break;
			}
			ans = i;
		}
	}
	if (ans == -1)
		printf("Bad magician!\n");
	else
	if (ans == 0)
		printf("Volunteer cheated!\n");
	else
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
		solve();
	}
	return 0;
}
