// test1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <math.h>

void calcForOne(int n, int p, int t, int *sum, int *max)
{
	int N = (p + t - 1) / t;
	int res = (p + N-1) / N;
	(*sum) += (n*(N - 1));
	*max = *max > res ? *max : res;
}

int calcMin(int *H, int pmax, int pt, int D)
{
	int Ts = (int)std::sqrt((double)pt / D);
	int min = INT_MAX;
	for (; Ts <= pmax; Ts++){
		int sum=0, max=0;
		for (int i = Ts + 1; i <= pmax; i++){
			if (H[i] < 1)
				continue;
			calcForOne(H[i], i, Ts, &sum, &max);
		}
		for (int i = max + 1; i <= Ts; i++)
			max = H[i] > 0 ? i : max;

		min = min > (sum + max) ? (sum + max): min;
	}
	return min;
}
int _tmain(int argc, _TCHAR* argv[])
{
	int T, i;
	scanf_s("%d", &T);
	for (i = 0; i < T; i++){
		int D;
		int p[1001];
		int H[1001] = { 0 };
		int pmax = 0, pt=0;
		scanf_s("%d", &D);
		for (int j = 0; j < D; j++){
			scanf_s("%d", &p[j]);
			H[p[j]]++;
			pt += p[j];
			pmax = pmax>p[j] ? pmax : p[j];
		}
		printf("Case #%d: %d\n", i+1, calcMin(H, pmax, pt, D));
	}

	return 0;
}

