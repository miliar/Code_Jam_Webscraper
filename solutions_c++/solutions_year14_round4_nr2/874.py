//Template
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
#include <string>
#include <vector>
#include <bitset>
#include <cstdarg>
#include <complex>
using namespace std;

typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef long double ld;
#define pair(x, y) make_pair(x, y)
#define runtime() ((double)clock() / CLOCKS_PER_SEC)

inline int read() {
	static int r, sign;
	static char c;
	r = 0, sign = 1;
	do c = getchar(); while (c != '-' && (c < '0' || c > '9'));
	if (c == '-') sign = -1, c = getchar();
	while (c >= '0' && c <= '9') r = r * 10 + (int)(c - '0'), c = getchar();
	return sign * r;
}

template <typename T>
inline void print(T *a, int n) {
	for (int i = 1; i < n; ++i) cout << a[i] << " ";
	cout << a[n] << endl;
}
#define PRINT(_l, _r, _s, _t) { cout << #_l #_s "~" #_t #_r ": "; for (int _i = _s; _i != _t; ++_i) cout << _l _i _r << " "; cout << endl; }

#define N 10000
int T, Case = 0, n, a[N + 1], b[N + 1], arr[N + 1];

inline int query(int x) {
	int r = 0;
	for (; x <= n; x += x & -x) r += arr[x];
	return r;
}

inline void modify(int x, int v) {
	for (; x > 0; x -= x & -x) arr[x] += v;
}

int calc(int l, int r, bool rev = false) {
	if (l > r) return 0;
	for (int i = 1; i <= n; ++i) arr[i] = 0;
	int ret = 0;
	if (rev) {
		for (int i = r; i >= l; --i) {
			ret += query(a[i]);
			modify(a[i], 1);
		}
	} else {
		for (int i = l; i <= r; ++i) {
			ret += query(a[i]);
			modify(a[i], 1);
		}
	}
	return ret;
}

int main(int argc, char *argv[]) {
#ifdef KANARI
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	
	ios::sync_with_stdio(false);
	cin >> T;
	while (T--) {
		cin >> n;
		for (int i = 1; i <= n; ++i) {
			cin >> a[i];
			b[i] = a[i];
		}
//		sort(b + 1, b + n + 1);
//		for (int i = 1; i <= n; ++i)
//			a[i] = lower_bound(b + 1, b + n + 1, a[i]) - b;
		/*
		int ans = n * n;
		for (int i = 0; i <= n; ++i) {
			ans = min(calc(1, i) + calc(i + 1, n, true), ans);
		}
		*/
		int ans = 0, l = 0, r = 0;
		for (int i = 1, last = 0; i <= n; ++i) {
			int m = INT_MAX, p = 0;
			for (int j = 1; j <= n; ++j)
				if (a[j] > last && a[j] < m) m = a[j], p = j;
			last = m;
			if (p - l - 1 > n - p - r) {
				for (int j = p + 1; j <= n - r; ++j)
					a[j - 1] = a[j], ++ans;
				a[n - r] = m;
				++r;
			} else {
				for (int j = p - 1; j > l; --j)
					a[j + 1] = a[j], ++ans;
				a[l + 1] = m;
				++l;
			}
		}
		
		cout << "Case #" << ++Case << ": " << ans << endl;
	}
	
	fclose(stdin);
	fclose(stdout);
	return 0;
}
