#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int matrix[5][5];
bool used[5][5];
int N, M;


int CNT(int r, int c) {
	if (r < 0 || r >= N || c < 0 || c >= M) return 0;
	return matrix[r][c];
}

int cnt (int r, int c) {
	if (r < 0 || r >= N || c < 0 || c >= M) return 0;
	if (matrix[r][c] == 1) return 0;
	if (used[r][c]) return 0;
	used[r][c] = true;
	if (CNT(r + 1, c) + CNT(r - 1, c) + CNT(r, c - 1) + CNT(r, c + 1) + CNT(r - 1, c - 1) + CNT(r - 1, c + 1) + CNT(r + 1, c - 1) + CNT(r + 1, c + 1) != 0) return 1;
	return 1 + cnt(r + 1, c) + cnt(r - 1, c) + cnt(r, c - 1) + cnt(r, c + 1) + cnt(r - 1, c - 1) + cnt(r - 1, c + 1) + cnt(r + 1, c - 1) + cnt(r + 1, c + 1);
}

void solve(int r, int c, int m) {
	if (m == r * c - 1) {
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++)
				if (i == 0 && j == 0) printf ("c"); else printf ("*");
			printf ("\n");
		}
		return;
	}
	if (r == 1) {
		printf ("c");
		for (int i = 0; i < r * c - m - 1; i++)
			printf (".");
		for (int i = 0; i < m; i++)
			printf ("*");
		printf ("\n");
		return;
	}
	if (c == 1) {
		printf ("c\n");
		for (int i = 0; i < r * c - m - 1; i++)
			printf (".\n");
		for (int i = 0; i < m; i++)
			printf ("*\n");
		return;
	}
	N = r;
	M = c;
	for (int i = 0; i < r; i++)
		for (int j = 0; j < c; j++)
			used[i][j] = false;
	for (int mask = 0; mask < (1 << (r * c)); mask++) {
		int q = mask;
		int CNT1 = 0;
		for (int i = 0; i < r; i++)
			for (int j = 0; j < c; j++) {
				matrix[i][j] = q % 2;
				CNT1 += (q % 2);
				q /= 2;
			}
		if (CNT1 != m) continue;
		for (int i = 0; i < r; i++)
			for (int j = 0; j < c; j++) {
				if (CNT(i + 1, j) + CNT(i - 1, j) + CNT(i, j - 1) + CNT(i, j + 1) + CNT(i - 1, j - 1) + CNT(i - 1, j + 1) + CNT(i + 1, j - 1) + CNT(i + 1, j + 1) == 0) {
					for (int R = 0; R < r; R++)
						for (int C = 0; C < c; C++)
							used[R][C] = false;
					int Q = cnt(i, j);
					if (Q == r * c - m) {
						for (int R = 0; R < r; R++) {
							for (int C = 0; C < c; C++) {
								if (R == i && C == j) printf ("c"); else if (matrix[R][C] == 0) printf ("."); else printf ("*");
							}
							printf ("\n");
						}
						return;
					}
				}
			}
	}
	printf ("Impossible\n");
}

int main () {
	int t;
	scanf ("%d", &t);
	for (int test = 0; test < t; test++) {
		int r, c, m;
		scanf ("%d%d%d", &r, &c, &m);
		printf ("Case #%d:\n", test + 1);
		solve(r, c, m);
	}
}

