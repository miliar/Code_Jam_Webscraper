//#pragma warning(disable:4996)
#include <iostream>
#include <functional>
#include <algorithm>
#include <cstring>
#include <vector>
#include <string>
#include <cstdio>
#include <cmath>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
using namespace std;
typedef long long ll;

#define INF 0x333f3f3f
#define repp(i, n, m) for (int i = n; i <= m; i++)
#define rep(i, n, m) for (int i = n; i < m; i++)
#define sa(n) scanf("%d", &(n))

const ll mod = 100000007;
const int maxn = 5e5 + 5;
const double PI = acos(-1.0);

set<int>s;

ll cal(int x)
{
	s.clear();
	ll i;
	for (i = 1;; i++)
	{
		ll r = i*x;
		ll res = r;
		while (r)
		{
			s.insert(r % 10);
			r /= 10;
		}
		if (s.size() == 10)
		{
			return res;
		}
	}
}

void test()
{
	int i, j;
	for (i = 1; i <= 10000; i++)
	{
		cal(i);
	}
}

ll n;

void solve()
{
	ll i, j, k;
	scanf("%lld", &n);
	if (n == 0)
	{
		puts("INSOMNIA");
	}
	else
	{
		printf("%lld\n", cal(n));
	}
}

int main()
{
/*	
#ifndef ONLINE_JUDGE  
	freopen("i.txt", "r", stdin);
	freopen("o.txt", "w", stdout);
#endif
*/
	//test();
	
	int i, t;
	scanf("%d", &t);
	for (i = 1; i <= t; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}
	
	return 0;
}