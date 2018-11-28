#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

#define N 5000

int n, R, P, S;
int dp[N][15];
char a[N];
int ans[3][15][N], num[3][15];
int _pow[20];
/*
bool check() {
	int num = _pow[n];
	// printf("%d\n", num);
	for (int i = 0; i < num; i++) {
		if (a[i] == 'P') dp[i][0] = 0;
		else if (a[i] == 'R') dp[i][0] = 1;
		else dp[i][0] = 2;
	}
	for (int i = 1, l = 2; i <= n; i += 1, l *= 2) {
		for (int j = 0; j < num; j += l) {
			if (dp[j][i - 1] == dp[j + l / 2][i - 1]) return false;
			dp[j][i] = (4 - dp[j][i - 1] - dp[j + l / 2][i - 1]) % 3;
			// printf("%d %d %d\n", j, i, dp[j][i]);
		}
	}
	return true;
}

bool solve(int num, int p, int r, int s) {
	if (p < 0 || r < 0 || s < 0) {
		return false;
	}
	if (num == _pow[n]) {
		if (check()) {
			a[num] = '\0';
			puts(a);
			return true;
		}
		return false;
	}
	a[num] = 'P';
	if (solve(num + 1, p - 1, r, s)) return true;
	a[num] = 'R';
	if (solve(num + 1, p, r - 1, s)) return true;
	a[num] = 'S';
	if (solve(num + 1, p, r, s - 1)) return true;
	return false;
}
*/
bool check(int a, int b, int len) {
	for (int i = 0; i < _pow[len]; i++) {
		if (ans[a][len][i] > ans[b][len][i]) 
			return false;
	}
	return true;
}

void prepare() {
	ans[0][0][0] = 0;
	ans[1][0][0] = 1;
	ans[2][0][0] = 2;

	for (int i = 1; i <= 12; i++) {
		int a, b;
		
		if (check(0, 1, i - 1)) {
			a = 0; b = 1;
		} else {
			a = 1; b = 0;
		}
		for (int j = 0; j < _pow[i - 1]; j++) {
			ans[0][i][j] = ans[a][i - 1][j];
		}
		for (int j = 0; j < _pow[i - 1]; j++) {
			ans[0][i][_pow[i - 1] + j] = ans[b][i - 1][j];
		}
		num[0][i] = num[0][i - 1] + num[1][i - 1];

		if (check(1, 2, i - 1)) {
			a = 1; b = 2;
		} else {
			a = 2; b = 1;
		}
		for (int j = 0; j < _pow[i - 1]; j++) {
			ans[1][i][j] = ans[a][i - 1][j];
		}
		for (int j = 0; j < _pow[i - 1]; j++) {
			ans[1][i][_pow[i - 1] + j] = ans[b][i - 1][j];
		}
		num[1][i] = num[1][i - 1] + num[2][i - 1];

		if (check(0, 2, i - 1)) {
			a = 0; b = 2;
		} else {
			a = 2; b = 0;
		}
		for (int j = 0; j < _pow[i - 1]; j++) {
			ans[2][i][j] = ans[a][i - 1][j];
		}
		for (int j = 0; j < _pow[i - 1]; j++) {
			ans[2][i][_pow[i - 1] + j] = ans[b][i - 1][j];
		}
		num[2][i] = num[0][i - 1] + num[2][i - 1];
	}
}

bool solve() {
	int ans_id = -1;
	for (int i = 0; i < 3; i++) {
		int count[3] = {0, 0, 0};
		for (int j = 0; j < _pow[n]; j++)
			count[ans[i][n][j]] += 1;
		// printf("%d %d %d %d\n", i, count[0], count[1], count[2]);
		if (count[0] == P && count[1] == R && count[2] == S) {
			if (ans_id == -1 || check(i, ans_id, n)) {
				ans_id = i;
			}
		}
	}
	if (ans_id == -1) return false;
	char str[] = {'P', 'R', 'S'};
	for (int i = 0; i < _pow[n]; i++) {
		printf("%c", str[ans[ans_id][n][i]]);
	}
	puts("");
	return true;
}

int main() {
	_pow[0] = 1;
	for (int i = 1; i <= 12; i++) {
		_pow[i] = _pow[i - 1] * 2;
	}
	prepare();
	int ncas;
	scanf("%d", &ncas);
	for (int tcas = 1; tcas <= ncas; tcas++) {
		scanf("%d%d%d%d", &n, &R, &P, &S);
		printf("Case #%d: ", tcas);
		if (!solve()) {
			puts("IMPOSSIBLE");
		}
	}
	return 0;
}