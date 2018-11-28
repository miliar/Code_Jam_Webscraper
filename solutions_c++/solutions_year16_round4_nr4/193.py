#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int N = 10 + 7;
const int INF = 1e9 + 7;

int n;


int op[N][N];
int cur[N][N];
int answer;

bool go(int person, int machine) {
	int cnt = 0;
	for (int i = 0; i < n; i++) {
		if (~person >> i & 1) {
			for (int j = 0; j < n; j++) {
				if ((~machine >> j & 1) && cur[i][j]) {
					cnt++;
					if (go(person | (1 << i), machine | (1 << j))) {
						return true;
					}
				}
			}
		}
	}
	if (cnt == 0 && person != (1 << n) - 1) {
		return true;
	} else {
		return false;
	}
}

bool check() {
	if (go(0, 0)) {
		return false;
	} else {
		return true;
	}
}

void dfs(int i, int j, int cost) {
	//cout << i << " " << j << " " << n << endl;
	if (cost > answer) {
		return ;
	}

	if (i == n) {
		if (check()) {
			answer = min(answer, cost);
		}
		return ;
	} else if (j == n) {
		dfs(i + 1, 0, cost);
		return ;
	}

	if (op[i][j] == 0) {
		cur[i][j] = 0;
		dfs(i, j + 1, cost);
		cur[i][j] = 1;
		dfs(i, j + 1, cost + 1);
	} else {
		cur[i][j] = op[i][j];
		dfs(i, j + 1, cost);
	}
}

int main() {
	int test;
	scanf("%d", &test);
	while (test--) {
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			static char s[11];
			scanf("%s", s);
			for (int j = 0; j < n; j++) {
				if (s[j] == '1') {
					op[i][j] = 1;
				} else {
					op[i][j] = 0;
				}
			}
		}

		answer = INF;
		dfs(0, 0, 0);

		static int testCount = 0;
		printf("Case #%d: %d\n", ++testCount, answer);

	}
	return 0;
}
