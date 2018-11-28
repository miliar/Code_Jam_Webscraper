#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int N = 200 + 7;

int n, k;
double p[N];

double f[N][N];

double calc(vector<double> block) {
	int m = block.size();
	for (int i = 0; i <= m; i++) {
		for (int j = 0; j <= m; j++) {
			f[i][j] = 0;
		}
	}
	f[0][0] = 1;
	for (int i = 0; i < m; i++) {
		for (int j = 0; j <= i; j++) {
			f[i + 1][j] += f[i][j] * block[i];
			f[i + 1][j + 1] += f[i][j] * (1 - block[i]);
		}
	}

	return f[m][m / 2];
}

int main() {
	int test;
	scanf("%d", &test);
	while (test--) {
		scanf("%d %d", &n, &k);
		double answer = 0;
		for (int i = 1; i <= n; i++) {
			scanf("%lf", &p[i]);
		}
		sort(p + 1, p + n + 1);
		for (int i = 0; i <= k; i++) {
			vector<double> block;
			for (int j = 1; j <= i; j++) {
				block.push_back(p[j]);
			}
			for (int j = n - (k - i) + 1; j <= n; j++) {
				block.push_back(p[j]);
			}
			answer = max(answer, calc(block));
		}

		static int testCount = 0;
		printf("Case #%d: %.8f\n", ++testCount, answer);

	}
	return 0;
}
