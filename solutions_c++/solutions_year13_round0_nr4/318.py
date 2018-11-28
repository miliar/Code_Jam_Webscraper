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
#ifdef _DEBUG
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

const int nmax = 20;

int need[nmax];
multiset < int > bonus[nmax];
bool used[1 << nmax];
vector < int > ans;
int n;

void init()
{
	_(used, 0);
	for (int i = 0; i < nmax; i ++)
		bonus[i].clear();
}

bool bit(int msk, int i)
{
	return msk & (1 << i);
}

multiset < int > merge(multiset < int > &a, multiset < int > &b)
{
	multiset<int> res = a;
	for (multiset<int>::iterator it = b.begin(); it != b.end(); it ++)
	{
		res.insert(*it);
	}
	return res;
}

bool dfs(int msk, multiset < int > q)
{
	if (used[msk]) return false;
	if (msk == ((1 << n) - 1)) return true;
	used[msk] = true;
	for (int i = 0; i < n; i ++)
	{
		if (!bit(msk, i) && q.find(need[i]) != q.end())
		{
			ans.pb(i);
			q.erase(q.find(need[i]));
			if (dfs(msk | (1 << i), merge(q, bonus[i])))
				return true;
			q.insert(need[i]);
			ans.pop_back();
		}
	}
	return false;
}

bool solve()
{
	init();
	int k, x;
	scanf("%d%d",&k,&n);
	multiset < int > start;
	for (int i = 0; i < k; i ++)
	{
		scanf("%d",&x);
		start.insert(x);
	}
	for (int i = 0; i < n; i ++)
	{
		scanf("%d%d",&need[i],&k);
		for (int j = 0; j < k; j ++)
		{
			scanf("%d",&x);
			bonus[i].insert(x);
		}
	}
	ans.clear();
	if (dfs(0, start))
	{
		for (int i = 0; i < sz(ans); i ++)
		{
			if (i) printf(" ");
			printf("%d", ans[i] + 1);
		}
	}
	else
		printf("IMPOSSIBLE");
	printf("\n");
	return false;
}

int main()
{
	prepare();
	int t;
	scanf("%d",&t);
	for (int i = 0; i < t; i ++)
	{
		cerr << i << endl;
		dbgx(i);
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}
