// Prob.cpp : Defines the entry point for the console application.
// Author: Ramesh Akinepalli

#include "stdio.h"
//#include <iostream>
//using namespace std;

int main(int argc, char* argv[])
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int iTC, A, B, K, R, Cnt;
	scanf("%d", &iTC);

	for (int i = 1; i <= iTC; i++)
	{
		Cnt = 0;
		printf("Case #%d: ", i);
		scanf("%d%d%d", &A, &B, &K);

		for(int i = 0; i < A; i++)
		{
			for(int j = 0; j < B; j++)
			{
				R = i & j;
				if( R < K ) Cnt++;
			}
		}

		printf("%d\n", Cnt);
	}

	return 0;
}

