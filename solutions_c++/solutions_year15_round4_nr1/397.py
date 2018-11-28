#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
using namespace std;

const int dx[4] = {-1, 0, 1, 0};
const int dy[4] = {0, 1, 0, -1};

int a[105][105];
int M, N;

int inside(int x, int y) {
	if (x < 1 || x > M) return 0;
	if (y < 1 || y > N) return 0;
	return 1;
}

int main() {
	char st[105];
	int testCaseNum;
	scanf("%d", &testCaseNum);
	for (int testCase = 1; testCase <= testCaseNum; ++testCase) {
		scanf("%d%d", &M, &N);
		for (int i = 1; i <= M; ++i) {
			scanf("%s", st + 1);
			for (int j = 1; j <= N; ++j) {
				if (st[j] == '.') a[i][j] = -1;
				if (st[j] == '^') a[i][j] = 0;
				if (st[j] == '>') a[i][j] = 1;
				if (st[j] == 'v') a[i][j] = 2;
				if (st[j] == '<') a[i][j] = 3;
			}
		}
		int ans = 0;
		int impossible = 0;
		for (int i = 1; i <= M; ++i)
			for (int j = 1; j <= N; ++j) {
				if (a[i][j] == -1) continue;
				int dangerSum = 0;
				for (int d = 0; d < 4; ++d) {
					int x = i, y = j;
					int danger = 1;
					while (true) {
						x += dx[d];
						y += dy[d];
						if (!inside(x, y)) break;
						if (a[x][y] != -1) {
							danger = 0;
							break;
						}
					}
					dangerSum += danger;
					if (a[i][j] == d && danger) ++ans;
				}
				if (dangerSum == 4) {
					impossible = 1;
				}
			}
		printf("Case #%d: ", testCase);
		if (impossible) {
			printf("IMPOSSIBLE\n");
		} else {
			printf("%d\n", ans);
		}
	}
}