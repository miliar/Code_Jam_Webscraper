#include <stdio.h>
#include <string.h>

int n, m;
int used[100][100];
int M[100][100];

void checkR (int r) {
	int i, j, mx;
	mx = M[r][0];
	for (i = 1; i < m; i++)	
		if (M[r][i] < mx)	used[r][i]--;
		else if (M[r][i] > mx) {
			for (j = 0; j < i; j++)
				if (M[r][j] == mx)	used[r][j]--;
			mx = M[r][i];
		}
}

void checkC (int c) {
	int i, j, mx;
	mx = M[0][c];
	for (i = 1; i < n; i++)	
		if (M[i][c] < mx)	used[i][c]--;
		else if (M[i][c] > mx) {
			for (j = 0; j < i; j++)
				if (M[j][c] == mx)	used[j][c]--;
			mx = M[i][c];
		}
}

int main (void) {
	int i, T, c;
	int j;
	bool ok;
	scanf ("%d", &T);
	for (c = 1; c <= T; c++) {
		printf ("Case #%d: ", c);
		memset (used, 0, sizeof used);
		scanf ("%d%d", &n, &m);
		for (i = 0; i < n; i++)
			for (j = 0; j < m; j++) {
				scanf ("%d", &M[i][j]);
				used[i][j] = 2;
			}

		for (i = 0; i < n; i++)	checkR(i);
		for (j = 0; j < m; j++)	checkC(j);
/*		for (i = 0; i < n; i++) {
			for (j = 0; j < m; j++)
				printf ("%d ", used[i][j]);
			printf ("\n");
		} */
		ok = 1;
		for (i = 0; i < n; i++)
			for (j = 0; j < m; j++)
				if (!used[i][j])	ok = 0;
		if (ok)	printf ("YES\n");
		else	printf ("NO\n");
	}
	return 0;
}
