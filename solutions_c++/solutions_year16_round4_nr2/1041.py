#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>

using namespace std;

double p[205];

double dp[(1 << 17)][17];

void relax(double &a, double b) {
	if (b > a)
		a = b;
}

int count(int x) {
	int c = 0;
	while (x) {
		c += (x % 2);
		x /= 2;
	}
	return c;
}

int main() {
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	cin.tie(0);
	ios_base::sync_with_stdio(false);

	int t;
	cin >> t;
	for (int q = 0; q < t; q++) {
		int n, k;
		cin >> n >> k;
		for (int j = 0; j < n; j++) {
			cin >> p[j];
		}

		for (int i = 0; i < (1 << n); i++) {
			for (int j = 0; j <= n; j++)
					dp[i][j] = 0.0;
		}
		dp[0][0] = 1.0;
		double mx = 0.0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < (1 << i); j++) {
				for (int l = 0; l <= i + 1; l++) {
					relax(dp[j | (1 << i)][l], dp[j][l] * (1 - p[i]) + p[i] * (l > 0 ? dp[j][l - 1] : 0));
					if (dp[j | (1 << i)][l] > mx && count(j) + 1 == k &&  l * 2 == k)
						mx = dp[j | (1 << i)][l];
				}
			}
		}
		printf("Case #%d: %0.8lf\n", q + 1, mx);
	}



	return 0;
}