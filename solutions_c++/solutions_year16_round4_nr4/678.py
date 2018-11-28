#include <cstdio>
#include <algorithm>

using namespace std;

const int N = 25;
const int INF = ~0u >> 1;

int n;
int a[N][N];
int b[N], c[N];
int before;

int test(int i, int j) {
	//printf("%d %d\n", i, j);
	if (i == n) {
		//printf("a\n");
		//for (i = 0; i < n; i++) {
			//for (j = 0; j < n; j++) printf("%d", a[i][j]);
			//printf("\n");
		//}
		for (i = 0; i < n; i++)
			for (j = 0; j < n; j++)
				for (int k = 0; k < n; k++) {
					if (a[i][j] == 1 && a[i][k] == 1)
						for (int l = 0; l < n; l++)
							if ((a[l][j] | a[l][k]) == 1 && (a[l][j] & a[l][k]) == 0) return INF;
					if (a[i][j] == 1 && a[k][j] == 1)
						for (int l = 0; l < n; l++)
							if ((a[i][l] | a[k][l]) == 1 && (a[i][l] & a[k][l]) == 0) return INF;
				}
		for (i = 0; i < n; i++) b[i] = c[i] = 0;
		int sum = 0;
		for (i = 0; i < n; i++)
			for (j = 0; j < n; j++)
				if (a[i][j] == 1) {
					b[i]++;
					c[j]++;
					sum++;
				}
		for (i = 0; i < n; i++)
			for (j = 0; j < n; j++)
				if (a[i][j] == 1)
					if (b[i] != c[j]) return INF;
		for (i = 0; i < n; i++) if (b[i] == 0) return INF;
		for (i = 0; i < n; i++) if (c[i] == 0) return INF;
		return sum - before;
	}
	if (j == n) return test(i + 1, 0);
	if (a[i][j] == 1) return test(i, j + 1);
	int ans = test(i, j + 1);
	a[i][j] = 1;
	ans = min(ans, test(i, j + 1));
	a[i][j] = 0;
	return ans;
}
int main() {
	int t, tt;
	scanf("%d", &t);
	for (tt = 1; tt <= t; tt++) {
		scanf("%d", &n);
		before = 0;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++) {
				char c;
				scanf(" %c", &c);
				a[i][j] = c - '0';
				before += a[i][j];
			}
		printf("Case #%d: %d\n", tt, test(0, 0));
	}
	return 0;
}
