// Q1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <string>
#include <vector>

using namespace std;

long int method_one(long int M[], long int N)
{
	int i;
	long int sum=0;
	for (i = 1; i < N; i++)
	{
		if (M[i] < M[i - 1])
			sum = sum + M[i-1] - M[i];
	}

	return sum;
}


int check_rate(long int M[], long int N)
{
	int i;
	int rate=0;
	int temp;

	for (i = 1; i < N; i++)
	{
		temp = M[i-1] - M[i];
		if (temp > rate)
			rate = temp;
	}

	return rate;
}

long int method_two(long int M[], long int N)
{
	int i;
	long int sum = 0;

	int rate;

	rate = check_rate(M, N);


	for (i = 1; i < N; i++)
	{
		if (M[i - 1] > rate)
			sum = sum + rate;
		else
			sum = sum + M[i - 1];
	}

	return sum;
}





int main()
{
    freopen("D://wxy_projects//A-large.in", "r", stdin);
    freopen("D://wxy_projects//A-large.out", "w", stdout);

	int Casenum;
	cin >> Casenum;

	for(int i=0; i<Casenum; i++) {
		long int N;
		long int M[10000];

		cin >> N;

		int ii;
		for (ii = 0; ii < N; ii++)
			cin >> M[ii];


		cout << "Case #" << (i+1) << ": " << method_one(M,N) <<" "<<method_two(M,N)<< endl;
	}
	return 0;
}

