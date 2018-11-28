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

#define N 1000
int T, n, s;
struct point {
	int x, y, z;
	int vx, vy, vz;
	inline void read() {
		scanf("%d%d%d%d%d%d", &x, &y, &z, &vx, &vy, &vz);
	}
} p[N + 1];

const double eps = 1e-6;

bool v[N + 1];
int q[N + 1];
double dist[N + 1][N + 1];

bool check(double d) {
	for (int i = 1; i <= n; ++i)
		v[i] = false;
	int h = 0, t = 0;
	q[t++] = 1, v[1] = true;
	while (h < t) {
		int cur = q[h++];
		for (int i = 1; i <= n; ++i)
			if (!v[i] && dist[cur][i] <= d) {
				v[i] = true;
				q[t++] = i;
			}
	}
	return v[2];
}

inline double sqr(double x) {
	return x * x;
}

int main(int argc, char *argv[]) {
#ifdef KANARI
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	
	int Case = 0;
	scanf("%d", &T);
	while (T--) {
		scanf("%d%d", &n, &s);
		for (int i = 1; i <= n; ++i)
			p[i].read();
		
		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= n; ++j) {
				dist[i][j] = sqrt(sqr(p[i].x - p[j].x) + sqr(p[i].y - p[j].y) + sqr(p[i].z - p[j].z));
			}
		
		double l = 0.0, r = 2000.0;
		while (r - l > eps) {
			double mid = (l + r) / 2.0;
			if (check(mid)) r = mid;
			else l = mid;
		}
		
		printf("Case #%d: %.7lf\n", ++Case, l);
	}
	
	fclose(stdin);
	fclose(stdout);
	return 0;
}
