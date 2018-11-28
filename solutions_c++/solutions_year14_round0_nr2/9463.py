#include <stdio.h>
#include <stdlib.h>

void main()
{
	FILE *file, *file1;
	fopen_s(&file, "input.in", "r");
	fopen_s(&file1, "output.out", "w");
	int testsCount, i, j;
	double a, b, c, f, x, gain, farmsCount;
	fscanf_s(file, "%d", &testsCount);
	for (i = 0; i < testsCount; i++)
	{
		gain = 2;
		farmsCount = 0;
		fscanf_s(file, "%lf%lf%lf", &c, &f, &x);
		a = x / gain;
		b = (c / gain) + x / (gain + f);
		while (a>b)
		{
			a = b;
			b = 0;
			farmsCount++;
			for (j = 0; j < farmsCount + 1; j++)
				b += c / (gain + j*f);
			b += x / (gain + j*f);
		}
		fprintf(file1, "Case #%d: %.7lf", i + 1, a);
		if (i < testsCount - 1)
			fprintf(file1, "\n");
	}
	_fcloseall();
}