#include <bits/stdc++.h>

const int N = 250;

int n, m;
double p[N];

int bit(int state, int x) {
	return (state >> (x - 1)) & 1;
}

void init() {
	std::cin >> n >> m;
	for (int i = 1; i <= n; i ++) {
		scanf("%lf", &p[i]);
	}
}

double solve(std::vector<double> vec) {
	static double f[N][N];
	
	memset(f, 0, sizeof(f));
	
	f[0][0] = 1.0;
	for (int i = 0; i < m; i ++) {
		for (int j = 0; j <= i; j ++) {
			f[i + 1][j] += f[i][j] * (1 - vec[i + 1]);
			f[i + 1][j + 1] += f[i][j] * vec[i + 1];
		}
	}
	return f[m][m / 2];
}

void work() {
	double answer = 0;
	/*
	for (int state = 0; state < (1 << n); state ++) {
		if (__builtin_popcount(state) == m) {
			std::vector<double> vec;
			vec.push_back(0);
			for (int j = 1; j <= n; j ++) {
				if (bit(state, j) == 1) {
					vec.push_back(p[j]);
				}
			}
			answer = std::max(answer, solve(vec));
		}
	}*/
	std::sort(p + 1, p + n + 1);
	for (int i = 0; i <= m; i ++) {
		std::vector<double> vec(1, 0);
		for (int j = 1; j <= i; j ++) {
			vec.push_back(p[j]);
		}
		for (int j = 1; j <= m - i; j ++) {
			vec.push_back(p[n - j + 1]);
		}
		answer = std::max(answer, solve(vec));
	}
	printf("%.10f\n", answer);
}

int main() {
	freopen("b1.in", "r", stdin);
	freopen("b1.out", "w", stdout);
	
	int testCnt;
	std::cin >> testCnt;
	for (int i = 1; i <= testCnt; i ++) {
		printf("Case #%d: ", i);
		init();
		work();
	}
	
	return 0;
}
