#include <iostream>

int main()
{
	FILE* file = NULL;

	file = stdin;
	FILE* opfile = stdout;

	//if(!file) file = stdin;

	int T = 0;
	fscanf(file, "%d",&T);

	for(int i = 0 ; i < T; i++)
	{
		int answer1 = 0, answer2 = 0;
		int rowArray1[4][4] ={0};
		int rowArray2[4][4] ={0};

		fscanf(file, "%d", &answer1);
		for(int j = 0; j < 4; j++)
		{
			fscanf(file, "%d %d %d %d", &rowArray1[j][0], &rowArray1[j][1], &rowArray1[j][2], &rowArray1[j][3]);
		}
		
		fscanf(file, "%d", &answer2);
		for(int j = 0; j < 4; j++)
		{
			fscanf(file, "%d %d %d %d", &rowArray2[j][0], &rowArray2[j][1], &rowArray2[j][2], &rowArray2[j][3]);
		}

		int count = 0;
		int matches[4] = {0};
		for(int j = 0; j < 4; j++)
		{
			for(int k = 0; k < 4; k++)
			{
				if(rowArray1[answer1 - 1][j] == rowArray2[answer2 - 1][k])
				{
					matches[count] =  rowArray1[answer1-1][j];
					count++;
				}
			}
		}

		if(count == 0)
		{
			fprintf(opfile,"Case #%d: Volunteer cheated!\n", i+1);
		}
		else if (count == 1)
		{
			fprintf(opfile, "Case #%d: %d\n", i+1, matches[0]);
		}
		else
		{
			fprintf(opfile,"Case #%d: Bad magician!\n", i+1);
		}
	}
	
}