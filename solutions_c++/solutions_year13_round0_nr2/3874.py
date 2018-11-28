#include <cstdio>

#define N 128

int T, norow, nocol, b[N][N], n, m, t, drow[N], dcol[N];
bool row[N], col[N], f;

int main() {
	scanf("%d", &T);
	for (int r = 1; r <= T; ++r) {
		printf("Case #%d: ", r);
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				scanf("%d", b[i] + j);
		for (int i = 0; i < n; ++i) row[i] = 1;
		for (int j = 0; j < m; ++j) col[j] = 1;
		norow = n; nocol = m; f = 1;
		while (norow && nocol && f) {
			f = 0;
			t = 100;
			for (int i = 0; i < n; ++i) if (row[i])
				for (int j = 0; j < m; ++j) if (col[j])
					if (b[i][j] < t) t = b[i][j];
			for (int i = 0; i < n; ++i) drow[i] = 0;
			for (int j = 0; j < m; ++j) dcol[j] = 0;
			for (int i = 0; i < n; ++i) if (row[i])
				for (int j = 0; j < m; ++j) if (col[j])
					if (b[i][j] == t) {
						++drow[i]; ++dcol[j];
					}
			for (int i = 0; i < n; ++i)
				if (drow[i] == nocol) {
					row[i] = 0; --norow; f = 1;
				}
			if (f)
				continue;
			for (int j = 0; j < m; ++j)
				if (dcol[j] == norow) {
					col[j] = 0; --nocol; f = 1;
				}
		}
		if (f) puts("YES");
		else puts("NO");
	}
	return 0;
}
