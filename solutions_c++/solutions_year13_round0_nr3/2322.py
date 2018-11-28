#pragma comment(linker, "/STACK:500000000")
#include <algorithm>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <math.h>
#include <set>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <time.h>
#include <queue>
#include <utility>
#include <vector>
using namespace std;

#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x)*(x))
#define y0 y123
#define y1 y1234
#define ll long long
#define PI 3.1415926535897932384626433832795
#define EPS 1e-9
#define INF 2147483647
#define MOD 1000000007
#define N 105


int gcd(int a, int b) { return (!b) ? a : gcd(b, a % b); }
int lcm(int a, int b) { return a / gcd(a,b) * b; }

ll a[N], t, l, r, m = 0;
bool f(ll n)
{
	ll mask[N], len = 0;
	while(n)
	{
		mask[len++] = n % 10;
		n /= 10;
	}
	for(ll l = 0, r = len-1; l < r; l++, r--)
		if(mask[l] != mask[r])
			return 0;
	return 1;
}
/*ll binsearch(ll v)
{
	ll L = 0, R = m-1, res;
	while(L <= R)
	{
		ll M = (L+R) / 2;
		if(a[M] >= v)
			res = M, R = M-1;
		else
			L = M+1;
	}
	return res;
}*/
int main()
{
	for(ll n = 1; n <= 10000000; n++)
		if(f(n) && f(n*n))
			a[m++] = n*n;
	freopen("C-large-1.in", "r", stdin);
	freopen("C-large-1.out", "w", stdout);
	scanf("%lld", &t);
	for(ll tt = 1; tt <= t; tt++)
	{
		scanf("%lld %lld", &l, &r);
		ll res = 0;
		for(ll i = 0; i < m; i++)
			if(a[i] >= l && a[i] <= r)
				res++;
		printf("Case #%lld: %lld\n", tt, res);
	}
	return 0;
}