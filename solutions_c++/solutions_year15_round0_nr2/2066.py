#include <iostream>
#include <stdio.h>
#include<algorithm>
#include<string>
#include<limits.h>
using namespace std;

int main() {
	int t, d, p[1001], i, j, k, max, min = 0, check;
	cin >> t;
	for (i = 1; i <= t; i++)
	{
		cin >> d;
		max = 0;
		min = INT_MAX;
		for (j = 0; j<d; j++)
		{
			cin >> p[j];
			if (max<p[j])
				max = p[j];
		}
		for (k = 1; k <= max; k++)
		{
			check = k;
			for (j = 0; j<d; j++)
			{
				check += ceil(((double)(p[j] - k) / k));
			}
			//printf("%d", check); 
			if (min>check)
				min = check;
		}
		printf("Case #%d: %d\n", i, min);
	}
	return 0;
}