#include <iostream>
#include <fstream>
#include <cstdio>
#include <climits>
#include <vector>
#include <map>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <string>
#include <cstring>
#include <algorithm>
#include <bitset>
#include <cmath>
#include <functional>

using namespace std;

#define ll long long
#define vt vector
#define mod 1000000007

ll req, no;

ll factor(ll val)
{
	if (val % 2 == 0)
		return 2;
	else
	{
		for (ll i = 3; i*i <= val; i += 2)
			if (val % i == 0)
				return i;
		return val;
	}
}

ll conv_10(ll val)
{
	ll x = 0;
	ll powval = 0;
	for (ll i = 0; i < no; i++)
	{
		if ((val >> i) & 1)
			x += powl(10, powval);
		powval++;
	}
	return x;
}

bool check(ll val)
{
	ll ans[11] = { 0 };
	for (ll i = 2; i <= 10; i++)
	{
		ll x = 0;
		ll powval = 0;
		for (ll j = 0; j < no; j++)
		{
			if ((val >> j) & 1)
				x += powl(i, powval);
			powval++;
		}
		ll y = factor(x);
		if (y == x)
			return false;
		else
			ans[i] = y;
	}
	printf("%lld ", conv_10(val));
	for (ll i = 2; i <= 10; i++)
		printf("%lld ", ans[i]);
	printf("\n");
	return true;
}

void solve()
{
	for (ll i = 0; i < 1 << (no - 2); i++)
	{
		ll x = 1;
		for (ll j = 0; j < (no - 2); j++)
			if ((i >> j) & 1)
			{
				x <<= 1;
				x += 1;
			}
			else
				x <<= 1;
		x <<= 1;
		x += 1;
		if(check(x)) req--;
		if (req == 0)
			break;
	}
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	ll t;
	scanf("%lld", &t);
	for (ll cases = 1; cases <= t; cases++)
	{
		ll n, j;
		scanf("%lld %lld", &n, &j);
		no = n;
		req = j;
		printf("Case #%lld:\n", cases);
		solve();
	}
	return 0;
}