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

#define N 200
double p[N + 1], f[N + 1][N + 1], seq[N + 1];
int n, k, T;

double calc() {
	f[0][0] = 1.0;
	for (int i = 1; i <= k; ++i) {
		f[i][0] = f[i - 1][0] * (1 - seq[i]);
		for (int j = 1; j <= i; ++j)
			f[i][j] = f[i - 1][j] * (1 - seq[i]) + f[i - 1][j - 1] * seq[i];
	}
	return f[k][k / 2];
}

int main(int argc, char *argv[]) {
#ifdef KANARI
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	
	int Case = 0;
	cin >> T;
	cout << fixed << setprecision(8);
	while (T--) {
		cin >> n >> k;
		for (int i = 1; i <= n; ++i)
			cin >> p[i];
		
		sort(p + 1, p + n + 1);
		double ans = 0.0;
		for (int i = 0; i <= k; ++i) {
			int cnt = 0;
			for (int j = 1; j <= i; ++j)
				seq[++cnt] = p[j];
			for (int j = 1; j <= k - i; ++j)
				seq[++cnt] = p[n - j + 1];
			ans = max(ans, calc());
		}
		
		cout << "Case #" << ++Case << ": " << ans << endl;
	}
	
	fclose(stdin);
	fclose(stdout);
	return 0;
}
