#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>

using namespace std;

bool comp(int a, int b)
{
	return a > b;
}

int main()
{
	FILE *in = fopen("B-large.in", "r");
	FILE *out = fopen("B-large.out", "w");
	
	int t;
	fscanf(in, "%d", &t);
	for (int i = 1; i <= t; i++)
	{
		int d, p[1111] = { 0 }, maxi = 0;
		fscanf(in, "%d", &d);
		for (int j = 0; j < d; j++)
		{
			fscanf(in, "%d", &p[j]);
			maxi = max(maxi, p[j]);
		}
		sort(p, p + d, comp);

		int ans = 987654321;
		//j개 남을 때까지
		for (int j = 1; j <= maxi; j++)
		{
			int sum = 0;
			//d개의 접시 탐색
			for (int k = 0; k < d; k++)
			{
				if (p[k] <= j)
				{
					break;
				}
				sum += p[k] / j;
				if (p[k] % j == 0)
				{
					sum--;
				}
			}
			sum += j;
			ans = min(ans, sum);
		}
		fprintf(out, "Case #%d: %d\n", i, ans);
	}


	fclose(in);
	fclose(out);

	return 0;
}