#include <stdio.h>
#include <string.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

int n, m;

char mat[120][120];



bool isOK(int r, int c, char ch) {
	int cnt = 0;
	if (ch == '^') {
		for (int i = 0; i < r; i++) {
			if (mat[i][c] != '.') cnt++;
		}
	} else if (ch == 'v') {
		for (int i = r + 1; i < n; i++) {
			if (mat[i][c] != '.') cnt++;
		}
	} else if (ch == '<') {
		for (int j = 0; j < c; j++) {
			if (mat[r][j] != '.') cnt++;
		}
	} else if (ch == '>') {
		for (int j = c + 1; j < m; j++) {
			if (mat[r][j] != '.') cnt++;
		}
	}
	return cnt > 0;
}

bool isAdj(int r, int c, char ch) {
	if (ch == '^')
		return isOK(r, c, 'v') || isOK(r, c, '<') || isOK(r, c, '>');
	if (ch == 'v')
		return isOK(r, c, '^') || isOK(r, c, '<') || isOK(r, c, '>');
	if (ch == '<')
		return isOK(r, c, 'v') || isOK(r, c, '^') || isOK(r, c, '>');
	if (ch == '>')
		return isOK(r, c, 'v') || isOK(r, c, '<') || isOK(r, c, '^');
}

int solve() {
	cin >> n >> m;
	for (int i = 0; i < n; i++)
		scanf("%s", mat[i]);
	int ret = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (mat[i][j] == '.') continue;
			if (!isOK(i, j, mat[i][j])) {
				if (isAdj(i, j, mat[i][j]))
					ret++;
				else
					return -1;
			}
		}
	}
	return ret;
}

int main() {
	int t;
	cin >> t;
	for (int cas = 1; cas <= t; cas++) {
		int ret = solve();
		printf("Case #%d: ", cas);
		if (ret >= 0)
			printf("%d\n", ret);
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}