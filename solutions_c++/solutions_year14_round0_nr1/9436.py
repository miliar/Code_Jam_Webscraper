#include <stdio.h>
#include <stdlib.h>

void main()
{
	FILE *f, *f1;
	fopen_s(&f, "input.in", "r");
	fopen_s(&f1, "output.out", "w");
	int t, i, j, k, count, answer, x, a[16], b[4];
	fscanf_s(f, "%d", &t);
	for (i = 0; i < t; i++)
	{
		count = 0;
		fscanf_s(f, "%d", &answer);
		for (j = 0; j < 16; j++)
			fscanf_s(f, "%d", &a[j]);
		for (j = (answer - 1) * 4; j < answer * 4; j++)
			b[j % 4] = a[j];
		fscanf_s(f, "%d", &answer);
		for (j = 0; j < 16; j++)
			fscanf_s(f, "%d", &a[j]);
		for (j = (answer - 1) * 4; j < answer * 4; j++)
		for (k = 0; k < 4; k++)
		if (a[j] == b[k])
		{
			x = a[j];
			count++;
		}
		fprintf(f1, "Case #%d: ", i+1);
		if (count == 1)
			fprintf(f1, "%d", x);
		else
		{
			if (count > 1)
				fprintf(f1, "Bad magician!");
			else
				fprintf(f1, "Volunteer cheated!");
		}
		if (i < t - 1)
			fprintf(f1, "\n");
	}
	_fcloseall();
}