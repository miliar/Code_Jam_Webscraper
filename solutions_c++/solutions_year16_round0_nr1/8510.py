// ConsoleApplication1.cpp : Defines the entry point for the console application.
//
#include <iostream>
#include "stdafx.h"

using namespace std;

void Solve(int TID, unsigned long long  int N)
{
	if (N == 0) 
	{
		printf("Case #%d: INSOMNIA\n", TID); 
	}
	else {
		bool M[10];
		int cM = 0;
		for (int i = 0; i < 10; i++)
		{
			M[i] = true;
		}
		unsigned long long int B = N;
		while (cM < 10)
		{
			unsigned long long int BB = B;
			while (BB > 0)
			{
				unsigned long long C = BB % 10;
				BB /= 10;
				if (M[C] == true) {
					cM++;
					M[C] = false;
				}
			}
			B += N;
		}

		printf("Case #%d: %llu\n",TID,B-N);
	}		
}
int main()
{
	unsigned long long int  T;
	scanf_s("%lld", &T);
	for (int i = 1; i <= T; i++)
	{
		unsigned long long int N;
		scanf_s("%lld", &N);
		Solve(i, N);
	}	
    return 0;
}

