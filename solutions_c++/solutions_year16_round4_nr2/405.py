#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>


using namespace std;

long double p[222], a[222][222], b[222][222];
int main() {
	freopen("B.in", "r", stdin);
	freopen("B_l.out", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int cas = 1; cas <= t; cas++){
		printf("Case #%d: ", cas);;
		int n, k;
		scanf("%d%d", &n, &k);
		for (int i = 0; i < n; i++){
			cin >> p[i];
		}
		long double ans = 0;
		sort(p, p + n);

		for (int i = 0; i <= n; i++)
			for (int j = 0; j <= n; j++)
				a[i][j] = b[i][j] = 0;
		a[0][0] = 1;
		a[0][1] = 0;
		for (int i = 1; i <= n; i++)
			for (int j = 0; j <= i + 1; j++){
				a[i][j] = a[i - 1][j] * (1-p[i - 1]) + a[i - 1][j - 1] * p[i - 1];
			}

		b[0][0] = 1;
		b[0][1] = 0;
		for (int i = 1; i <= n; i++)
			for (int j = 0; j <= i + 1; j++){
				b[i][j] = b[i - 1][j] * (1-p[n - i]) + b[i - 1][j - 1] * p[n - i];
			}

		for (int i = 0; i <= k; i++) {
			long double *L = a[i], *R = b[k - i], val = 0;
			for (int j = 0; j <= (k / 2); j++)
				val += L[j] * R[(k / 2) - j];
			if (ans < val)
				ans = val;
		}
		printf("%f\n", (double) ans);
	}
}