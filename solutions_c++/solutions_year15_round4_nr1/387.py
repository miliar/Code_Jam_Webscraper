/*************************************************************************
    > File Name: A.cpp
    > Author: wmg_1001
    > Mail: wmg_1007@163.com 
    > Created Time: Sat 30 May 2015 10:25:45 PM CST
 ************************************************************************/

#include <iostream>
#include <fstream>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <ctime>
#include <iomanip>
#include <algorithm>
#include <deque>
#include <queue>
#include <map>
#include <set>
using namespace std;

const int maxn = 105;
const int dir_x[4] = {-1, 0, 1, 0};
const int dir_y[4] = {0, 1, 0, -1};

int G[maxn][maxn], n, m;

bool Get(int x, int y, int d) {
	do {
		x += dir_x[d];
		y += dir_y[d];
		if (x < 0 || x >= n || y < 0 || y >= m) break;
		if (G[x][y] >= 0) return true;
	} while (true);
	return false;
}

void work() {
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			char ch = getchar();
			while (ch != '.' && ch != 'v' && ch != '^' && ch != '>' && ch != '<')
				ch = getchar();
			if (ch == '.') G[i][j] = -1;
			if (ch == 'v') G[i][j] = 2;
			if (ch == '^') G[i][j] = 0;
			if (ch == '<') G[i][j] = 3;
			if (ch == '>') G[i][j] = 1;
		}
	}
	int res = 0;
	bool succ;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (G[i][j] == -1) continue;
			succ = Get(i, j, G[i][j]);
			if (!succ) res++;
			for (int k = 0; k < 4; k++) {
				succ |= Get(i, j, k);
			}
			if (!succ) {
				cout << "IMPOSSIBLE" << endl;
				return ;
			}
		}
	}
	cout << res << endl;
}

int main() {
	int T, case_T = 0;
	cin >> T;
	while (T--) {
		case_T++;
		cout << "Case #" << case_T << ": ";
		work();
	}
	return 0;
}