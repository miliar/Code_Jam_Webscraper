#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

const int MAX = 100;
int board[MAX][MAX];
int tt, n, m;

bool valid() {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			bool valid = true;
			for (int k = 0; k < n && valid; k++) {
				if (board[k][j] > board[i][j]) {
					valid = false;
				}
			}
			if (valid) continue;
			valid = true;
			for (int k = 0; k < m && valid; k++) {
				if (board[i][k] > board[i][j]) {
					valid = false;
				}
			}
			if (!valid) return false;
		}
	}
	return true;
}

int main() {
	scanf("%d", &tt);
	for (int t = 1; t <= tt; t++) {
		scanf("%d %d", &n, &m);
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				scanf("%d", &board[i][j]);
			}
		}
		printf("Case #%d: %s\n", t, valid() ? "YES" : "NO");
	}

	return 0;
}