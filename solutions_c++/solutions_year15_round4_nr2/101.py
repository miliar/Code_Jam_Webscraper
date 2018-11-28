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

#define N 100
int T, n;
double V, X, v[N + 1], x[N + 1];

int main(int argc, char *argv[]) {
#ifdef KANARI
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	
	int Case = 0;
	scanf("%d", &T);
	while (T--) {
		scanf("%d%lf%lf", &n, &V, &X);
		for (int i = 1; i <= n; ++i)
			scanf("%lf%lf", v + i, x + i);
		
		double ans = 0.0;
		if (n == 1) {
			if (X == x[1]) ans = V / v[1];
			else ans = -1.0;
		} else if (n == 2) {
			if (x[1] < X && x[2] < X) ans = -1.0;
			else if (x[1] > X && x[2] > X) ans = -1.0;
			else if (x[1] == X && x[2] == X) ans = V / (v[1] + v[2]);
			else if (x[1] == X) ans = V / v[1];
			else if (x[2] == X) ans = V / v[2];
			else {
				double t2 = V * (X - x[1]) / v[2] / (x[2] - x[1]);
				double t1 = V * (X - x[2]) / v[1] / (x[1] - x[2]);
				ans = max(t1, t2);
			}
		} else {
			
			for (int i = 1; i < n; ++i) {
				double coef = (v[i] - (x[i] - X) * v[i] / (x[n] - X) / v[n]);
				if (coef > 0) ans += coef;
			}
			if (ans == 0.0) ans = -1.0;
			else ans = V / ans;
		}
		printf("Case #%d: ", ++Case);
		if (ans < 0) printf("IMPOSSIBLE\n");
		else printf("%.10lf\n", ans);
	}
	
	fclose(stdin);
	fclose(stdout);
	return 0;
}
