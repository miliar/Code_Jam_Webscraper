#include <iostream>
#include <stdlib.h>
using namespace std;

int Partition(float a[], int beg, int end)          //Function to Find Pivot Point
{
	float  pivot = a[beg];
	int loc, p = beg;

	for (loc = beg + 1; loc <= end; loc++)
	{
		if (pivot > a[loc])
		{
			a[p] = a[loc];
			a[loc] = a[p + 1];
			a[p + 1] = pivot;

			p = p + 1;
		}
	}
	return p;
}


void QuickSort(float a[], int beg, int end)
{
	if (beg < end)
	{
		int p = Partition(a, beg, end);                       //Calling Procedure to Find Pivot

		QuickSort(a, beg, p - 1);                             //Calls Itself (Recursion)
		QuickSort(a, p + 1, end);			              //Calls Itself (Recursion)
	}
}

int main()
{
	int test;
	int i, noOfLogs;
	float *naomiLog, *kenLog;
	char *used;
	cin >> test;
	for (i = 1; i <= test; i++)
	{
		cin >> noOfLogs;
		naomiLog = (float *)malloc(noOfLogs* sizeof(float));
		kenLog = (float *)malloc(noOfLogs* sizeof(float));
		int t;
		for (t = 0; t < noOfLogs; t++)
			cin >> naomiLog[t];
		for (t = 0; t < noOfLogs; t++)
			cin >> kenLog[t];
		QuickSort(naomiLog, 0, noOfLogs - 1);
		QuickSort(kenLog, 0, noOfLogs - 1);
		cout << "Case #" << i << ": ";
		int winW = 0;
		used = (char *)malloc(sizeof(char));
		int windW = 0;
		for (t = 0; t < noOfLogs; t++)
		{
			int j;
			for (j = 0; j < noOfLogs; j++)
			{
				if (naomiLog[t] < kenLog[j] && used[j] != 'y')
				{
					winW++;
					used[j] = 'y';
					break;
				}
			}
		}
		for (t = 0; t < noOfLogs; t++)
		{
			int j;
			for (j = 0; j < noOfLogs; j++)
			{
				if (naomiLog[t] > kenLog[j])
				{
					windW++;
					kenLog[j] = 3.3;
					break;
				}
			}
		}
		cout << windW<< " " << noOfLogs - winW << endl;

	}
}
