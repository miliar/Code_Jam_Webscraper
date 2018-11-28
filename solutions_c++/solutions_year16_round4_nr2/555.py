#include <iostream>
#include <cstdio>
#include <cstring>  
#include <string>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <ctime>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <cassert>
#include <bitset>

using namespace std;
 
double f[201][201], g[201][201], p[201];

int main() {
	int cases;
	scanf("%d", &cases);
	for (int o = 0; o < cases; ++o) {
		int n, m;
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i) {
			scanf("%lf", &p[i]);
		}
		sort(p, p + n);
		memset(f, 0, sizeof(f));
		f[0][0] = 1.;
		for (int i = 1; i <= m; ++i) {
			for (int j = 0; j <= i; ++j) {
				f[i][j] = f[i - 1][j] * (1 - p[i - 1]);
			   if (j > 0) f[i][j] += f[i - 1][j - 1] * p[i - 1];
			}
		}
		memset(g, 0, sizeof(g));
		g[0][0] = 1.;
		for (int i = 1; i <= m; ++i) {
			for (int j = 0; j <= i; ++j) {
				g[i][j] = g[i - 1][j] * (1 - p[n - i]);
				if (j > 0) g[i][j] += g[i - 1][j - 1] * p[n - i];
			}
		}
		double ans = 0;
		for (int i = 0; i <= m; ++i) {
			double tmp = 0;
			for (int j = 0; j <= m / 2; ++j) {
				tmp += f[i][j] * g[m - i][m / 2 - j];
			}
			if (tmp > ans) ans = tmp;
		}
		printf("Case #%d: %.6f\n", o + 1, ans);
	}		
	return 0;
}


