// lamphanviet@gmail.com
#include <bits/stdc++.h>
using namespace std;

#define fr(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define frr(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)
#define rep(i,n) for (int i = 0, _n = (n); i < _n; i++)
#define repr(i,n) for (int i = (n) - 1; i >= 0; i--)
#define foreach(it, ar) for ( typeof(ar.begin()) it = ar.begin(); it != ar.end(); it++ )
#define fill(ar, val) memset(ar, val, sizeof(ar))

#define ull unsigned long long
#define ll long long
#define all(ar) ar.begin(), ar.end()
#define pb push_back
#define mp make_pair
#define ff first
#define ss second

typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<ii> vii;
typedef vector<int> vi;

#define PI 3.1415926535897932385
#define INF 1000111222
#define EPS 1e-7
#define MAX 100000111
#define MOD 1000000007

int n, m, dd[MAX];
bool isPrime[MAX];
vi primes;

void sieve() {
	fill(isPrime, true);
	isPrime[0] = isPrime[1] = false;
	for (int i = 4; i < MAX; i += 2) {
		isPrime[i] = false;
		dd[i] = 2;
	}
	for (int i = 3; i * i < MAX; i += 2)
		if (isPrime[i])
			for (int j = i * i; j < MAX; j += i + i) {
				isPrime[j] = false;
				dd[j] = i;
			}
	primes.pb(2);
	for (int i = 3; i < MAX; i += 2)
		if (isPrime[i]) primes.pb(i);
}

int notPrime(ll a) {
	if (a < MAX) {
		if (isPrime[a]) return -1;
		return dd[a];
	}
	for (int i = 0; i < primes.size() && primes[i] * 1LL * primes[i] <= a; i++) {
		if (a % primes[i] == 0) return primes[i];
	}
	if (primes.back() * 1LL * primes.back() < a) puts("wrong");
	return -1;
}

ll toDec(int a, int b) {
	ll res = 0, k = 1;
	rep(i, n) {
		int d = (a & (1 << i)) ? 1 : 0;
		if (d) res += k;
		k *= b;
	}
	return res;
}

void print(int a) {
	frr(i, n - 1, 0) printf("%d", (a & (1 << i)) ? 1 : 0);
}

int jam[20];

void check(int a) {
	//printf("checking %d\n", a);
	fr(b, 2, 10) {
		ll d = toDec(a, b);
		jam[b] = notPrime(d);
		if (jam[b] < 0) return;
	}
	print(a);
	fr(b, 2, 10) printf(" %d", jam[b]);
	puts("");
	m--;
}

void gen(int i, int val) {
	if (m <= 0) return;
	if (i >= n - 1) {
		check(val);
		return;
	}
	val |= (1 << (i));
	gen(i + 1, val);

	val ^= (1 << (i));
	gen(i + 1, val);
}

void solve() {
	int start = 1;
	start |= (1 << (n - 1));
	gen(1, start);
}

int main() {
	//ios::sync_with_stdio(false);
	#ifndef ONLINE_JUDGE
		freopen("test.inp", "r", stdin);
		freopen("test.out", "w", stdout);
	#endif
	sieve();
	int cases, caseNo = 0;
	for (scanf("%d", &cases); cases--; ) {
		scanf("%d %d", &n, &m);
		printf("Case #%d:\n", ++caseNo);
		solve();
	}
	return 0;
}

