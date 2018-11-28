#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
using namespace std;

typedef long long ll;

ll muti_mod(ll a, ll b, ll n)
{
	ll exp = a % n, res = 0;
	while (b) {
		if (b & 1) {
			res += exp;
			if (res > n) res -= n;
		}
		exp <<= 1;
		if (exp > n) exp -= n;
		b >>= 1;
	}
	return res;
}
// ret = (a^b)%n
ll mod_exp(ll a, ll p, ll m)
{
	ll exp = a % m, res = 1; //
	while (p > 1) {
		if (p & 1) //
			res = muti_mod(res, exp, m);
		exp = muti_mod(exp, exp, m);
		p >>= 1;
	}
	return muti_mod(res, exp, m);
}
//miller-rabin 法测试素数, times 测试次数
bool miller_rabin(ll n, int times)
{
	if (n == 2)return 1;
	if (n < 2 || !(n & 1))return 0;
	ll a, u = n - 1, x, y;
	int t = 0;
	while (u % 2 == 0) {
		t++;
		u /= 2;
	}
	for (int i = 0; i < times; i++) {
		a = rand() % (n - 1) + 1;
		x = mod_exp(a, u, n);
		for (int j = 0; j < t; j++) {
			y = muti_mod(x, x, n);
			if ( y == 1 && x != 1 && x != n - 1 )
				return false; //must not
			x = y;
		}
		if ( y != 1) return false;
	}
	return true;
}

ll pollard_rho(ll n, int c) //找出一个因子
{	
	ll x, y, d, i = 1, k = 2;
	x = rand() % (n - 1) + 1;
	y = x;
	while (true) {
		i++;
		x = (muti_mod(x, x, n) + c) % n;
		d = __gcd(y - x, n);
		if (1 < d && d < n) return d;
		if ( y == x) return n;
		if (i == k) {
			y = x;
			k <<= 1;
		}
	}
}

ll a[11];
bool check(ll x, int n)
{
	for (ll base = 2; base <= 10; base++) {
		ll v = 0, tmp = 1;
		for (int i = 0; i < n; i++) {
			if ((x >> i) & 1)  v += tmp;
			tmp *= base;
		}
		if (!miller_rabin(v, 8)) {
			a[base] = pollard_rho(v, 107);
			while(a[base] == v) a[base] = pollard_rho(v, 107);
		} else {
			return false;
		}
	}
	return true;
}

void doit(int n, int m)
{
	ll t = (1ll << (n - 1)) + 1;
	for (ll i = 0; i < (1ll << (n - 2)); i++) {
		ll x = t + (i << 1);
		if (check(x, n)) {
			for (int i = n - 1; i >= 0; i--)  printf("%d", int((x >> i) & 1));
			for (int i = 2; i <= 10; i++) printf(" %lld", a[i]);
			puts("");
			if (--m == 0) return;
		}
	}
}

int main(int argc, char *argv[])
{

	if (argc == 2) {
		freopen(argv[1], "r", stdin);
	} else if (argc == 3) {
		freopen(argv[1], "r", stdin);
		freopen(argv[2], "w", stdout);
	}

	srand(time(NULL));

	int T, cas = 0;
	scanf("%d", &T);
	while (T--) {
		int n, m;
		scanf("%d%d", &n, &m);
		printf("Case #%d:\n", ++cas);
		doit(n, m);
	}
	return 0;
}