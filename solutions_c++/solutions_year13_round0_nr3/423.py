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

const lint nmax = 100000000000000LL;

vector < lint > q;

bool isPalindrome(lint x)
{
	string s, t;
	while (x)
	{
		s.pb('0' + x % 10);
		x /= 10;
	}
	t = s;
	reverse(all(t));
	return s == t;
}

void precalc()
{
	for (lint i = 1; i * i <= nmax; i ++)
	{
		if (isPalindrome(i) && isPalindrome(i*i))
		{
			q.pb(i*i);
		}
	}
}

bool solve()
{
	lint l, r;
	scanf("%lld%lld",&l,&r);
	printf("%d\n", upper_bound(all(q), r) - lower_bound(all(q), l));
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
		cerr << i << endl;
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}
