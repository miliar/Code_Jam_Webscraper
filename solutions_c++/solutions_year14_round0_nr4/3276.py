#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
using namespace std;


void vibsort(long size, float mass[])
{
	for (long i = 0; i < size; i++)
	{
		long minValueIndex = i;

		for (long j = i + 1; j < size; j++)
		{
			if (mass[j] < mass[minValueIndex])
			{
				minValueIndex = j;
			}
		}
		float temp;
		temp = mass[i];
		mass[i] = mass[minValueIndex];
		mass[minValueIndex] = temp;
	}
}

int calc(int n, float ken[], float naomi[])
{
	int m1 = 0, m2 = 0, score = 0;
	while (m1 < n && m2 < n)
	{
		if (ken[m1] > naomi[m2])
			m2++;
		else
		{
			score++;
			m1++;
			m2++;
		}
	}
	return score;
}

int calc2(int n, float ken[], float naomi[])
{
	int m1 = 0, m2 = 0, score = 0;
	while (m1 < n && m2 < n)
	{
		if (naomi[m1] < ken[m2])
		{
			score++;
			m1++;
			m2++;
		}
		else
			m2++;
	}

	return n - score;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	int n;

	float naomi[1000];
	float ken[1000];


	for (int k = 1; k <= t; k++)
	{
		cout << "Case #" << k << ": ";
		cin >> n;
		for (int i = 0; i < n; i++)
			cin >> naomi[i];
		for (int i = 0; i < n; i++)
			cin >> ken[i];
		if (n > 1)
		{
			vibsort(n, naomi);
			vibsort(n, ken);
		}

		cout << calc(n, ken, naomi) << " ";
		cout << calc2(n, ken, naomi) << endl;
	}
	
	
	return 0;
}
