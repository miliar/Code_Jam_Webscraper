#include <cstdio>

const int MAX = 6;

int n;
bool skill[MAX][MAX];
int zIndex[MAX][MAX], zFull;

void input() {
	scanf("%d", &n);

	zFull = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			char s[2];
			scanf("%1s", s);
			skill[i][j] = s[0] == '1';
			if (s[0] == '0') {
				zIndex[i][j] = zFull++;
			}
		}
	}
}

bool e[MAX][MAX];

bool check() {
	int rowSum[MAX];
	for (int i = 0; i < n; i++) {
		rowSum[i] = 0;
		for (int j = 0; j < n; j++) {
			rowSum[i] += e[i][j];
		}
	}

	for (int i = 0; i < n; i++) {
		int same = 0;
		for (int other = 0; other < n; other++) {
			int j;
			//check same
			for (j = 0; j < n; j++) {
				if (e[i][j] != e[other][j]) break;
			}
			if (j == n) {
				same++;
				continue;
			}
			//check diff
			for (j = 0; j < n; j++) {
				if (e[i][j]) {
					if (e[other][j]) return 0;
				}
			}
		}
		if (same != rowSum[i]) return 0;
	}

	return 1;
}

int solve() {
	int ans = MAX * MAX;
	for (int f = 0; f < (1 << zFull); f++) {
		int money = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (skill[i][j] == 1) e[i][j] = 1;
				else {
					bool nowE = (f >> zIndex[i][j]) & 1;
					e[i][j] = nowE;
					money += nowE;
				}
			}
		}

		if (check()) {
			if (ans > money)
				ans = money;
		}
	}

	return ans;
}

int main() {
	freopen("output.txt", "w", stdout);

	int numCase, nowCase;
	scanf("%d", &numCase);
	for (nowCase = 1; nowCase <= numCase; nowCase++) {
		input();

		printf("Case #%d: %d\n", nowCase, solve());
	}

	return 0;
}