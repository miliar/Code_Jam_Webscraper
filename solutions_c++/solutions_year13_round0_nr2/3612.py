#include<iostream>
using namespace std;

#define N 100

void initLawn (int **lawn, int m, int n, FILE* fInput, int* largestRow, int* largestCol)
{
	for(int i=0; i<m; ++i)
		largestCol[i] = 0;
	for(int i=0; i<n; ++i)
		largestRow[i] = 0;
	for(int i=0; i<m; ++i)
	{
		for (int j=0; j<n; ++j)
		{
			fscanf(fInput, "%d", &lawn[i][j]);
			if (lawn[i][j] > largestRow[j])
				largestRow[j] = lawn[i][j];
			if (lawn[i][j] > largestCol[i])
				largestCol[i] = lawn[i][j];
			//cout<<lawn[i][j]<<" ";
		}
		//cout<<endl;
	}
	/*
	for(int i=0; i<m; ++i)
		cout<<largestCol[i]<<" ";
	cout<<endl;
	for(int i=0; i<n; ++i)
		cout<<largestRow[i]<<" ";
	cout<<endl;
	*/
}

bool canMowe (int row, int col, int **lawn, int* largestRow, int* largestCol)
{
	if (lawn[row][col] >= largestRow[col])
		return true;
	if (lawn[row][col] >= largestCol[row])
		return true;
	return false;
}

bool isValidPattern(int **lawn, int m, int n, int* largestRow, int* largestCol)
{
	if (1 == m || 1 == n)
		return true;
	
	for (int i=0; i<m; ++i)
	{
		for (int j=0; j<n; ++j)
		{
			if (!canMowe(i, j, lawn, largestRow, largestCol))
			{
				//cout<<i<<" "<<j<<endl;
				return false;
			}
		}
	}
	return true;
}

int main()
{
	int **lawn = (int**)malloc(N * sizeof(int*));
	for (int i=0; i<N; ++i)
		lawn[i] = (int*)malloc(N * sizeof(int));
	FILE* fInput = fopen("b.in", "r");
	FILE* fOut = fopen("b.out", "w");
	
	int group = 0;
	int m = 0, n = 0;
	fscanf(fInput, "%d", &group);
	int *largestRow, *largestCol;
	for (int i=0; i<group; ++i)
	{
		fscanf(fInput, "%d%d", &m, &n);
		largestRow = (int*)malloc(n * sizeof(int));
		largestCol = (int*)malloc(m * sizeof(int));
		initLawn(lawn, m, n, fInput, largestRow, largestCol);
		
		fprintf(fOut, "Case #%d: ", i+1);
		if (isValidPattern(lawn, m, n, largestRow, largestCol))
			fprintf(fOut, "YES\n");
		else
			fprintf(fOut, "NO\n");
	}
	
	fclose(fInput);
	fclose(fOut);
	return 0;
}
