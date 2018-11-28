#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <assert.h>
#define two(x) (1 << (x))
#define has(x, y) (((x) & (1 << (y))) != 0)

const int dx[] = {-1, -1, -1, 0, 0, 1, 1, 1};
const int dy[] = {-1, 0, 1, -1, 1, -1, 0, 1};

int m, n, c;
int solmine;
int solstart;
int num[7][7];
int vis;

void dfs(int start, int mine)
{
	int x = start / n;
	int y = start % n;
	for (int k = 0; k < 8; ++k) {
		int x2 = x + dx[k];
		int y2 = y + dy[k];
		if (x2 >= 0 && x2 < m && y2 >= 0 && y2 < n && !has(vis, x2 * n + y2) && !has(mine, x2 * n +y2)) {
			vis |= 1 << (x2 * n + y2);
			if (num[x2][y2] == 0) dfs(x2 * n + y2, mine);
		}
	}
}

bool check(int mine)
{
	memset(num, 0, sizeof(num));
	for (int i = 0; i < m; ++i) for (int j = 0; j < n; ++j) for (int k = 0; k < 8; ++k) {
		int x = i + dx[k], y = j + dy[k];
		if (x >= 0 && x < m && y >= 0 && y < n && has(mine, x * n + y)) ++num[i][j];
	}
	int start;
	// only 1 ground
	int countmine = 0;
	for (int i = 0; i < m * n; ++i) if (has(mine, i)) ++countmine;
	if (countmine == m * n - 1) {
		for (int i = 0; i < m * n; ++i) if (!has(mine, i)) {
			start = i;
			break;
		}
		solmine = mine;
		solstart = start;
		return true;
	}
	// multiple ground
	start = -1;
	for (int i = 0; i < m * n; ++i) if (num[i / n][i % n] == 0 && !has(mine, i)) {
		start = i;
		break;
	}
	if (start == -1) return false;
	vis = 0;
	vis |= 1 << start;
	dfs(start, mine);
	for (int i = 0; i < m * n; ++i) if (!has(mine, i) && !has(vis, i)) return false;
	solmine = mine;
	solstart = start;
	return true;
}

bool search(int mine, int depth, int remain)
{
	if (depth == m * n) return remain == 0 && check(mine);
	if (remain > 0) 
		if (search(mine | (1 << depth), depth + 1, remain - 1)) return true;
	return search(mine, depth + 1, remain);
}

void work()
{
	scanf("%d%d%d", &m, &n, &c);
	static int ttt = 0;
	printf("Case #%d:\n", ++ttt);
	if (search(0, 0, c)) {
		for (int i = 0; i < m; ++i) {
			for (int j = 0; j < n; ++j) 
				if (i * n + j == solstart)
					printf("c");
				else if (has(solmine, i * n + j))
					printf("*");
				else
					printf(".");
			printf("\n");
		}
	} else {
		printf("Impossible\n");
	}
}

int main()
{
	freopen("C-small-attempt5.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int T;
	scanf("%d", &T);
	while (T--) work();
}