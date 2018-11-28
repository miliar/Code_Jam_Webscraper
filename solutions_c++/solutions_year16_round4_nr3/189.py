#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<queue>
#include<stack>
#include<map>
#include<vector>
#include<string>
using namespace std;

int mirror[20][20], a[100], b[100], n, m, N, num[100][100][100], dr[100];
pair<int, int> pos[100];

void print() {
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			if (mirror[i][j] == 0) printf("/");
			else printf("\\");
		}
		printf("\n");
	}
}

void placemirror(int x) {
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			mirror[i][j] = (x >> (i*m+j)) & 1;
		}
	}
}

int light(int x, int y, int direction) {
	if (x < 0) {
		//printf("%d %d %d\n", x, y, direction);
		return num[x+1][y][0];
	}
	if (y < 0) return num[x][y+1][3];
	if (x >= n) return num[x-1][y][2];
	if (y >= m) return num[x][y-1][1];
	if (mirror[x][y] == 0) {
		if (direction == 0) return light(x, y-1, 1);
		if (direction == 3) return light(x-1, y, 2);
		if (direction == 1) return light(x+1, y, 0);
		if (direction == 2) return light(x, y+1, 3);
	} else {
		if (direction == 0) return light(x, y+1, 3);
		if (direction == 3) return light(x+1, y, 0);
		if (direction == 1) return light(x-1, y, 2);
		if (direction == 2) return light(x, y-1, 1);
	}
}

bool check(int x, int y) {
	return y == light(pos[x].first, pos[x].second, dr[x]);
}

void work() {
	scanf("%d%d", &n, &m);
	for (int i = 0; i < (n+m); ++i) {
		scanf("%d%d", &a[i], &b[i]);
	}
	int ct = 0;
	memset(num, 0, sizeof(num));
	for (int i = 0; i < m; ++i) {
		num[0][i][0] = ++ct;
		dr[ct] = 0;
		pos[ct] = make_pair(0, i);
	}
	for (int i = 0; i < n; ++i) {
		num[i][m-1][1] = ++ct;
		dr[ct] = 1;
		pos[ct] = make_pair(i, m-1);
	}
	for (int i = m - 1; i >= 0; --i) {
		num[n-1][i][2] = ++ct;
		dr[ct] = 2;
		pos[ct] = make_pair(n-1, i);
	}
	for (int i = n - 1; i >= 0; --i) {
		num[i][0][3] = ++ct;
		dr[ct] = 3;
		pos[ct] = make_pair(i, 0);
	}
	/*
	for (int i = 1; i <= ct; ++i) {
		printf("%d %d\n", pos[i].first, pos[i].second);
	}
	*/
	N = (1 << (n*m));
	for (int i = 0; i < N; ++i) {
		placemirror(i);
		bool flag = true;
		for (int j = 0; j < (n+m); ++j) {
			if (!check(a[j], b[j])) {
				flag = false;
				break;
			}
		}
		if (flag) {
			print();
			return;
		}
	}
	printf("IMPOSSIBLE\n");
}

int main() {
	freopen("C-small-attempt1.in", "r", stdin);
	int TestCase;
	scanf("%d", &TestCase);
	for (int i = 1; i <= TestCase; ++i) {
		printf("Case #%d:\n", i);
		work();
	}
	
	return 0;
}