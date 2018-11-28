/*
* @problem: Coin Jam
*/

#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <limits.h>
#include <vector>
#include <map>
#include <bitset>
#include <string>
#include <iterator>
#include <set>
#include <utility>
#include <queue>
#include <numeric>
#include <functional>
#include <ctype.h>
#include <stack>
#include <algorithm>
#include <cstdlib>
#define MAX 70000
#define mod 1000000007LL
#define bitcnt(x) __builtin_popcount(x)
#define MS0(x) memset(x, 0, sizeof(x))
#define MS1(x) memset(x, -1, sizeof(x))
#define ll long long int
#define pii pair<int, int>
#define pll pair<long long int,long long int>
#define in(x) scanf("%lld", &x)
#define ind(x) scanf("%d", &x)
#define ins(x) scanf("%s", x)
#define pi acos(-1.0)

using namespace std;
int n, m, bit[35];
vector<ll> v;

bool isprime(ll y)
{
	if(y % 2 == 0)
		return 0;
	for(ll i = 3, j = sqrt(y); i <= j; i += 2)
	{
		if(y % i == 0)
			return 0;
	}
	return 1;
}

bool check(ll x)
{
	if (isprime(x))
		return 0;
	for (int i = 0; i < n; i++)
	{
		if((x & (1 << i)))
			bit[i] = 1;
		else
			bit[i] = 0;
	}
	ll tmp, p;
	for (int i = 3; i <= 10; i++)
	{
		tmp = 0;
		p = 1;
		for (int j = 0; j < n; j++)
		{
			tmp += (p * bit[j]);
			p = p * i;
		}
		if (isprime(tmp))
			return 0;
	}
	return 1;
}

void solve(int i, int mask)
{
	if (i == n - 1)
	{
		if (check(mask))
		{
			v.push_back(mask);
			return;
		}
		return;
	}
	solve(i + 1, mask);
	if (v.size() < m)
		solve(i + 1, mask | (1 << i));
	return;
}

ll factor(ll x)
{
	if(x % 2 == 0)
		return 2;
	for(ll i = 3, j = sqrt(x); i <= j; i += 2)
	{
		if(x % i == 0)
			return i;
	}
	return x;
}

int main()
{
	// ios_base::sync_with_stdio(0);
	// cin.tie(0);
	int t;
	ll tmp;
	ind(t);
	for (int i = 1; i <= t; i++)
	{
		ind(n);
		ind(m);
		v.clear();
		printf("Case #%d:\n", i);
		solve(1, 1 | (1 << (n - 1)));
		for (int j = 0; j < m; j++)
		{
			tmp = v[j];
			for (int k = 0; k < n; k++)
			{
				if (tmp & (1 << k))
				{
					bit[k] = 1;
				}
				else
				{
					bit[k] = 0;
				}
			}
			for (int k = n - 1; k >= 0; k--)
			{
				printf("%d", bit[k]);
			}
			printf(" %lld ", factor(tmp));
			//printf(" %lld ", tmp);
			ll p;
			for (int k = 3; k <= 10; k++)
			{
				tmp = 0;
				p = 1;
				for (int a = 0; a < n; a++)
				{
					tmp += (p * bit[a]);
					p = p * k;
				}
				printf("%lld ", factor(tmp));
				//printf("%lld ", tmp);
			}
			printf("\n");
		}
	}
	return 0;
}