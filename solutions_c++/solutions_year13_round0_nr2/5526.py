#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define FILE_IN "B-small-attempt1.in"
#define FILE_OUT "B-small-attempt1.out"

int check_line(int **arr, int m, int n, int i, int j)
{
	int rLegal = 1, cLegal = 1, index;
	for(index = 0;index<m;index++)
	{
		if(arr[index][j]!=arr[i][j])
		{
			cLegal = 0;
			break;
		}

	}
	for(index = 0;index<n;index++)
	{
		if(arr[i][index]!=arr[i][j])
		{
			rLegal = 0;
			break;
		}
	}
	return (rLegal||cLegal);
}

int is_legal(int **arr, int m, int n, int max)
{
	if(m==1 || n==1)
		return 1;
	int i, j;
	for(i=0;i<m;i++)
		for(j=0;j<n;j++)
		{
			int num = arr[i][j];
			if(num==max)
				continue;
			else
			{
				if(check_line(arr, m, n, i, j))
					continue;
				else
					return 0;
			}
		}
	return 1;
}

int main()
{
	FILE *in = fopen(FILE_IN, "r");
	FILE *out = fopen(FILE_OUT, "w");
	int case_num, i=0;
	fscanf(in, "%d", &case_num);
	while(i<case_num)
	{
		int M, N, m, n, max=0;
		fscanf(in, "%d %d", &M, &N);
		int **arr = (int**)malloc(M*sizeof(int*));
		for(m=0;m<M;m++)
		{
			arr[m] = (int*)malloc(N*sizeof(int));
			for(n=0;n<N;n++)
			{
				fscanf(in, "%d", &arr[m][n]);
				if(arr[m][n]>max)
					max = arr[m][n];
			}
		}

		if(is_legal(arr, M, N, max))
		{
			//printf("Case #%d: %s\n", i+1, "YES");
			fprintf(out, "Case #%d: %s\n", i+1, "YES");
		}
		else
		{
			//printf("Case #%d: %s\n", i+1, "NO");
			fprintf(out, "Case #%d: %s\n", i+1, "NO");
		}

		for(m=0;m<M;m++)
			free(arr[m]);
		free(arr);
		i++;
	}
	fclose(in);
	fclose(out);
	//system("pause");
	return 0;
}