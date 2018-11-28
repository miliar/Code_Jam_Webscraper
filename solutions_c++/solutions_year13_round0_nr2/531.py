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
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
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
const int N = 105;
int m, n;
int a[N][N];

int main() {
	int Tc;
	scanf("%d", &Tc);
	rep (_, Tc) {
		printf("Case #%d: ", _ + 1);
		scanf("%d%d", &m, &n);
		rep (i, m)
			rep (j, n)
				scanf("%d", &a[i][j]);
		bool ans = 1;
		rep (i, m)
			rep (j, n) {
				bool row = 1, col = 1;
				rep (k, m)
					if (a[k][j] > a[i][j]) col = 0;
				rep (k, n)
					if (a[i][k] > a[i][j]) row = 0;
				if (!row && !col) ans = 0;
			}
		puts(ans ? "YES" : "NO");
	}
	return 0;
}
