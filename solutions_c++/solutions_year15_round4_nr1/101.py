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
int T, n, m;
char a[N + 1][N + 1];
char dir[] = "v>^<";

bool check(int x, int y, char dir) {
	int dx = 0, dy = 0;
	if (dir == 'v') dx = 1;
	else if (dir == '^') dx = -1;
	else if (dir == '>') dy = 1;
	else dy = -1;
	x += dx, y += dy;
	while (x > 0 && y > 0 && x <= n && y <= m) {
		if (a[x][y] != '.') return true;
		x += dx, y += dy;
	}
	return false;
}

int main(int argc, char *argv[]) {
#ifdef KANARI
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	
	int Case = 0;
	scanf("%d", &T);
	while (T--) {
		scanf("%d%d", &n, &m);
		for (int i = 1; i <= n; ++i)
			scanf("%s", a[i] + 1);
		
		int ans = 0;
		for (int i = 1; ans != -1 && i <= n; ++i)
			for (int j = 1; ans != -1 && j <= m; ++j)
				if (a[i][j] != '.') {
					if (!check(i, j, a[i][j])) {
						bool ok = false;
						for (int d = 0; !ok && d < 4; ++d)
							if (dir[d] != a[i][j] && check(i, j, dir[d]))
								ok = true;
						if (ok) ++ans;
						else ans = -1;
					}
				}
		
		printf("Case #%d: ", ++Case);
		if (ans == -1) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
	}
	
	fclose(stdin);
	fclose(stdout);
	return 0;
}
