#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <queue>
#include <string>
#include <cstdio>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
using namespace std;
int R, C, N, A[30], ID[30][30], P[50];
int Ret[30][30], B[30][30];
bool bRet;

int get_id(int x, int y, int d)
{
	if (x < 1 || x > R || y < 1 || y > C) return ID[x][y];
	if (d == 0) {
		if (B[x][y] == 0) return get_id(x, y - 1, 1);
		if (B[x][y] == 1) return get_id(x, y + 1, 3);
	} else if (d == 1) {
		if (B[x][y] == 0) return get_id(x + 1, y, 0);
		if (B[x][y] == 1) return get_id(x - 1, y, 2);
	} else if (d == 2) {
		if (B[x][y] == 0) return get_id(x, y + 1, 3);
		if (B[x][y] == 1) return get_id(x, y - 1, 1);
	} else if (d == 3) {
		if (B[x][y] == 0) return get_id(x - 1, y, 2);
		if (B[x][y] == 1) return get_id(x + 1, y, 0);
	}
	return -1;
}

bool check()
{
	/*
	for (int i = 1; i <= R; i ++) {
		for (int j = 1; j <= C; j ++) {
			if (B[i][j] == 0) printf("/");
				else printf("\\");
		}
		printf("\n");
	}
	*/
	for (int i = 1; i <= C; i ++) {
		int id = get_id(1, i, 0);
	//	printf("%d %d\n", ID[0][i], id);
		if (id != P[ID[0][i]]) return false;
	}
	for (int i = 1; i <= R; i ++) {
		int id = get_id(i, C, 1);
		if (id != P[ID[i][C+1]]) return false;
	}
	for (int i = C; i >= 1; i --) {
		int id = get_id(R, i, 2);
		if (id != P[ID[R+1][i]]) return false;
	}
	for (int i = R; i >= 1; i --) {
		int id = get_id(i, 1, 3);
		if (id != P[ID[i][0]]) return false;
	}
	return true;
}

void search(int x, int y)
{
	if (bRet) return;
	if (x == R + 1) {
		if (check()) {
			bRet = true;
			memcpy(Ret, B, sizeof(B));
		}
	} else {
		if (y == C + 1) {
			search(x + 1, 1);
		} else {
			B[x][y] = 0;
			search(x, y + 1);
			B[x][y] = 1;
			search(x, y + 1);
		}
	}
}

int main()
{
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int nCase = 0, test;
	scanf("%d", &test);
	while (test --) {
		scanf("%d%d", &R, &C);
		for (int i = 0; i < 2 * (R + C); i ++) {
			scanf("%d", &A[i]);
		}
		for (int i = 0; i < 2 * (R + C); i += 2) {
			P[A[i]] = A[i + 1];
			P[A[i + 1]] = A[i];
		}
		N = 1;
		for (int i = 1; i <= C; i ++) ID[0][i] = N ++;
		for (int i = 1; i <= R; i ++) ID[i][C+1] = N ++;
		for (int i = C; i >= 1; i --) ID[R+1][i] = N ++;
		for (int i = R; i >= 1; i --) ID[i][0] = N ++;
		bRet = false;
		search(1, 1);
		printf("Case #%d:\n", ++ nCase);
		if (bRet) {
			for (int i = 1; i <= R; i ++) {
				for (int j = 1; j <= C; j ++) {
					if (Ret[i][j] == 0) printf("/");
						else printf("\\");
				}
				printf("\n");
			}
		} else {
			printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}
