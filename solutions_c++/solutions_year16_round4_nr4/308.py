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

#define N 4
bool can[N + 1][N + 1], v[N + 1][N + 1], f[N + 1][1 << N | 1], valid[N + 1][1 << (N * N) | 1];
int T, n, seq[N + 1];

inline string binary(int x) {
	string ret = "";
	while (x > 0) {
		if (x & 1) ret.append(1, '1');
		else ret.append(1, '0');
		x >>= 1;
	}
	reverse(ret.begin(), ret.end());
	return ret;
}

inline string binary(int x, int len) {
	string ret = "";
	for (int i = len - 1; i >= 0; --i)
		ret.append(1, '0' + (x >> i & 1));
	return ret;
}

inline string split(string x, int len) {
	string ret = "";
	int cnt = 0;
	for (int i = 0; i < x.length(); ++i) {
		ret.append(1, x[i]);
		++cnt;
		if (cnt == len) {
			ret.append(1, '\n');
			cnt = 0;
		}
	}
	return ret;
}

void calc(int n) {
	for (int x = 0; x < (1 << (n * n)); ++x) {
		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= n; ++j)
				v[i][j] = (x >> ((i - 1) * n + j - 1) & 1);
		for (int i = 1; i <= n; ++i)
			seq[i] = i;
		bool ok = true;
		do {
			memset(f, 0, sizeof f);
			f[0][0] = true;
			for (int i = 1; i <= n; ++i) {
				bool found = false;
				for (int s = 0; s < (1 << n); ++s) {
					if (__builtin_popcount(s) != i - 1) continue;
					if (!f[i - 1][s]) continue;
					bool full = true;
					for (int j = 1; j <= n; ++j) {
						if (v[seq[i]][j] && !(s >> (j - 1) & 1)) {
							f[i][s | (1 << (j - 1))] = true;
							full = false;
						}
					}
					if (full) found = true;
				}
				if (found) ok = false;
			}
		} while (ok && next_permutation(seq + 1, seq + n + 1));
		if (ok) {
			cerr << split(binary(x, n * n), n) << endl;
			valid[n][x] = true;
		}
	}
}

int main(int argc, char *argv[]) {
#ifdef KANARI
	freopen("input.txt", "r", stdin);
	freopen("answer.txt", "w", stdout);
#endif
	
	int Case = 0;
	cin >> T;
	
	for (int n = 1; n <= 4; ++n) {
		calc(n);
	}
	
	while (T--) {
		cin >> n;
		int x = 0;
		for (int i = 1; i <= n; ++i) {
			string s;
			cin >> s;
			for (int j = 1; j <= n; ++j) {
				can[i][j] = s[j - 1] == '1';
				if (s[j - 1] == '1')
					x |= 1 << ((i - 1) * n + j - 1);
			}
		}
		
		int ans = n * n;
		for (int i = 0; i < (1 << (n * n)); ++i)
			if (valid[n][i] && (i & x) == x) {
				ans = min(ans, __builtin_popcount(i ^ x));
			}
		
		cout << "Case #" << ++Case << ": " << ans << endl;
	}
	
	fclose(stdin);
	fclose(stdout);
	return 0;
}
