# include <stdio.h>
# include <string.h>
# include <stdlib.h>
# include <map>
# include <algorithm>

using namespace std;

int matrix[55][55];
map<long long, int> mapper;

void complete(int n, int b) {
	for (int i = b - n; i < b; i ++) {
		for (int j = i + 1; j < b; j ++) {
			matrix[i][j] = 1;
		}
	}
}

int main() {
	freopen("a.txt", "r", stdin);
	freopen("b.txt", "w", stdout);

	int t;
	scanf("%d", &t);

	long long f[55];
	memset(f, 0, sizeof(f));
	f[1] = 1;
	f[2] = 1;
	mapper[1] = 2;
	for (int i = 3; i <= 50; i ++) {
		f[i] = f[i - 1] * 2;
		mapper[f[i]] = i;
	}

	for (int kase = 1; kase <= t; kase ++) {
		printf("Case #%d: ", kase);

		int b, m;
		scanf("%d%d", &b, &m);
		
		if (f[b] < m) printf("IMPOSSIBLE\n"); else {
			printf("POSSIBLE\n");
			memset(matrix, 0, sizeof(matrix));

			int x = 0;
			for (int i = 2; i <= 50; i ++) {
				if (f[i] > m) {
					x = i - 1;
					complete(x, b);
					m -= f[i - 1];
					break;
				}
			}

			for (int i = 0; i < b - x; i ++) {
				matrix[i][i + 1] = 1;
			}

			while (m) {
				int p = m & -m;
				matrix[0][b - mapper[p]] = 1;
				m -= p;
			}

			for (int i = 0; i < b; i ++) {
				for (int j = 0; j < b; j ++) printf("%d", matrix[i][j]);
				printf("\n");
			}
		}
	}
}