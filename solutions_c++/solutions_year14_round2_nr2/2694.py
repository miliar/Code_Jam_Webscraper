// RoundA.cpp : Defines the entry point for the console application.
//

#pragma warning(disable:4996)
#include "stdafx.h"
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<time.h>
#include <iostream>
#include<Windows.h>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	int TC, T, A, B, K, counter;
	int i, j;
	int arr[100];

	freopen("B-small-attempt0.in", "r", stdin);
	freopen("output.in", "w", stdout);

	scanf("%d", &TC);

	for (T = 1; T <= TC; T++){	

		counter = 0;

		scanf("%d %d %d", &A, &B, &K );
		for ( i = 0; i < B; i++)
		{
			for ( j = 0; j < A; j++)
			{
				if ((i & j) < K)
					counter++;
			}
		}

		printf("Case #%d: %d\n", T, counter);
	}

	return 0;
}

