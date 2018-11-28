//
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <climits>
#include <cmath>
#include <utility>
#include <set>
#include <map>
#include <queue>
#include <ios>
#include <iomanip>
#include <ctime>
#include <numeric>
#include <functional>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <bitset>
#include <cstdarg>
using namespace std;

inline int read() {
	static int r;
	static char c;
	r = 0, c = getchar();
	while (c < '0' || c > '9') c = getchar();
	while (c >= '0' && c <= '9') r = r * 10 + (c - '0'), c = getchar();
	return r;
}

template <typename T>
inline void print(T *a, int n) {
	for (int i = 1; i < n; ++i) cout << a[i] << " ";
	cout << a[n] << endl;
}
#define PRINT(__l, __r, __begin, __end) { for (int __i = __begin; __i != __end; ++__i) cout << __l __i __r << " "; cout << endl; }

typedef long long ll;
#define pair(x, y) make_pair(x, y)
#define runtime() ((double)clock() / CLOCKS_PER_SEC)

#define N 10000
int n, m, T;
struct point {
	int x;
	ll v, v2;
/*	inline bool operator < (const point &p) const {
		return x == p.x ? v > p.v : x < p.x;
	}
*/} p[N + 1];
const ll mod = 1000002013LL;

inline ll cost(int l, int r) {
	int len = r - l;
	return ((ll)n * len - len * (len - 1) / 2) % mod;
}

int tc = 0;

map <int, ll> h;

int stack[N + 1];

int main(int argc, char* argv[]) {
#ifdef KANARI
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	
	cin >> T;
	
	while (T--) {
		cin >> n >> m;
		int cnt = 0;
		
		ll sum = 0LL;
		h.clear();
		for (int i = 1; i <= m; ++i) {
			int l, r, k;
			cin >> l >> r >> k;
			sum += (ll)k * cost(l, r) % mod;
			if (sum >= mod) sum -= mod;
			h[l] += k, h[r] -= k;
		}
		
		for (map <int, ll> :: iterator it = h.begin(); it != h.end(); ++it) {
			++cnt;
			p[cnt].x = it->first, p[cnt].v = it->second;
		}		
		
//		for (int i = 1; i <= cnt; ++i) cout << p[i].x << " " << p[i].v << endl;
		
		int c = 0;
		/*
		for (int i = 1, j; i <= cnt; i = j) {
			
			c += p[i].v;
			for (j = i + 1; c > 0 && j <= cnt; ++j) c += p[j].v;
			int l = i, r = j - 1;
			while (l <= r) {
				if (p[l].v2 > p[r].v2) {
					sum -= p[r].v2 * cost(p[l].x, p[r].x) % mod;
					p[l].v2 -= p[r].v2;
					--r;
				} else if (p[l].v2 == p[r].v2) {
					sum -= (ll)p[l].v2 * cost(p[l].x, p[r].x) % mod;
					++l, --r;
				} else {
					sum -= p[l].v2 * cost(p[l].x, p[r].x) % mod;
					p[r].v2 -= p[l].v2;
					++l;
				}
				if (sum < 0) sum += mod;
			}
		}
		*/
		int top = 0;
		for (int i = 1; i <= cnt; ++i) {
			if (p[i].v > 0) stack[++top] = i;
			else {
				while (p[i].v < 0) {
					ll cur = min(-p[i].v, p[stack[top]].v);
					p[i].v += cur, p[stack[top]].v -= cur;
					sum -= cur * cost(p[stack[top]].x, p[i].x);
					if (sum < 0) sum += mod;
					if (!p[stack[top]].v) -- top;
				}
			}
		}
		
		cout << "Case #" << ++tc << ": " << sum << endl;
	}
	
	return 0;
}

