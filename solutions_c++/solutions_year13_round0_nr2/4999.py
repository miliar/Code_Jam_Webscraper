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

typedef long long ll;
#define pair(x, y) make_pair(x, y)

#define N 100
int T, n, m, a[N + 1][N + 1];
int tc = 0;
bool v[N + 1][N + 1], r[N + 1], c[N + 1];

int main() {
#ifdef KANARI
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	cin >> T;
	while (T--) {
		cin >> n >> m;
		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= m; ++j)
				cin >> a[i][j];
				
		bool ok = true;
		for (int w = 2; ok && w > 0; --w) {
			for (int i = 1; i <= n; ++i)
				for (int j = 1; j <= m; ++j)
					if (a[i][j] <= w) v[i][j] = true;
					else v[i][j] = false;
			memset(r, 0, sizeof r), memset(c, 0, sizeof c);
			for (int i = 1; i <= n; ++i) {
				bool fine = true;
				for (int j = 1; fine && j <= m; ++j)
					if (!v[i][j]) fine = false;
				r[i] = fine;
			}
			for (int i = 1; i <= m; ++i) {
				bool fine = true;
				for (int j = 1; fine && j <= n; ++j)
					if (!v[j][i]) fine = false;
				c[i] = fine;
			}

			for (int i = 1; ok && i <= n; ++i)
				for (int j = 1; ok && j <= m; ++j) {
					if (v[i][j] && !r[i] && !c[j]) ok = false;
					if (!v[i][j] && (r[i] || c[j])) ok = false;
				}
		}
		
		cout << "Case #" << ++tc << ": " << (ok ? "YES" : "NO") << endl;
	}

	return 0;
}


