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

#define N 110
#define L 60
int T, n, l;
char g[N + 1][L + 1], b[L + 1];

int main(int argc, char *argv[]) {
#ifdef KANARI
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	
	int Case = 0;
	scanf("%d", &T);
	while (T--) {
		scanf("%d%d", &n, &l);
		for (int i = 1; i <= n; ++i)
			scanf("%s", g[i]);
		scanf("%s", b);
		
		bool ok = true;
		for (int i = 1; i <= n; ++i)
			if (!strcmp(g[i], b)) ok = false;
		
		printf("Case #%d: ", ++Case);
		if (!ok) printf("IMPOSSIBLE\n");
		else {
			if (l == 1) {
				printf("0");
			} else {
				for (int i = 1; i <= l - 1; ++i)
					printf("?");
			}
			printf(" ");
			for (int i = 1; i <= (l + 1) / 2; ++i)
				printf("01");
			printf("0?1");
			for (int i = 1; i <= (l + 1) / 2; ++i)
				printf("01");
			printf("\n");
		}
	}
	
	fclose(stdin);
	fclose(stdout);
	return 0;
}
