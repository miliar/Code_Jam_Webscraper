#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <bitset>
#include <queue>
#include <sstream>
using namespace std;
#define clr(a,x) memset(a, x, sizeof(a))
#define all(v) (v).begin(), (v).end()
#define iter(v) __typeof((v).begin())
#define foreach(it, v) for (iter(v) it = (v).begin(); it != (v).end(); it++)
#define pb push_back
#define mp make_pair
#define rep(i, n) for (ll i = 0; i < (ll)(n); i++)
#define FOR(i, a, b) for (int i = (int)(a); i <= (b); i++)
typedef long long ll;
typedef pair <int,int> PII;
ll sqr(ll x) {return x * x;}
template <class T> void checkmax(T &t, T x){if (x > t) t = x;}
template <class T> void checkmin(T &t, T x){if (x < t) t = x;}
template <class T> void _checkmax(T &t, T x){if (t == -1 || x > t) t = x;}
template <class T> void _checkmin(T &t, T x){if (t == -1 || x < t) t = x;}
ll power_mod(ll a, int b, int p) {
	ll ret = 1;
	for (; b; b >>= 1) {
		if (b & 1) ret = ret * a % p;
		a = a * a % p;
	}
	return ret;
}

vector <ll> v;

bool check(ll x) {
	static int a[105];
	int n = 0;
	while (x) {
		a[n++] = x % 10;
		x /= 10;
	}
	int i = 0, j = n - 1;
	while (i < j)
		if (a[i++] != a[j--]) return 0;
	return 1;
}

ll f(ll x) {
	int index = upper_bound(v.begin(), v.end(), x) - v.begin();
	return index;
}

int main() {
	int Tc;
	scanf("%d", &Tc);
	rep (i, 10000001) {
		if (check(i) && check(i * i)) {
			v.push_back(i * i);
		}
	}
	rep (_, Tc) {
		printf("Case #%I64d: ", _ + 1);
		ll a, b;
		cin >> a >> b;
		cout << f(b) - f(a - 1) << endl;
	}
	return 0;
}
