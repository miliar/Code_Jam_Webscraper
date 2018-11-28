#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>

using namespace std;
double Naomi[1050], Ken[1050];
bool used[1050];

int n;

int dec_war()
{
	int result = 0, k = 0;
	for (int i = 0; i < n; i++)
		used[i] = false;

	while (Naomi[k] < Ken[0])
		k++;
	for (int i = k; i < n; i++)
	{
		for (int j = 0; j < n - k; j++)
			if (!used[j] && Ken[j] < Naomi[i])
			{
				result++;
				used[j] = true;
				break;
			}
	}
	return result;
}

int war()
{
	int result = 0;
	for (int i = 0; i < n; i++)
		used[i] = false;

	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			if (Ken[j] > Naomi[i] && !used[j])
			{
				used[j] = true;
				break;
			}

	for (int i = 0; i < n; i++)
		if (!used[i])
			result++;
	return result;
}

int main() 
{
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);

	int T = 0;
	n = 0;

	scanf("%d", &T);
	for (int q = 0; q < T; q++)
	{
		int res1 = 0, res2 = 0;
		scanf("%d", &n);

		for (int i = 0; i < n; i++)
		{
			scanf("%lf", &Naomi[i]);
		}
		for (int i = 0; i < n; i++)
		{
			scanf("%lf", &Ken[i]);
		}

		sort(Naomi, Naomi + n);
		sort(Ken, Ken + n);

		res1 = dec_war();
		res2 = war();

		printf("Case #%d: %d %d", q + 1, res1, res2);

		if ( q != T - 1 )
			printf("\n");
	}
	return 0;
}