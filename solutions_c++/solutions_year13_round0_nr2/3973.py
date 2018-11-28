#include "stdio.h"
#include "stdlib.h"
#include "string.h"

void SolveCase(int **arr, int N, int M, int k)
{
	int **temp = new int*[N];
	for(int i = 0; i<N; i++)
	{
		temp[i] = new int[M];
	}

	for(int i = 0; i<N; i++)
	{
		for(int j = 0; j<M; j++)
			temp[i][j] = 100;
	}

	// find the max for each column in arr and put that as the column value for temp
	for(int i = 0; i<N; i++)
	{
		int max = 0;
		for(int j = 0; j<M; j++)
		{
			if(max < arr[i][j])
				max = arr[i][j];
		}

		for(int j = 0; j<M; j++)
		{
			temp[i][j] = max;
		}
	}

	for(int j = 0; j<M; j++)
	{
		int max = 0;
		for(int i = 0; i<N; i++)
		{
			if(max < arr[i][j])
				max = arr[i][j];
		}

		for(int i = 0; i<N; i++)
		{
			if(temp[i][j] > max)
				temp[i][j] = max;
		}
	}

	bool isPossible = true;
	for(int j = 0; j<M; j++)
	{		
		for(int i = 0; i<N; i++)
		{
			if(temp[i][j] != arr[i][j])
			{
				isPossible = false;
				break;
			}
		}

		if(!isPossible)
			break;
	}
	
	if(isPossible)
		printf("Case #%d: YES\n", k);
	else
		printf("Case #%d: NO\n", k);

	for(int i = 0; i<N; i++)
	{
		delete[] temp[i];
	}

	delete[] temp;
}

// ---------------------------------------------------------------------------------
// Main Function
// ---------------------------------------------------------------------------------

void main ()
{
	int T;
	scanf("%d", &T);

	for(int k = 1; k<=T; k++)
	{
		int N, M;
		scanf("%d%d", &N, &M);
		int **arr = new int*[N];
		for(int i = 0; i<N; i++)
		{
			arr[i] = new int[M];
		}

		for(int i = 0; i<N; i++)
		{
			for(int j = 0; j<M; j++)
				scanf("%d", &arr[i][j]);
		}

		SolveCase(arr, N, M, k);

		for(int i = 0; i<N; i++)
		{
			delete[] arr[i];
		}

		delete[] arr;
		
	}
}
