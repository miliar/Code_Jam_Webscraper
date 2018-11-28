#include <stdio.h>
int main()
{
	int card1[5][5];
	int card2[5][5];
	int i, j;
	int testCase;
	int selectedRow1, selectedRow2;
	int cnt = 0;
	int ans;
	FILE* input = fopen("A-small-attempt().txt", "r");
	FILE* output = fopen("output.out", "w");
	fscanf(input,"%d", &testCase);


	for (int index = 1; index <= testCase; index++)
	{
		fscanf(input,"%d", &selectedRow1);
		for (i = 1; i <= 4; i++)
		{
			for (j = 1; j <= 4; j++)
			{
				fscanf(input,"%d", &card1[i][j]);
			}
		}

		fscanf(input,"%d", &selectedRow2);

		for (i = 1; i <= 4; i++)
		{
			for (j = 1; j <= 4; j++)
			{
				fscanf(input,"%d", &card2[i][j]);
			}
		}

		for (i = 1; i <= 4; i++)
		{
			for (j = 1; j <= 4; j++)
			{
				if (card1[selectedRow1][i] == card2[selectedRow2][j])
				{
					cnt++;
					ans = i;
				}
			}
		}

		if (cnt == 0)
			fprintf(output,"Case #%d: Volunteer cheated!\n", index);
		else if (cnt == 1)
		{
			fprintf(output,"Case #%d: %d\n", index, card1[selectedRow1][ans]);
		}

		else
			fprintf(output,"Case #%d: Bad magician!\n", index);

		cnt = 0;
	}

	fclose(input);
	fclose(output);
}