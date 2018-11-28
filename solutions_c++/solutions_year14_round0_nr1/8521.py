#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(int argc, char* argv[])
{
	FILE *f = fopen((argc > 1 ? argv[1] : "in.txt"), "r");
	FILE *g = fopen("out.txt", "w");
	int t;

	fscanf(f, "%d\n", &t);
	for (int test = 0; test < t; test++) {
		int a[2][4][4];
		int r[2];
		for (int i = 0; i < 2; i++) {
			fscanf(f, "%d\n", &r[i]);
			r[i]--;
			for (int j = 0; j < 4; j++)
				fscanf(f, "%d %d %d %d\n", &a[i][j][0], &a[i][j][1], &a[i][j][2], &a[i][j][3]);
		}

		int cnt = 0, candidate;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (a[0][r[0]][i] == a[1][r[1]][j]) {
					candidate = a[0][r[0]][i];
					cnt++;
				}
			}
		}

		if (cnt == 0)
			fprintf(g, "Case #%d: Volunteer cheated!\n", test + 1);
		else if (cnt == 1)
			fprintf(g, "Case #%d: %d\n", test + 1, candidate);
		else
			fprintf(g, "Case #%d: Bad magician!\n", test + 1);
	}
	fclose(f);
	fclose(g);
	return 0;
}

