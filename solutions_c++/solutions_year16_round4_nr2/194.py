#include <bits/stdc++.h>

using namespace std;
#define FOR(i,n) for(int i = 0; i < (n); i++)
#define sz(c) ((int)c.size())
#define ten(n) ((int)1e##n)
using ll = long long;

template<typename ...> static inline int getchar_unlocked(void) { return getchar(); }
template<typename ...> static inline void putchar_unlocked(int c) { putchar(c); }
#define mygc(c) (c)=getchar_unlocked()
#define mypc(c) putchar_unlocked(c)
void reader(int& x) { int k, m = 0; x = 0; for (;;) { mygc(k); if (k == '-') { m = 1; break; }if ('0' <= k&&k <= '9') { x = k - '0'; break; } }for (;;) { mygc(k); if (k<'0' || k>'9')break; x = x * 10 + k - '0'; }if (m) x = -x; }
void reader(ll& x) { int k, m = 0; x = 0; for (;;) { mygc(k); if (k == '-') { m = 1; break; }if ('0' <= k&&k <= '9') { x = k - '0'; break; } }for (;;) { mygc(k); if (k<'0' || k>'9')break; x = x * 10 + k - '0'; }if (m) x = -x; }
int reader(char c[]) { int i, s = 0; for (;;) { mygc(i); if (i != ' '&&i != '\n'&&i != '\r'&&i != '\t'&&i != EOF) break; }c[s++] = i; for (;;) { mygc(i); if (i == ' ' || i == '\n' || i == '\r' || i == '\t' || i == EOF) break; c[s++] = i; }c[s] = '\0'; return s; }
int reader(string& c) { int i; for (;;) { mygc(i); if (i != ' '&&i != '\n'&&i != '\r'&&i != '\t'&&i != EOF) break; }c.push_back(i); for (;;) { mygc(i); if (i == ' ' || i == '\n' || i == '\r' || i == '\t' || i == EOF) break; c.push_back(i); }; return sz(c); }
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
template<class T> void writerArr(vector<T>& x) { writerArr(x.data(), (int)x.size()); }

template<class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template<class T> T lcm(T a, T b) { return a / gcd(a, b) * b; }
ll mod_pow(ll a, ll n, ll mod) {
	ll ret = 1;
	ll p = a % mod;
	while (n) {
		if (n & 1) ret = ret * p % mod;
		p = p * p % mod;
		n >>= 1;
	}
	return ret;
}
template<class T> T extgcd(T a, T b, T& x, T& y) { for (T u = y = 1, v = x = 0; a;) { T q = b / a; swap(x -= q * u, u); swap(y -= q * v, v); swap(b -= q * a, a); } return b; }
template<class T> T mod_inv(T a, T m) { T x, y; extgcd(a, m, x, y); return (m + x % m) % m; }

using Pii = pair<int,int>;

double niv(vector<double> vd, int k) {
	const int n = sz(vd);
	double ans = 0;
	vector<int> t;
	if (k == 2) {
		FOR(i, n) FOR(j, n) {
			if (i == j) continue;
			double d = vd[i] * (1 - vd[j]) + (1 - vd[i]) * vd[j];
			if (ans < d) {
				ans = d;
				t = vector<int>{i, j};
			}
		}
	} else if (k == 4) {
		FOR(i, n) for (int j = i + 1; j < n; j++) {
			for (int k = j + 1; k < n; k++) {
				for (int l = k + 1; l < n; l++) {
					double x[4] = { vd[i], vd[j], vd[k], vd[l] };
					double y[5]; FOR(i, 5) y[i] = 0;
					y[0] = 1.0;
					FOR(a, 4) {
						for (int b = 3; b >= 0; b--) {
							y[b + 1] += y[b] * x[a];
							y[b] *= (1 - x[a]);
						}
					}
					double d = y[2];
					if (ans < d) {
						ans = d;
						t = vector<int>{i, j,k,l};
					}
				}
			}
		}
	}
	writerArr(t);
	return ans;
}

double calc(vector<double>& x) {
	vector<double> y(sz(x) + 1);
	y[0] = 1.0;
	for(auto a: x) {
		for (int b = sz(x) - 1; b >= 0; b--) {
			y[b + 1] += y[b] * a;
			y[b] *= (1 - a);
		}
	}
	return y[sz(x) / 2];
}

void test() {
	while (true) {
		vector < double> vd;
		FOR(i, 10) vd.push_back(rand() / double(RAND_MAX * 10));
		sort(vd.begin(), vd.end());
		niv(vd, 2);
		niv(vd, 4);
	}
}

void solve() {
	int n, k; cin >> n >> k;
	vector<double> vd(n);
	FOR(i, n) cin >> vd[i];
	sort(vd.begin(), vd.end());
	double ans = 0.0;
	FOR(i, k + 1) {
		vector<double> us;
		FOR(j, i) us.push_back(vd[j]);
		FOR(j, k - i) us.push_back(vd[n - 1 - j]);
		auto d = calc(us);
		ans = max(ans, d);
	}

	printf("%.10lf\n",ans);
}

int main() {
	// test();
	int t; cin >> t;
	FOR(i, t) {
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}