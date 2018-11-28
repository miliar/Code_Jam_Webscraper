#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <iomanip>
#include <iostream>
#include <queue>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

#define INF 1000000000
#define FOR(i, a, b) for(int i=int(a); i<int(b); i++)
#define FORC(cont, it) for(typeof((cont).begin()) it = (cont).begin(); it != (cont).end(); it++)
#define pb push_back

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;

#define maxN 17
#define maxJ 501
#define maxB 11
#define ansCount 10
#define maxNum 40000

ll ans[maxN][maxJ][10];

// Returns (a * b) % c, and avoids overflow
ll mulmod(ll a, ll b, ll c) {
	ll x = 0, y = a % c;
	while (b) {
		if (b & 1) x = (x + y) % c;
		y = (y << 1) % c;
		b >>= 1;
	}
	return x % c;
}

// Returns (x**n) % MOD, avoids overflow
ll fastPow(ll x, ll n, ll MOD) {
	ll ret = 1;
	while (n) {
		if (n & 1) ret = mulmod(ret, x, MOD);
		x = mulmod(x, x, MOD);
		n >>= 1;
	}
	return ret;
}

// Miller-Rabin primality test
// Over all Time Complexity is (logN)**3 (if N is relatively small it could be said its (logN)**4 because of the constant 9)
bool isPrime(ll n) {
	ll d = n - 1;
	int s = 0;
	while (d % 2 == 0) {
		s++;
		d >>= 1;
	}
	// It's garanteed that these values will work for any number smaller than 3*10**18 (3 and 18 zeros)
	int a[9] = { 2, 3, 5, 7, 11, 13, 17, 19, 23 };
	FOR(i, 0, 9) if (a[i] == n) return true;
	FOR(i, 0, 9) {
		bool comp = fastPow(a[i], d, n) != 1;
		if (comp) FOR(j, 0, s) {
			ll fp = fastPow(a[i], (1LL << (ll)j)*d, n);
			if (fp == n - 1) {
				comp = false;
				break;
			}
		}
		if (comp) return false;
	}
	return true;
}

ll gcd(ll a, ll b) {
	if (b) return gcd(b, a%b);
	return a;
}

ll A, B;
vector<ll> factors;
ll f(ll x, ll n) {
	return (mulmod(x, (x + A), n) + B) % n;
}
void pollardRho(ll n) {
	if (n == 1) return;
	if (isPrime(n)) {
		factors.pb(n);
		return;
	}
	ll d = n, x, y;
	while (d == n) {
		d = 1;
		x = y = 2;
		A = 2 + rand() % (n - 2);
		B = 2 + rand() % (n - 2);
		while (d == 1) {
			x = f(x, n);
			y = f(f(y, n), n);
			d = gcd(abs(x - y), n);
		}
	}
	factors.push_back(d);
}

ll convert(ll num, int base) {
	ll ans = 0;
	while (num) {
		ans = ans*base + (num & 1);
		num >>= 1;
	}
	return ans;
}

int main() {
	int T, caso=1, N, J, ac=0;
	cin >> T;
	FOR(i, 1<<maxN-2, 1<<maxN-1) {
		if (!(i & 1)) continue;
		bool valid = true;
		FOR(j, 2, maxB) {
			ll n = convert(i, j);
			if (j == 10) ans[maxN - 1][ac][0] = n;
			factors.clear();
			pollardRho(n);
			ans[maxN-1][ac][j - 1] = factors[0];
			if (isPrime(n)) valid = false;
		}
		if (valid) {
			ac++;
		}
		if (ac > 100) break;
	}
	while (T--) {
		cin >> N >> J;
		cout << "Case #" << caso++ << ": " << endl;
		FOR(i, 0, J) {
			FOR(j, 0, ansCount) {
				cout << ans[N][i][j] << " \n"[j==ansCount-1];
			}
		}
	}
	return 0;
}
