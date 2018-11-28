// Q1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>

#define FO(i, a, b) for (int i = a; i < b; i++)

using namespace std;

int getMin(int arr[], int count)
{
	int min = arr[0];
	for (int i = 1; i < count; i++)
		if (arr[i] < min)
			min = arr[i];

	return min;
}

int getMax(int arr[], int count)
{
	int max = arr[0];
	for (int i = 1; i < count; i++)
		if (arr[i] > max)
			max = arr[i];

	return max;
}

void SortAsc(int arr[], int count)
{
    int temp;

    for (int i = 0; i < count - 1; i++)
    {
        for (int j = i + 1; j < count; j++)
        {
            if (arr[i] > arr[j])
            {
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
}

void SortDesc(int arr[], int count)
{
    int temp;

    for (int i = 0; i < count - 1; i++)
    {
        for (int j = i + 1; j < count; j++)
        {
            if (arr[i] < arr[j])
            {
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
}

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("q1.in", "r", stdin);
	freopen("q1.out", "w", stdout);

	int t, n;
	long m[1000];
	cin >> t;

	for (int i = 0; i < t; i++)
	{
		cout << "Case #" << i + 1 << ": ";

		cin >> n;

		FO (j, 0, n)
			cin >> m[j];

		long sol1 = 0;
		FO (j, 0, n - 1)
			if (m[j] > m [j + 1])
				sol1 += m[j] - m[j + 1];

		long sol2 = 0;
		long max = m[0] - m [1];
		FO(j, 1, n - 1)
			if (m[j] - m[j + 1] > max)
				max = m[j] - m[j + 1];

		FO (j, 0, n - 1)
		{
			if (m[j] <= max)
				sol2 += m[j];
			else
				sol2 += max;
		}

		cout << sol1 << " " << sol2 << endl;
	}

	return 0;
}

