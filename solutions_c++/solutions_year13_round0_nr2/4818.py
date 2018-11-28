#include <iostream>
#include <cstdio>
using namespace std;

int N, M;
int a[100][100];
int row[100], col[100];

void print_row() {
	int i;
	printf("row: ");
	for (i = 0; i < N; i++)
		printf("%d ", row[i]);
	printf("\n");
}

void print_col() {
	int i;
	printf("col: ");
	for (i = 0; i < M; i++)
		printf("%d ", col[i]);
	printf("\n");
}

int cut_row(int r, int h) {
	int i;
	for (i = 0; i < M; i++) {
		if (a[r][i] > h)
			return 0;
	}
	return 1;
}

int cut_col(int c, int h) {
	int i;
	for (i = 0; i < N; i++) {
		if (a[i][c] > h)
			return 0;
	}
	return 1;
}

int cut_grass() {
	int i, j;

	for (i = 0; i < N; i++) {
		for (j = 0; j < M; j++) {
			if (cut_row(i, a[i][j]) == 0 && cut_col(j, a[i][j]) == 0)
				return 0;
		}
	}
	return 1;
}

int main() {
	int T;
	int i, j, k;
	int yes;

	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	scanf("%d", &T);
	for (i = 0; i < T; i++) {
		scanf("%d %d", &N, &M);
		for (j = 0; j < N; j++) {
			for (k = 0; k < M; k++) {
				scanf("%d", &a[j][k]);
			}
		}
		// for (j = 0; j < N; j++) {
		// 	for (k = 0; k < M; k++) {
		// 		printf("%d", a[j][k]);
		// 	}
		// 	puts("");
		// }
		fflush(stdout);
		yes = cut_grass();
		printf("Case #%d: ", i+1);
		if (yes > 0)
			printf("YES\n");
		else
			printf("NO\n");
	}

	return 0;
}