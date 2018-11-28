// B. Rank and File.cpp : Defines the entry point for the console application.
//

#include <stdio.h>

void insertHeap(long current, long low, long high, long a[])
{
	long large, done = 0;
	large = 2 * low + 1;
	while (large <= high && !done)
	{
		if (large < high && a[large] < a[large + 1])
		{
			large++;
		}
		if (current > a[large])
		{
			done = 1;
		}
		else
		{
			a[low] = a[large];
			low = large;
			large = 2 * low + 1;
		}
	}
	a[low] = current;
}

void buildHeap(long a[], long n)
{
	long low;
	for (low = n / 2 - 1; low >= 0; low--)
	{
		insertHeap(a[low], low, n - 1, a);
	}
}

void heapSort(long a[], long n)
{
	long lu, current;
	buildHeap(a, n);
	for (lu = n - 1; lu >= 1; lu--)
	{
		current = a[lu];
		a[lu] = a[0];
		insertHeap(current, 0, lu - 1, a);
	}
}



int main()
{
	FILE *inputFile, *outputFile;
	inputFile = fopen("B-large.in", "r");
	outputFile = fopen("OUTPUT.txt", "w");
	long T, i, N, j, k, tmp, arr[1000], count;
	
	//scanf("%ld", &T);
	fscanf(inputFile, "%ld", &T);
	for (i = 1;i <= T;i++)
	{
		//scanf("%ld", &N);
		fscanf(inputFile, "%ld", &N);
		long heights[2501] = { 0 };
		for (j = 0;j < 2 * N*N - N;j++)
		{
			//scanf("%ld", &tmp);
			fscanf(inputFile, "%ld", &tmp);
			if (heights[tmp] == 0)
			{
				heights[tmp] = 1;
			}
			else
			{
				heights[tmp] = 0;
			}
		}
		count = 0;
		for (j = 1;j <= 2500;j++)
		{
			if (heights[j] == 1)
			{
				arr[count] = j;
				count++;
			}
		}

		heapSort(arr, count);
		//printf("Case #%ld: ", i);
		fprintf(outputFile, "Case #%ld: ", i);
		for (j = 0;j < count;j++)
		{
			//printf("%ld ", arr[j]);
			fprintf(outputFile, "%ld ", arr[j]);
		}
		//printf("\n");
		fprintf(outputFile, "\n");


	}




	return 0;
}

