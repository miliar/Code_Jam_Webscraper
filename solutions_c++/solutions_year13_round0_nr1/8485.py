#include <stdio.h>

int main()
{
	FILE *fin, *fout;
	int test, i, j, k;
	char arr[4][5], tmp;
	bool tbool;

	fin = fopen("A-small-attempt0.in", "r");
	fout = fopen("output.txt", "w");

	fscanf(fin, "%d", &test);

	for (i=0; i<test; i++)
	{
		bool empty = false;
		for (j = 0; j < 4; j++) {
			fscanf(fin, "%s", arr[j]);
			for (k = 0; k < 4; k ++)
			{
				if (arr[j][k] == '.')
				{
					empty = true;
					break;
				}
			}
		}
		// check row
		for (j = 0; j < 4; j++)
		{
			tmp = arr[j][0];
			if (arr[j][0] == '.')
				continue;
			tbool = true;
			for (k = 1; k < 4; k++)
			{
				if (tmp != arr[j][k] && arr[j][k] != 'T')
				{
					tbool = false;
					break;
				}
			}
			if (tbool) // tmp win
				goto here;
		}

		// check col
		for (j = 0; j < 4; j++)
		{		
			tmp = arr[0][j];
			if (tmp == '.')
				continue;
			tbool = true;
			for (k = 1; k < 4; k++)
			{
				if (tmp != arr[k][j] && arr[k][j] != 'T')
				{
					tbool = false;
					break;
				}
			}
			if (tbool) // tmp win
				goto here;
		}

		// check dia
		tmp = arr[0][0];
		if (tmp != '.') {
			tbool = true;
			for (j = 1; j < 4; j++)
			{
				if (tmp != arr[j][j] && arr[j][j] != 'T')
					{
						tbool = false;
						break;
					}
			}
			if (tbool) // tmp win
				goto here;
		}

		tmp = arr[0][3];
		if (tmp != '.') {
			tbool = true;
			for (j = 1; j < 4; j++)
			{
				if (tmp != arr[j][3-j] && arr[j][3-j] != 'T')
					{
						tbool = false;
						break;
					}
			}
			if (tbool) // tmp win
				goto here;
		}
		// check end. draw or not ended

		if (empty)
			fprintf(fout, "Case #%d: Game has not completed\n", i+1);
		else
			fprintf(fout, "Case #%d: Draw\n", i+1);
		continue;

here:
		fprintf(fout, "Case #%d: %c won\n", i+1, tmp);
		continue;

	}
	return 0;
}