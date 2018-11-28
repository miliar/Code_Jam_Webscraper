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

const int nmax = 2005;
const lint MOD = 1000002013LL;

lint n, m;
vector < lint > X;
lint lx[nmax], rx[nmax], cnt[nmax];
lint sum[nmax];
set < pair < lint , int > > q;

lint getFun(lint lx, lint rx, lint cnt)
{
	lint len = rx - lx;
	return (n + (n - len + 1)) * len / 2 % MOD * cnt % MOD;
}

int getX(lint x) { return lower_bound(all(X), x) - X.begin(); }

void getSegm(int pos, int &l, int &r, lint &newVal)
{
	l = r = pos;
	while (l > 0 && sum[l - 1] == sum[pos]) l--;
	while (r < sz(X) - 1 && sum[r + 1] == sum[pos]) r ++;
	lint lVal = (l == 0) ? 0 : sum[l - 1];
	lint rVal = (r == sz(X) - 1) ? 0 : sum[r + 1];
	newVal = max(lVal, rVal);
}

void upd(int pos, lint val)
{
	q.erase(mp(-sum[pos],pos));
	sum[pos] = val;
	q.insert(mp(-sum[pos],pos));
}

bool solve()
{
	scanf("%lld%lld",&n,&m);
	X.clear();
	X.pb(1);
	X.pb(n);
	lint ans = 0;
	for (int i = 0; i < m; i ++)
	{
		scanf("%lld%lld%lld",&lx[i],&rx[i],&cnt[i]);
		ans = (ans + getFun(lx[i], rx[i], cnt[i])) % MOD;
		X.pb(lx[i]);
		X.pb(rx[i]);
	}
	sort(all(X));
	X.erase(unique(all(X)),X.end());
	_(sum, 0);
	for (int i = 0; i < m; i ++)
	{
		lx[i] = getX(lx[i]);
		rx[i] = getX(rx[i]);
		for (int j = lx[i]; j < rx[i]; j ++)
			sum[j] += cnt[i];
	}
	q.clear();
	for (int i = 0; i < sz(X) - 1; i ++)
	{
		q.insert(mp(-sum[i], i));
	}
	while (1)
	{
		int pos = q.begin()->second;
		lint val = -q.begin()->first;
		if (val == 0) break;
		int l, r;
		lint newVal;
		getSegm(pos, l, r, newVal);
		ans = (ans - getFun(X[l], X[r + 1], val - newVal) + MOD) % MOD;
		for (int i = l; i <= r; i ++)
			upd(i, newVal);
	}
	printf("%lld\n", ans);
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
