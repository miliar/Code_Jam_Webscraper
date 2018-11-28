#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

void printMatrix(char matrix[4][4])
{
	int i,j;
	for(i=0; i<4; i++)
	{
		for(j=0; j<4; j++)
		{
			printf("%c", matrix[i][j]);
		}
		printf("\n");
	}
	printf("\n");
}

void initMaxArray(int *max_array, int n)
{
	int i;
	for(i=0; i<n; i++)
	{
		max_array[i] = 0;
	}
}

int main()
{
	int t = 0, T;
	char matrix[100][100];
	int row_max[100];
	int col_max[100];
	int n, m;
	int i, j;
	int h;
	int no_flag = 0;
	scanf("%d", &T);

	while(t<T)
	{
		t++;
		no_flag = 0;
		scanf("%d %d", &n, &m);
		initMaxArray(row_max, n);
		initMaxArray(col_max, m);
		for(i=0; i<n; i++)
		{
			for(j=0; j<m; j++)
			{
				scanf("%d", &h);
				matrix[i][j] = h;
				if(h > row_max[i])
					row_max[i] = h;

				if(h > col_max[j])
					col_max[j] = h;
			}
		}

		for(i=0; i<n && (no_flag == 0); i++)
		{
			for(j=0; j<m; j++)
			{
				if((matrix[i][j] < row_max[i]) && (matrix[i][j] < col_max[j]))
				{
					no_flag = 1;
					break;
				}
			}
		}

		if(no_flag == 1)
			printf("Case #%d: NO\n", t);
		else
			printf("Case #%d: YES\n", t);
	}

	return 0;
}
