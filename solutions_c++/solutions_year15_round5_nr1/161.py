#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE

#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <limits>
#include <ctime>
#include <cassert>
#include <map>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <stack>
#include <queue>
#include <numeric>
#include <iterator>
#include <bitset>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> Pii;
typedef pair<ll, ll> Pll;

#define FOR(i,n) for(int i = 0; i < (n); i++)
#define sz(c) ((int)(c).size())
#define ten(x) ((int)1e##x)

#pragma comment(linker,"/STACK:56777216")

template<class T> void chmax(T& l, const T r){ l = max(l, r); }
template<class T> void chmin(T& l, const T r){ l = min(l, r); }

#ifdef _WIN32
#   define mygc(c) (c)=getchar()
#   define mypc(c) putchar(c)
#else
#   define mygc(c) (c)=getchar_unlocked()
#   define mypc(c) putchar_unlocked(c)
#endif

void reader(int& x) { int k, m = 0; x = 0; for (;;) { mygc(k); if (k == '-') { m = 1; break; }if ('0' <= k&&k <= '9') { x = k - '0'; break; } }for (;;) { mygc(k); if (k<'0' || k>'9')break; x = x * 10 + k - '0'; }if (m) x = -x; }
void reader(ll& x) { int k, m = 0; x = 0; for (;;) { mygc(k); if (k == '-') { m = 1; break; }if ('0' <= k&&k <= '9') { x = k - '0'; break; } }for (;;) { mygc(k); if (k<'0' || k>'9')break; x = x * 10 + k - '0'; }if (m) x = -x; }
int reader(char c[]) { int i, s = 0; for (;;) { mygc(i); if (i != ' '&&i != '\n'&&i != '\r'&&i != '\t'&&i != EOF) break; }c[s++] = i; for (;;) { mygc(i); if (i == ' ' || i == '\n' || i == '\r' || i == '\t' || i == EOF) break; c[s++] = i; }c[s] = '\0'; return s; }
template <class T, class S> void reader(T& x, S& y) { reader(x); reader(y); }
template <class T, class S, class U> void reader(T& x, S& y, U& z) { reader(x); reader(y); reader(z); }
template <class T, class S, class U, class V> void reader(T& x, S& y, U& z, V & w) { reader(x); reader(y); reader(z); reader(w); }

void writer(int x, char c) { int s = 0, m = 0; char f[10]; if (x<0)m = 1, x = -x; while (x)f[s++] = x % 10, x /= 10; if (!s)f[s++] = 0; if (m)mypc('-'); while (s--)mypc(f[s] + '0'); mypc(c); }
void writer(ll x, char c) { int s = 0, m = 0; char f[20]; if (x<0)m = 1, x = -x; while (x)f[s++] = x % 10, x /= 10; if (!s)f[s++] = 0; if (m)mypc('-'); while (s--)mypc(f[s] + '0'); mypc(c); }
void writer(const char c[]) { int i; for (i = 0; c[i] != '\0'; i++)mypc(c[i]); }
void writer(const char x[], char c) { int i; for (i = 0; x[i] != '\0'; i++)mypc(x[i]); mypc(c); }
template<class T> void writerLn(T x) { writer(x, '\n'); }
template<class T, class S> void writerLn(T x, S y) { writer(x, ' '); writer(y, '\n'); }
template<class T, class S, class U> void writerLn(T x, S y, U z) { writer(x, ' '); writer(y, ' '); writer(z, '\n'); }
template<class T> void writerArr(T x[], int n) { if (!n) { mypc('\n'); return; }FOR(i, n - 1)writer(x[i], ' '); writer(x[n - 1], '\n'); }

template<class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template<class T> T lcm(T a, T b) { return a / gcd(a, b) * b; }
template<class T> T extgcd(T a, T b, T& x, T& y){ for (T u = y = 1, v = x = 0; a;) { T q = b / a; swap(x -= q * u, u); swap(y -= q * v, v); swap(b -= q * a, a); } return b; }
template<class T> T mod_inv(T a, T m){ T x, y; extgcd(a, m, x, y); return (m + x % m) % m; }
template<class T> T CRT(T r1, T m1, T r2, T m2) { T a1, a2; extgcd(m1, m2, a1, a2); T ret = (m1*a1*r2 + m2*a2*r1) % (m1*m2); return ret < 0 ? ret + m1 * m2 : ret; }

int s[ten(6) + 10];
int m[ten(6) + 10];
vector<int> e[ten(6)];
Pii rg[ten(6)];
int n, d;

void dfs(int v, int par, Pii cur){
	cur.first = min(cur.first, s[v]);
	cur.second = max(cur.second, s[v]);
	rg[v] = cur;
	for (auto to : e[v]) {
		if (to == par) continue;
		dfs(to, v, cur);
	}
}

void read_input(){
	reader(n, d);
	int s0, as, cs, rs; reader(s0, as, cs, rs);
	int m0, am, cm, rm; reader(m0, am, cm, rm);
	s[0] = s0;
	m[0] = m0;
	FOR(i, n - 1){
		s[i + 1] = (s[i] * as + cs) % rs;
		m[i + 1] = (m[i] * am + cm) % rm;
	}

	//n = 4, d = 5;
	//s[0] = 10;
	//s[1] = 8;
	//s[2] = 8;
	//s[3] = 15;
	//m[1] = 0;
	//m[2] = 1;
	//m[3] = 0;

}

ll solve(){
	read_input();

	FOR(i, n) e[i].clear();
	FOR(i, n -1){
		int par = m[i + 1] % (i + 1);
		e[par].push_back(i + 1);
		e[i + 1].push_back(par);
	}

	dfs(0, -1, Pii(s[0],s[0]));
	static int  evt_bucket[ten(6) + 10];
	memset(evt_bucket, 0, sizeof(evt_bucket));
	FOR(i, n){
		int diff = rg[i].second - rg[i].first;
		if (diff > d) continue;
		int l = max(rg[i].second - d, 0);
		int r = min(rg[i].first + 1, ten(6));
		evt_bucket[l]++;
		evt_bucket[r]--;
	}

	int r = rg[0].first, cur = 0;
	int ans = 0;
	FOR(i, ten(6)){
		cur += evt_bucket[i];
		ans = max(ans, cur);
	}

	return ans;
}

int main(){
	int t; cin >> t;
	FOR(i, t){
		ll ans = solve();
		printf("Case #%d: ", i + 1);
		printf("%lld\n", ans);
	}
}