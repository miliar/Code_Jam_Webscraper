#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
int TestCase, N, M, K, A[10][10];
int C[33554500];

bool in_range(int x, int y)
{
	return 1 <= x && x <= N && 1 <= y && y <= M;
}

void DFS(int x, int y)
{
	if (!in_range(x, y)) {
		return;
	}
	if (A[x][y] != 0) {
		return;
	}
	A[x][y] = -2;
	for (int dx = -1; dx <= 1; dx ++) {
		for (int dy = -1; dy <= 1; dy ++) {
			DFS(x + dx, y + dy);
		}
	}
}

bool Check()
{
	if (K + 1 == N * M) {
		return true;
	}
	for (int i = 1; i <= N; i ++) {
		for (int j = 1; j <= M; j ++)
		if (A[i][j] == -1) {
			for (int dx = -1; dx <= 1; dx ++) {
				for (int dy = -1; dy <= 1; dy ++)
				if (in_range(i + dx, j + dy) && A[i + dx][j + dy] == 0) {
					A[i + dx][j + dy] = 1;
				}
			}
		}
	}
	for (int i = 1; i <= N; i ++) {
		for (int j = 1; j <= M; j ++)
		if (A[i][j] == 1) {
			bool flag = false;
			for (int dx = -1; dx <= 1; dx ++) {
				for (int dy = -1; dy <= 1; dy ++)
				if (in_range(i + dx, j + dy) && A[i + dx][j + dy] == 0) {
					flag = true;
				}
			}
			if (!flag) {
				return false;
			}
		}
	}
	int Cnt = 0;
	for (int i = 1; i <= N; i ++) {
		for (int j = 1; j <= M; j ++)
		if (A[i][j] == 0) {
			DFS(i, j);
			Cnt ++;
		}
	}
	return Cnt == 1;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	for (int i = 0; i < 1 << 25; i ++) {
		for (int j = 0; j < 25; j ++) {
			C[i] += (i >> j) & 1;
		}
	}
	scanf("%d", &TestCase);
	for (int Case = 1; Case <= TestCase; Case ++) {
		scanf("%d%d%d", &N, &M, &K);
		printf("Case #%d:\n", Case);
		int NM = N * M;
		bool Flag = false;
		for (int i = 0; i < 1 << NM; i ++)
		if (C[i] == K) {
			memset(A, 0, sizeof(A));
			for (int j = 0; j < NM; j ++)
			if ((i >> j) & 1) {
				int x = j / M;
				int y = j % M;
				A[x + 1][y + 1] = -1;
			}
			if (Check()) {
				for (int i = 1; i <= N; i ++) {
					for (int j = 1; j <= M; j ++) {
						if (A[i][j] == -1) {
							printf("*");
						} else if (A[i][j] == -2) {
							if (Flag) {
								printf(".");
							} else {
								printf("c");
								Flag = true;
							}
						} else {
							if (K + 1 == NM) {
								printf("c");
								Flag = true;
							} else {
								printf(".");
							}
						}
					}
					printf("\n");
				}
				break;
			}
		}
		if (!Flag) {
			printf("Impossible\n");
		}
	}
	return 0;
}
