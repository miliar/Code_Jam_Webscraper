/*         DECEITFUL WAR
*/


#include<stdio.h>
#include<iostream>
using namespace std;

int cmp(const void *x, const void *y)
{
	double xx = *(double*)x, yy = *(double*)y;
	if (xx > yy) return -1;
	if (xx < yy) return  1;
	return 0;
}
int main()
{
	int t, k, i, j, n, war, d_war;
	double arr1[1000], arr2[1000];
	cin >> t;

	for (k = 1; k <= t; k++)
	{
		war = 0, d_war = 0;
		cin >> n;

		for (i = 0; i < n; i++)
			cin >> arr1[i];
		qsort(arr1, n, sizeof(double), cmp);

		for (i = 0; i < n; i++)
			cin >> arr2[i];
		qsort(arr2, n, sizeof(double), cmp);

		cout << "Case #" << k << ": ";

		double temp[1005];
		for (i = 0; i < n; i++)
			temp[i] = arr2[i];


		for (i = 0; i < n; i++)
		{
			for (j = 0; j < n; j++)
			{
				if (arr1[i] > arr2[j])
				{
					arr2[j] = 10;
					d_war++;
					break;
				}
			}
		}
		cout << d_war << " ";


		for (i = 0; i < n; i++)
		{
			for (j = n - 1; j >= 0; j--)
			{
				if (temp[j] >= arr1[i])
				{
					temp[j] = -1;
					break;
				}
			}
			if (j == -1)
				war++;
		}
		cout << war << endl;
	}
	return 0;
}
