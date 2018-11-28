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

const int nmax = 1005;

double a[nmax], b[nmax];
int n;

bool check(int lose)
{
	for (int i = 0; i < lose; i ++)
	{
		if (a[i] > b[n - lose + i])
			return false;
	}
	for (int i = lose; i < n; i ++)
	{
		if (a[i] < b[i - lose])
			return false;
	}
	return true;
}

int war2()
{
	sort(a, a + n);
	sort(b, b + n);

	for (int lose = 0; lose < n; lose ++)
	{
		if (check(lose))
		{
			return n - lose;
		}
	}
	return 0;
}

int war()
{
	sort(a, a + n);
	sort(b, b + n);
	bool used[nmax];

	_(used, 0);
	int ret = 0;
	for (int i = n - 1; i >= 0; i --)
	{
		bool ok = true;
		for (int j = 0; j < n; j ++)
		{
			if (b[j] > a[i] && !used[j])
			{
				ok = false;
				used[j] = true;
				break;
			}
		}

		if (ok)
		{
			for (int j = 0; j < n; j ++)
			{
				if (!used[j])
				{
					ret++;
					used[j] = true;
					break;
				}
			}
		}
	}
	return ret;
}

bool solve()
{
	scanf("%d",&n);
	for (int i = 0; i < n; i ++)
		scanf("%lf",&a[i]);
	for (int i = 0; i < n; i ++)
		scanf("%lf",&b[i]);
	printf("%d ", war2());
	printf("%d\n", war());

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
