#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cmath>
#include <algorithm>
#include <assert.h>
#include <memory.h>
#include <string.h>
#include <complex>
#include <queue>
#include <cstdlib>
#include <ctime>
using namespace std;

#define ll long long
#define pb push_back
#define mp make_pair
#define sz(x) (int)(x).size()

int mas[100];
int vis[100][100][4];

int getid(int r, int c, int d, int R, int C) {
	if(r == 0 && d == 0) return c;
	if(c == C - 1 && d == 3) return r + (C);
	if(r == R - 1 && d == 2) return C - 1 - c + (C + R);
	if(c == 0 && d == 1) return R - 1 - r + (C + R + C);
	return -1;
}

int matr[100][100];

void dfs(int r, int c, int d, int id, vector<string> &matrix) {
	int R = sz(matrix);
	int C = sz(matrix[0]);
	if(r < 0 || c < 0 || r >= R || c >= C) return;
	if(vis[r][c][d] != -1) return;
	vis[r][c][d] = id;
	// вверх
	if(d == 0) dfs(r-1, c, 2, id, matrix);
	// вниз
	if(d == 2) dfs(r+1, c, 0, id, matrix);
	// влево
	if(d == 1) dfs(r, c-1, 3, id, matrix);
	// вправо
	if(d == 3) dfs(r, c+1, 1, id, matrix);

	if(matrix[r][c] == '/') {
		if(d == 0 || d == 1) dfs(r, c, 1-d, id, matrix);
		if(d == 2 || d == 3) dfs(r, c, 5-d, id, matrix); 
	}
	else {
		if(d == 1 || d == 2) dfs(r, c, 3-d, id, matrix);
		if(d == 0 || d == 3) dfs(r, c, 3-d, id, matrix); 
	}
}

bool check(int N, vector<string> &matrix) {
	int R = sz(matrix);
	int C = sz(matrix[0]);
	for(int i = 0; i < R; i++)
		for(int j = 0; j < C; j++) 
			for(int k = 0; k < 4; k++) 
				vis[i][j][k] = -1;
	for(int i = 0; i < N; i++)
		for(int j = 0; j < N; j++)
			matr[i][j] = false;
	for(int i = 0; i < R; i++) {
		for(int j = 0; j < C; j++) {
			for(int k = 0; k < 4; k++) {
				if(vis[i][j][k] == -1) {
					int id = getid(i, j, k, R, C);
					if(id != -1) dfs(i, j, k, id, matrix);
				}
			}
		}
	}
	for(int i = 0; i < R; i++) {
		for(int j = 0; j < C; j++) {
			for(int k = 0; k < 4; k++) {
				int id = getid(i, j, k, R, C);
				if(id != -1 && vis[i][j][k] != -1 && id != vis[i][j][k]) {
					matr[id][vis[i][j][k]] = true;
					matr[vis[i][j][k]][id] = true;
				}
			}
		}
	}

	for(int i = 0; i < N; i += 2) {
		if(matr[mas[i]][mas[i+1]] && matr[mas[i+1]][mas[i]]) {}
		else return false;
	}
	for(int i = 0; i < N; i++) {
		int sum = 0;
		for(int j = 0; j < N; j++) sum += matr[i][j];
		if(sum != 1) return false;
	}
	return true;
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	int T;
	scanf("%d", &T);
	for(int test = 1; test <= T; test++) {
		printf("Case #%d:\n", test);
		int R, C;
		scanf("%d %d", &R, &C);
		int N = 2 * R + 2 * C;
		for(int i = 0; i < N; i++) scanf("%d", &mas[i]), mas[i]--;
		bool ok = false;
		for(int mask = 0; mask < (1 << (R * C)); mask++) {
			vector<string> matrix(R);
			int bit = 0;
			for(int i = 0; i < R; i++) {
				for(int j = 0; j < C; j++) {
					if(mask & (1 << bit)) matrix[i] += "/";
					else matrix[i] += "\\";
					bit++;
				}
			}
			if(check(N, matrix)) {
				ok = true;
				for(int i = 0; i < R; i++) cout << matrix[i] << endl;
				break;
			}
		}
		if(!ok) cout << "IMPOSSIBLE" << endl;
	}

	return 0;
}