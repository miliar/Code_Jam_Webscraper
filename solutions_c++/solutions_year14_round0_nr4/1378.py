//Codejam 2014 Qualification D
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
int Case = 0, T, n;
double a[N + 1], b[N + 1];

set <double> h;
set <double> :: iterator it;

int main(int argc, char *argv[]) {
#ifdef KANARI
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	
	scanf("%d", &T);
	while (T--) {
		scanf("%d", &n);
		for (int i = 1; i <= n; ++i) scanf("%lf", a + i);
		for (int i = 1; i <= n; ++i) scanf("%lf", b + i);
		sort(a + 1, a + n + 1);
		sort(b + 1, b + n + 1);
		
		int ans1 = 0, ans2 = 0;
		h.clear();
		for (int i = 1; i <= n; ++i) h.insert(b[i]);
		for (int i = 1; i <= n; ++i)
			if (a[i] > *h.begin()) ++ans1, h.erase(h.begin());
			else h.erase(--h.end());
		h.clear();
		for (int i = 1; i <= n; ++i) h.insert(b[i]);
		for (int i = 1; i <= n; ++i) {
			it = h.lower_bound(a[i]);
			if (it == h.end()) ++ans2, h.erase(h.begin());
			else h.erase(it);
		}
		
		printf("Case #%d: %d %d\n", ++Case, ans1, ans2);
	}
	
	fclose(stdin);
	fclose(stdout);
	return 0;
}
