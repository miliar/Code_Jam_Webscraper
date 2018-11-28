#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <deque>
#include <bitset>

#define sqr(x) ((x) * (x))
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define y0 ywuerosdfhgjkls
#define y1 hdsfjkhgjlsdfhgsdf
#define j1 j924
#define j0 j2834
#define sqrt(x) (sqrt(abs(x)))
#define re return
#define sz(x) ((int)(x).size())
#define all(x) (x).begin(), (x).end()
#define rep(i, n) for (int i = 0; i < (n); i++)
#define rrep(i, n) for (int i = ((n) - 1); i >= 0; i--)
#define fill(a, x) memset(a, x, sizeof(a))

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair <int, int> ii;
typedef vector <int> vi;
typedef vector <ii> vii;
typedef vector <vi> vvi;
typedef double D;
typedef vector <string> vs;

template <class T> inline T abs(T a) {
	return a > 0 ? a : -a;
}

int n;
int m;

bool possibly(ll n, ll x, ll p) {
	if (x == 0)
		re true;
	ll N = 1ll << n;
	if (x >= N)
		re false;
	if (p >= N)
		re true;

	if (x < N / 2 && p <= N / 2)
		re possibly(n - 1, x - x / 2, p);
	if (x < N / 2 && p > N / 2)
		re true;
	if (x >= N / 2 && p <= N / 2)
		re possibly(n - 1, x - x / 2, p);
	if (x >= N / 2 && p > N / 2) {
		if (x != N - 1)
			re true;
	}
	re false;
}

bool sure(ll n, ll x, ll p) {
	if (x == 0)
		re true;
	ll N = 1ll << n;
	if (x >= N)
		re false;
	if (p >= N)
		re true;

	if (p <= N / 2) {
		re x == 0;
	}
	
	re sure(n - 1, (x - 1) / 2 , p - N / 2);

}

int main() {
	int T;
	cin >> T;
	rep(I, T) {
		cout << "Case #" << I + 1 << ":";
		ll n, p;
		cin >> n >> p;
		ll l, r;
		l = 0; r = 1 << n;
		while (r - l > 1) {
			ll x = (l + r) / 2;
			if (sure(n, x, p))
				l = x;
			else
				r = x;
		}
		cout << " " << l;
		l = 0; r = 1 << n;
		while (r - l > 1) {
			ll x = (l + r) / 2;
			if (possibly(n, x, p))
				l = x;
			else
				r = x;
		}
		cout << " " << l << endl;
	}
	return 0;
}
