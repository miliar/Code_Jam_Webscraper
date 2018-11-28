#include <stdio.h>

int main()
{
	int t, i, j;

	FILE *fin, *fout;

	fin = fopen("input.txt", "r");
	fout = fopen("output.txt", "w");

	fscanf(fin, "%d", &t);
	for (i = 1; i <= t; i++)
	{
		int a, b, c;

		fscanf(fin, "%d %d %d", &a, &b, &c);

		if (a >= 7)
		{
			fprintf(fout, "Case #%d: RICHARD\n", i);
			continue;
		}

		if (a == 1) fprintf(fout, "Case #%d: GABRIEL\n", i);
		else if (a == 2)
		{
			if ((b*c) % 2 == 0) fprintf(fout, "Case #%d: GABRIEL\n", i);
			else fprintf(fout, "Case #%d: RICHARD\n", i);
		}
		else if (a == 3)
		{
			if ((b*c) % 3 == 0 && b > 1 && c > 1) fprintf(fout, "Case #%d: GABRIEL\n", i);
			else fprintf(fout, "Case #%d: RICHARD\n", i);
		}
		else if (a == 4)
		{
			if ((b*c) % 4 == 0 && b >= 3 && c >= 3) fprintf(fout, "Case #%d: GABRIEL\n", i);
			else fprintf(fout, "Case #%d: RICHARD\n", i);
		}
	}
	fclose(fin);
	fclose(fout);

	return 0;
}