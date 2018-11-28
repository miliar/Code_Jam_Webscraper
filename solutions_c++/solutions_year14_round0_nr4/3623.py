#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <math.h>
#include <memory.h>


using namespace std;
#define MAX 1000

double mas1[MAX], mas2[MAX];

int main()
{
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		int N;
		scanf("%d", &N);
		for (int i = 0; i < N; i++)
			scanf("%lf", &mas1[i]);
		for (int i = 0; i < N; i++)
			scanf("%lf", &mas2[i]);
		sort(mas1, mas1+N);
		sort(mas2, mas2+N);
		int index = 0;
		int r1 = 0;
		for (int i = 0; i < N; i++)
		{
			while (index < N && mas2[index] < mas1[i])
				index++;
			if (index < N)
			{
				r1++;
				index++;
			}
		}

		index = 0;
		int r2 = 0;
		for (int i = 0; i < N; i++)
		{
			while (index < N && mas1[index] < mas2[i])
				index++;
			if (index < N)
			{
				r2++;
				index++;
			}
		}
		printf("Case #%d: %d %d\n", t+1, r2, N - r1);
	}


	return 0;
}