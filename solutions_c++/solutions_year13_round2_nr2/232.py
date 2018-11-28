#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>

using namespace std;

double f[2111][2111];

inline int pos_rank(int x, int y) {
	return (abs(x) + abs(y)) / 2;
}

inline int rank_num(int n) {
	return (n + 1) * (n + n + 1);
}

inline int n_rank(int n) {
	int x = 0;
	while (rank_num(x) <= n) x++;
	return x;
}

void work() {
	int n, x, y; scanf("%d%d%d", &n, &x, &y);
	//printf("%d %d %d ", n, x, y);

	int r_pos = pos_rank(x, y), r_n = n_rank(n);

	//printf(" (r_pos = %d, r_n = %d) ", r_pos, r_n);

	if (r_pos > r_n) {
		printf("%.10f\n", 0.); return ;
	}
	if (r_pos < r_n) {
		printf("%.10f\n", 1.); return ;
	}

	int m = r_n + r_n; n -= rank_num(r_n - 1);
	/*for (int i = 0; i <= m; ++i)
		for (int j = 0; j + i <= n && j <= m; ++j)
			f[i][j] = 0.;*/
	memset(f, 0, sizeof(f));
	f[0][0] = 1.;


	//printf(" (m = %d, n = %d) ", m, n);
	double ans = 0.;
	for (int k = 0; k <= n; ++k)
		for (int i = 0; i <= m && i <= k; ++i) {
			if (k - i > m) continue;
			if (i < m) {
				if (k - i < m) {
					f[i + 1][k - i] += f[i][k - i] * 0.5;
					f[i][k - i + 1] += f[i][k - i] * 0.5;
				}
				else f[i + 1][k - i] += f[i][k - i];
			}
			else
				if (k - i < m) f[i][k - i + 1] += f[i][k - i];
		}

	for (int i = y + 1; i <= m && i <= n; ++i) ans += f[i][n - i];

	printf("%.10f\n", ans);
}

int main() {
	int T; scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		printf("Case #%d: ", t);
		work();
	}

	return 0;
}
