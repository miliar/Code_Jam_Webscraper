#include <stdio.h>

int main()
{		
	FILE *in;
	FILE *out;

	in = fopen("B-large.in", "r");
	out = fopen("output-B-large.txt", "w");

	int testCases;
	fscanf(in, "%d\n", &testCases);
	for (int t = 0; t < testCases; t++){
		int a, b;
		// Read the goal table;
		fscanf(in, "%d %d\n", &a, &b);
		int goal[a][b];
		for (int i = 0; i < a; i++) {
			for (int j = 0; j < b; j++) {
				fscanf(in, "%d ", &goal[i][j]);
			}
			fscanf(in, "\n");
		}
		// Init the start table;
		char current[a][b];
		for (int i = 0; i < a; i++) {
			for (int j = 0; j < b; j++) {
				current[i][j] = 100;
			}
		}

		for (int i = 0; i < a; i++) {
			int sormax = goal[i][0];
			for (int j = 1; j < b; j++) {
				if (goal[i][j] > sormax) sormax = goal[i][j];
			}
			for (int j = 0; j < b; j++) {
				if (current[i][j] > sormax) current[i][j] = sormax;
			}
		}

		for (int j = 0; j < b; j++) {
			int oszlopMax = goal[0][j];
			for (int i = 1; i < a; i++) {
				if (goal[i][j] > oszlopMax) oszlopMax = goal[i][j];
			}
			for (int i = 0; i < a; i++) {
				if (current[i][j] > oszlopMax) current[i][j] = oszlopMax;
			}
		}

		int result = 1;
		for (int i = 0; i < a; i++) {
			for (int j = 0; j < b; j++) {
				if (goal[i][j] != current[i][j]) result = 0;
			}
		}

		fprintf(out, "Case #%d: %s\n", (t+1), (result == 1) ? "YES" : "NO");
	}

	fclose(in);
	fclose(out);

	return 0;
}
