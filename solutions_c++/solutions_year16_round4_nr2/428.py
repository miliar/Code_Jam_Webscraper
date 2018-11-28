#include <bits/stdc++.h>

const int MAXN = 210;

int T, n, m;
double p[MAXN], q[MAXN], f[MAXN][MAXN];

double getValue(){
	f[0][0] = 1;
	for (int i = 1; i <= m; i++)
		for (int j = 0; j * 2 <= m; j++) {
			f[i][j] = f[i - 1][j] * (1 - q[i]);
			if(j >= 1) {
				f[i][j] += f[i - 1][j - 1] * q[i];
			}
		}
	return f[m][m >> 1];
}
int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	std::cin >> T;
	for (int cs = 1; cs <= T; cs++) {
		std::cin >> n >> m;
		for (int i = 1; i <= n; i++) std::cin >> p[i];
		std::sort(p + 1, p + n + 1);
		double answer = 0;
		for (int i = 0; i <= m; i++) {
			int tot = 0, rem = m - i;
			for (int j = 1; j <= i; j++) q[++tot] = p[j];
			for (int j = n - rem + 1; j <= n; j++) q[++tot] = p[j];
			answer = std::max(answer, getValue());
		}
		printf("Case #%d: %.10f\n", cs, answer);
	}
	return 0;
}

