#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ROW 0
#define COL 1
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define INF 101

int ** test;
int flag = 0;



void test_shell();

int main(void)
{
	FILE *input, *output;
	int size;
	int row, col;
	int *max_row, *max_col;
	int right, left, up, down;

	if((input = fopen("B-small-attempt0.in", "rt")) == NULL)
	{
		printf("input fopen err\n");
		return 0;
	}

	if((output = fopen("B-small-attempt0.out", "wt")) == NULL)
	{
		printf("output fopen err\n");
		return 0;
	}

	fscanf(input,"%d",&size);

	for( int i = 0 ; i < size ; i++ )
	{
		flag = 0;
		fscanf(input,"%d %d",&row, &col);

		max_row = (int*)malloc(sizeof(int) * row);
		max_col = (int*)malloc(sizeof(int) * col);

		test  = (int**)malloc(sizeof(int*) * row);

		for( int j = 0 ; j < row ; j++ )
		{
			test[j] = (int*)malloc(sizeof(int)*col);
			for( int k = 0 ; k < col ; k++ )
				fscanf(input, "%d", &test[j][k]);
		}

		for( int a = 0 ; a < row ; a++)
			max_row[a] = MAX(test[a][0],test[a][col-1]);

		for( int a = 0 ; a < col ; a++)
			max_col[a] = MAX(test[0][a],test[row-1][a]);

		for ( int r = 0 ; r < row ; r++ )
		{
			right = left = up = down = 0;
			for ( int c = 0 ; c < col ; c++ )
			{
				for( int k = r ; k < row ; k++ )
				{
					if( test[k][c] > test[r][c] )
						down = 1;
				}
				for( int k = r ; k >= 0 ; k-- )
				{
					if( test[k][c] > test[r][c] )
						up = 1;
				}
				for( int k = c ; k < col ; k++ )
				{
					if( test[r][k] > test[r][c] )
						right = 1;
				}
				for( int k = c ; k >= 0 ; k-- )
				{
					if( test[r][k] > test[r][c] )
						left = 1;
				}
				if( right + up > 1 || right + down > 1 || left + up > 1 || left + down > 1)
					flag = 1;

				if(flag == 1) break;
			}
			if(flag == 1) break;
		}

		if( flag != 1)
			fprintf(output, "Case #%d: %s\n", i+1, "YES");
		else
			fprintf(output, "Case #%d: %s\n", i+1, "NO");

		for( int j = 0 ; j < row ; j++ )
		{
			free(test[j]);
		}
		free(test);
	}
	return 0;
}


void test_shell()
{

}