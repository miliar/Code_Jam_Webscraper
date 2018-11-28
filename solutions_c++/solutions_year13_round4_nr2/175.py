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

lint n, total, P;

lint bst(lint id)
{
	lint lft = total - id;
	lint pos = 0, add = (1LL << n);
	while (lft > 1)
	{
		add >>= 1LL;
		lft >>= 1LL;
		pos += add;
	}
	return total - pos;
}

lint low(lint id)
{
	lint lft = id + 1;
	lint pos = 0, add = (1LL << n);
	int k = n;
	while (lft > 1)
	{
		k--;
		add >>= 1LL;
		lft >>= 1LL;
	}
	for (int i = 0; i < k; i ++)
	{
		add >>= 1LL;
		pos += add;
	}
	return total - pos;
}

lint get1()
{
	if (low(total - 1) <= P)
		return total - 1;
	lint l = 0, r = total - 1, mid;
	while (r - l > 1)
	{
		mid = (l + r) >> 1LL;
		if (low(mid) <= P)
			l = mid;
		else
			r = mid;
	}
	return l;
}

lint get2()
{
	if (bst(total - 1) <= P)
		return total - 1;
	lint l = 0, r = total - 1, mid;
	while (r - l > 1)
	{
		mid = (l + r) >> 1LL;
		if (bst(mid) <= P)
			l = mid;
		else
			r = mid;
	}
	return l;
}

bool solve()
{
	cin >> n >> P;
	total = (1LL << n);
	cout << get1() << " " << get2() << endl;
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
