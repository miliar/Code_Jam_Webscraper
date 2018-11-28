#include <stdio.h>
//#include <algorithm>

void sort( int *seq, int size);

int main()
{
	FILE *in = fopen("test1.in", "r");
	FILE *out = fopen("output.txt", "w");
	int rowf, rows, t;
	int fcards[4][4], scards[4][4];
	int num = 0, am;
	fscanf(in,"%d", &t);
	for( int i = 0; i < t; i++)
	{
		fscanf(in, "%d", &rowf);
		//fseek(in, sizeof(int) * 4 * (row - 1), SEEK_CUR);
		for( int d = 0; d < 4; d++)
			for(int  j = 0; j < 4; j++)
				fscanf(in, "%d", &fcards[d][j]);
		//fseek(in, sizeof(int) * 4 * ( 4 - row), SEEK_CUR);
		fscanf(in, "%d", &rows);
		//fseek(in, sizeof(int) * 4 * (row - 1), SEEK_CUR);
		for( int d = 0; d < 4; d++)
			for(int  j = 0; j < 4; j++)
				fscanf(in, "%d", &scards[d][j]);
		//fseek(in, sizeof(int) * 4 * ( 4 - row), SEEK_CUR);
		am = 0;
		for(int k = 0; k < 4; k++)
			for(int q = 0; q < 4; q++)
			{
				if( fcards[rowf - 1][k] == scards[rows - 1][q] )
				{
					num = fcards[rowf - 1][k];
					am++;
				}
			}

		if(!am)
			fprintf(out, "Case #%d: Volunteer cheated!\n", i + 1);
		else if (am == 1)
			fprintf(out, "Case #%d: %d\n", i + 1, num);
		else
			fprintf(out, "Case #%d: Bad magician!\n", i + 1);
	}
	return 0;
}

/*void sort(int *seq, int size)
{
	int tmp;
	for(int i = 1; i < size; i++)
		for( int j = i; j > 0 && seq[j] > seq[j - 1]; j--)
		{
			tmp = seq[j];
			seq[j] = seq[j - 1];
			seq[j - 1] = tmp;
		}
}*/