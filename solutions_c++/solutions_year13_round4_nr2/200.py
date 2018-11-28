#pragma comment(linker, "/STACK:67108864")

#include <iostream>
#include <fstream> 
#include <cstdio>
#include <vector>
#include <stack>
#include <cmath>
#include <algorithm>
#include <string>
#include <cstring>
#include <cassert>
#include <complex>
#include <bitset>
#include <map>
#include <set>
#include <ctime>

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define forab(i, k, n) for(int i = (int)(k); i < (int)(n); i++)
#define forba(i, n, k) for(int i = (int)(n) - 1; i >= (int)(k); i--)

#define vi vector<int>
#define pii pair<int, int>
#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x)*(x))
#define ff first
#define ss second
#define pb push_back
#define mp make_pair

using namespace std;

typedef long long ll;

const long double pi = 3.1415926535897932384626433832795;
const long double eps = 0.000000001;
const int INF = 1E9;
const int MAXN = 100500;
const ll MOD = 1000002013;

int t;
ll n, rounds, p, ans1, ans2;

bool good(ll x, int param) {
	ll pos = 0, a, b, na, nb, k, step;
	a = n - x - 1;
	b = x;
	if (param == 0) { //guarant
		step = n >> 1;
		forn(i, rounds) {
			if (b) {
				b--;
				pos += step;
			} else
				a--;
			na = a >> 1;
			nb = b >> 1;
			if (na + nb + 1 < step)
				na++;

			a = na;
			b = nb;
			step >>= 1;
		}

		return (pos <= p);
	} else { //maybe
		step = n >> 1;
		forn(i, rounds) {
			if (a) 
				a--;
			else {
				b--;
				pos += step;
			}

			na = a >> 1;
			nb = b >> 1;
			if (na + nb + 1 < step)
				nb++;

			a = na;
			b = nb;
			step >>= 1;
		}

		return (pos <= p);
	}
}

ll bins(int param) {
	ll l = 0, r = n, mid;
	while (r - l > 1) {
		mid = (l + r) >> 1;
		if (good(mid, param))
			l = mid;
		else
			r = mid;
	}
	return l;
}

int main() {

	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	cin >> t;
	forn(tt, t) {
		cin >> n >> p;
		p--;
		rounds = n;
		n = (1ll << n);

		ans1 = bins(0);
		ans2 = bins(1);
		printf("Case #%d: %lld %lld\n", tt + 1, ans1, ans2);
	}

	return 0;
}