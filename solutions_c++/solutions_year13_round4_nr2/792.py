#include <iostream>
#include <cstdio>
#include <fstream>

#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <utility>
#include <string>
#include <cstring>

#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cassert>
#include <memory.h>
using namespace std;

#define fr(i, n) for (int i = 0; i < (int)(n); i++)
#define fb(i, n) for (int i = n - 1; i >= 0; i--)
#define all(a) (a).begin(), (a).end()
#define _(a, b) memset(a, b, sizeof(a))
#define mp make_pair
#define pb push_back
#define sz(v) ((int)(v).size())

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

inline int ni() { int a; scanf("%d", &a); return a; }
inline double nf() { double a; scanf("%lf", &a); return a; }
template <class T> void out(T a, T b) { bool first = true; for (T i = a; i != b; i++) { if (!first) printf(" "); first = false; cout << *i; } puts(""); }
template <class T> void outl(T a, T b) { for (T i = a; i != b; i++) cout << *i << "\n"; } 

int T;
ll N, P;
ll l, r, res;
ll mx, mb;

inline ll get(ll n, ll pos) {	
	ll ans = (1LL << n) - pos;
	ll val = n;
	ll b = 0;
	while (val != 0) {
		val--;
		if (ans <= 1) {
			b <<= 1;
			b++;
		} else {
			b <<= 1;
		}
		ans >>= 1;
	}
	return b;
}

inline ll get2(ll n, ll pos) {
	ll ans = pos + 1;
	ll val = n;
	ll b = 0;
	while (val != 0) {
		val--;
		if (ans > 1) {
			b <<= 1;
			b++;
		} else {
			b <<= 1;
		}
		ans >>= 1;
	}		
	return b;
}

inline pair<ll, ll> solve() {
	N = ni(); P = ni();
	l = 0, r = (1LL << N);
	while (l < r - 1) {
		res = (l + r) >> 1;
		if (get(N, res) < P)
			l = res;
		else
			r = res;
	}
	mx = l;

	l = 0, r = (1LL << N);
	while (l < r - 1) {
		res = (l + r) >> 1;
		if (get2(N, res) < P)
			l = res;
		else
			r = res;
	}
	mb = l;

	return mp(mb, mx);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	T = ni();
	fr(test, T) {
		pair<ll, ll> ans = solve();
		cout << "Case #" << test + 1 << ": " << ans.first << " " << ans.second << endl;
	}	  
}
        