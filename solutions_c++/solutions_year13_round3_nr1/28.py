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
const int N = 1000005;
int n, m;
int nex[N];
char s[N];

bool isv(char c) {
	return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

int main() {
	int Tc;
	scanf("%d", &Tc);
	rep (ri, Tc) {
		printf("Case #%d: ", ri + 1);
		scanf("%s%d", s, &m);
		n = strlen(s);
		for (int i = n - 1; ~i; i--) {
			if (isv(s[i])) {
				nex[i] = i;
			} else {
				nex[i] = i == n - 1 ? -1 : nex[i + 1];
			}
		}
		ll ans = 0;
		set <int> s;
		rep (i, n) {
			int x = nex[i] == -1 ? n - i : nex[i] - i;
			if (x >= m) s.insert(i);
		}
		rep (i, n) {
			set <int>::iterator it = s.lower_bound(i);
			if (it == s.end()) continue;
			int st = *it + m - 1;
			ans += n - st;
		}
		cout << ans << endl;
	}
	return 0;
}
