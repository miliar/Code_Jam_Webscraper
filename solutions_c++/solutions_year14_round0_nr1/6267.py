#include <iostream>
#include <stdio.h>
using namespace std;

using namespace std;

int main()
{
	int cases, counter, row1, row2;
	int result[100];
	int grid[4][4];
	int compare[4][2];
	bool inUseGrid[16];
	bool incomplete = true;

	counter = 0; 
	cases = 0;
	row1 = 0;
	row2 = 0;
	errno_t err;

	FILE* hfile;
	err = fopen_s(&hfile, "input.txt", "rb");

	if (err == 0)
	{
		printf("The file 'input.txt' was opened\n");
	}
	else
	{
		printf("The file 'input.txt' was not opened\n");
		system("pause");
		exit(15);
	}

	for (int i = 0; i < 16; i++)
	{
		inUseGrid[i] = false;
	}

	while (cases < 1 || cases > 100)
	{
		fscanf_s(hfile, "%d", &cases);
	}

	while (counter < cases)
	{
		row1 = 0;
		row2 = 0;

		while (row1 < 1 || row1 > 4)
		{
			fscanf_s(hfile, "%d", &row1);
		}

		incomplete = true;
		while (incomplete)
		{
			incomplete = false;

			for (int i = 0; i < 16; i++)
				inUseGrid[i] = false;

			for (int i = 0; i < 4; i++)
			{
				fscanf_s(hfile, "%d %d %d %d", &grid[0][i], &grid[1][i], &grid[2][i], &grid[3][i]);
			}

			for (int j = 0; j < 16; j++)
			{
				int index = grid[j % 4][j / 4];
				if (index >= 1 && index <= 16)
				{
					inUseGrid[index - 1] = true;
				}
			}
			
			for (int i = 0; i < 16; i++)
				if (inUseGrid[i] == false)
					incomplete = true;
		}
		for (int i = 0; i < 4; i++)
			compare[i][0] = grid[i][row1 - 1];

		while (row2 < 1 || row2 > 4)
		{
			fscanf_s(hfile, "%d", &row2);
		}

		incomplete = true;
		while (incomplete)
		{
			incomplete = false;

			for (int i = 0; i < 16; i++)
				inUseGrid[i] = false;

			for (int i = 0; i < 4; i++)
			{
				fscanf_s(hfile, "%d %d %d %d", &grid[0][i], &grid[1][i], &grid[2][i], &grid[3][i]);
			}

			for (int j = 0; j < 16; j++)
			{
				int index = grid[j % 4][j / 4];
				if (index >= 1 && index <= 16)
					inUseGrid[index - 1] = true;
			}

			for (int i = 0; i < 16; i++)
			if (inUseGrid[i] == false)
				incomplete = true;
		}
		for (int i = 0; i < 4; i++)
			compare[i][1] = grid[i][row2 - 1];

		int cmp = 0, len = 0;

		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if (compare[i][0] == compare[j][1])
				{
					len++;
					cmp = compare[i][0];
				}
			}
		}

		switch (len)
		{
			case 0:
				result[counter] = 0; 
				break;
			case 1:
				result[counter] = cmp;
				break;
			default:
				result[counter] = -1;
				break;
		}
		counter += 1;
	}

	fclose(hfile);

	fopen_s(&hfile, "output.txt", "wb");
	for (int i = 0; i < cases; i++)
	{
		switch (result[i])
		{
		case -1:
			fprintf(hfile, "Case #%d: Bad magician!\n", i + 1);
			break;
		case 0:
			fprintf(hfile, "Case #%d: Volunteer cheated!\n", i + 1);
			break;
		default:
			fprintf(hfile, "Case #%d: %d\n", i + 1, result[i]);
			break;
		}
	}
	
	return 0;
}