#include<stdlib.h>
#include<time.h>
#include<cmath>
#include<cstring>
#include<cstdio>
#include<set>
#include<queue>
#include<bitset>
#include<vector>
#include<iostream>
#include<algorithm>
using namespace std;
typedef long long LL;
typedef unsigned long long UL;
typedef vector<int> vi;
typedef pair<int, int> pii;
#define sz(x) ((int)(x.size()))
#define sqr(x) ((x)*(x))
#define pb push_back
#define mp make_pair
#define fi first
#define se second
const int N = 1e2 + 7;
const int M = 1e6 + 7;
const int INF = 2e5 + 7;
const int MOD = 1e9 + 7;
const LL LINF = 1e17 + 7;
const double Pi = acos(-1.);
const double EPS = 1e-8;
int n, m, a[N];
LL mul(LL a, LL b, LL mod) {
	LL res = 0;
	while (b) {
		if (b & 1)
			res = (res + a) % mod;
		a = (a + a) % mod;
		b = b >> 1;
	}
	return res;
}
LL exp(LL a, LL b, LL mod) {
	LL res = 1;
	while (b) {
		if (b & 1)
			res = mul(res, a, mod);
		a = mul(a, a, mod);
		b = b >> 1;
	}
	return res;
}
bool millerRabin(LL n) {
	if (n < 2)
		return false;
	if (n == 2)
		return true;
	bool flag;
	int count = 10;
	LL b, r, t, x;
	srand(time(NULL));
	while (count--) {
		flag = false;
		r = 0;
		b = n - 1;
		x = 2 + rand() % (n - 2);
		while (!(b & 1)) {
			++r;
			b = b >> 1;
		}
		t = exp(x, b, n);
		if (t == 1 || t == n - 1) {
			flag = true;
			continue;
		}
		for (int i = 1; i < r; ++i) {
			t = mul(t, t, n);
			if (t == 1)
				return false;
			if (t == n - 1) {
				flag = true;
				break;
			}
		}
		if (!flag) {
//			printf("x = %I64d, t = %I64d, ", x, exp(x, b, n));
			break;
		}
	}
	return flag;
}
LL fac(LL t) {
	for (int i = 2; i <= sqrt(0. + t); ++i)
		if (t % i == 0) {
			return i;
		}
	return 1;
}
LL ans[N];
void dfs(int t) {
	if (m <= 0)
		return;
	if (t < 0) {
		if (!(a[n - 1] == 1 && a[0] == 1))
			return;
		--m;
		for (int i = n - 1; i >= 0; --i)
			printf("%d", a[i]);
		for (int b = 2; b <= 10; ++b)
			printf(" %I64d", b + 1LL);
		puts("");
		return;
	}
	a[t] = a[t - 1] = 0;
	dfs(t - 2);
	a[t] = a[t - 1] = 1;
	dfs(t - 2);
}
int main() {
	freopen("C-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int T, tt = 0;
	scanf("%d", &T);
	while (T--) {
		scanf("%d%d", &n, &m);
		printf("Case #%d:\n", ++tt);
		dfs(n - 1);
	}
	return 0;
}
