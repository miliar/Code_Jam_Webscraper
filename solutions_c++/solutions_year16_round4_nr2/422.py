#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<queue>
#include<stack>
#include<map>
#include<vector>
#include<string>
using namespace std;

int n, K;
double f[500][500], a[500], b[500];

void work() {
	double ans = 0;
	scanf("%d%d", &n, &K);
	for (int i = 0; i < n; ++i) {
		scanf("%lf", &a[i]);
	}
	sort(a, a + n);
	/*
	for (int i = 0; i < n; ++i) {
		printf("%lf ", a[i]);
	}
	printf("\n");
	*/
	for (int i = 0; i <= K; ++i) {
		int m = 0;
		for (int j = 0; j < i; ++j) {
			b[m++] = a[j];
		}
		for (int j = n - (K-i); j < n; ++j) {
			//printf("j= %d", j);
			b[m++] = a[j];
		}
		/*
		printf("m=%d\n", m);
		for (int j = 0; j < m; ++j) {
			printf("%lf ", b[j]);
		}
		printf("\n\n");
		*/
		memset(f, 0, sizeof(f));
		f[0][0] = 1 - b[0], f[0][1] = b[0];
		for (int j = 1; j < K; j++) {
			for (int k = 0; k <= j + 1; ++k) {
				if (k == 0) f[j][k] = f[j-1][k] * (1 - b[j]);
				else if (k == j + 1) f[j][k] = f[j-1][k-1] * b[j];
				else f[j][k] = f[j-1][k-1] * b[j] + f[j-1][k] * (1 - b[j]);
			}
		}
		ans = max(ans, f[K-1][K/2]);
	}
	printf("%.6lf\n", ans);
}

int main() {
	freopen("B-large.in", "r", stdin);
	int TestCase;
	scanf("%d", &TestCase);
	for (int i = 1; i <= TestCase; ++i) {
		printf("Case #%d: ", i);
		work();
	}
	
	return 0;
}