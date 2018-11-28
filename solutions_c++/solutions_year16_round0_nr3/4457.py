#include<bits/stdc++.h>
#include<ext/numeric>
using namespace std;
using namespace __gnu_cxx;

#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz(v)  (int)v.size()
#define UNVISITED -1
#define CLR(a,v) memset(a,v,sizeof a)
#define PC(x) __builtin_popcount(x)

typedef long long ll;
typedef pair<int, int> ii;
typedef pair<ll, ll> pll;
typedef unsigned long long ull;

int dx[] = { 0, 0, 1, -1, -1, -1, 1, 1 };
int dy[] = { 1, -1, 0, 0, 1, -1, 1, -1 };

ll n, j;
const int MAX = (1 << 17) + 1;
bitset<MAX> bs;
vector<int> primes;
int siz;
void sieve() {
	bs.set();
	bs[0] = bs[1] = 0;
	for (ll i = 2; i < MAX; ++i)
		if (bs[i]) {
			primes.push_back(i);
			for (ll k = i * i; k < MAX; k += i)
				bs[k] = 0;
		}
	siz = sz(primes);
}
int prime(ll x, int base) {
	ll res = 0;
	ll i = 1;
	for (ll k = 0; k < n; ++k, i *= base)
		if (x & (1ll << k))
			res += i;
	int ret = -1;
	for (ll c = 0; c < siz && primes[c] * primes[c] <= res; ++c)
		if (!(res % primes[c])) {
			ret = primes[c];
			break;
		}
	return ret;
}
void conv(ll msk) {
	printf("1");
	for (ll i = n - 2; i; --i)
		if (msk & (1ll << i))
			printf("1");
		else
			printf("0");
	printf("1");
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("C-small-attempt0.in", "rt", stdin);
	freopen("out.txt", "wt", stdout);
#endif
	sieve();
	int t;
	scanf("%d", &t);
	scanf("%lld%lld", &n, &j);
	puts("Case #1:");
	ll msk = 1ll << (n - 1);
	++msk;
	int cnt = 0;
	for (ll i = msk; cnt < j; i += 2) {
		bool b = 1;
		int div[11];
		for (int base = 2; base <= 10 && b; ++base) {
			div[base] = prime(i, base);
			if (div[base] == -1) {
				b = 0;
				break;
			}
		}
		if (b) {
			++cnt;
			conv(i);
			for (int k = 2; k <= 10; ++k)
				printf(" %d", div[k]);
			puts("");
		}
	}
}

