#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void sort(double a[], int n)
{
	for(int i = 0; i < n - 1; ++i)
		for(int j = n - 1; j > i; --j)
			if(a[j] < a[j - 1])
			{
				double t = a[j];
				a[j] = a[j - 1];
				a[j-1] = t;
			}
}

int war(double a[], double b[], int n)
{
	int i = 0, j = 0, count = 0;
	while(i < n && j < n)
	{
		if(a[i] > b[j])
			++j;
		else
			++i, ++j, ++count;
	}
	return n - count;
}

int deceitfulwar(double a[], double b[], int n)
{
	int i = n - 1, j = n - 1, count = 0;
	while(i >= 0 && j >= 0)
	{
		if(a[i] > b[j])
			--i, --j, ++count;
		else 
			--j;
	}

	return count;
}

int main(void)
{
	freopen("D-large.in", "rb", stdin);
	freopen("4l.txt", "wb", stdout);

	int t, k = 0;
	scanf("%d", &t);
	while(k++ < t)
	{
		int n;
		double arr1[2000], arr2[2000];

		scanf("%d", &n);
		for(int i = 0; i < n; ++i)
			scanf("%lf", arr1 + i);

		for(int i = 0; i < n; ++i)
			scanf("%lf", arr2 + i);

		sort(arr1, n);
		sort(arr2, n);

		printf("Case #%d: %d %d\n", k, deceitfulwar(arr1, arr2, n), war(arr1, arr2, n));
	}

	return 0;
}