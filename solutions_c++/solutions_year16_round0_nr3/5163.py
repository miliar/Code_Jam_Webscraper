//============================================================================
// Name        : CoinJam.cpp
// Author      : Mohammed
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;
#include <assert.h>
#include <cstdio>
#include <cstdlib>
#include <string.h>
#include <cmath>

bool isprime(long long int num)
{
	if (num <= 1)
		return false;

	if ((num <= 3))
		return true;

	if (num % 2 == 0)
		return false;

	long long int n = ceil(sqrt(num));
	for (long long int i= 3; i <= n; i+=2)
	{
		if (num % i == 0)
			return false;
	}
	return true;
}

long long int convert_to_base (char* str, int base)
{
	int i = 0;
	long long int number = 0;
	while(str[i]!= '\0')
	{
		if (str[i] == '1')
			number += pow(base,15-i);
		i++;
	}
	return number;
}

unsigned long int divisor_check(long long int num)
{
	for (int i = 2; i < num; ++i)
	{
	    if (num % i == 0)
	        return i;
	}
	return 0;
}
int main()
{
	// open input file
	FILE* inptr = fopen("C-small-attempt0.in","r");
	assert(inptr != NULL);

	// open output file
	FILE* outptr = fopen("out.txt","w");
	assert (outptr != NULL);
	// reading data
	unsigned int T, N, J;
	fscanf(inptr,"%d", &T);
	fscanf(inptr,"%d", &N);
	fscanf(inptr,"%d", &J);
	//cout<<T<<" "<<N<<" "<<J;

	// binary counter counts for each number and see if prime or not
	char counter [15];
	char coin [17]={'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'};
	coin[16]='\0';
	coin[15]='1';
	coin[0]='1';
	unsigned int count = 0;
	unsigned int jamcoins = 1;
	fprintf(outptr,"%s","Case #1:\n");
	while(jamcoins <= J)
	{
		// count number of times that number is not prime
		int prime_count = 0;
		itoa(count,counter,2);
		int n = strlen(counter);
		for(int i = 0; i<n; i++)
			coin[14-i]=counter[n-1-i];
		// change number to different bases and see if prime or not
		for (int j = 2; j<=10; j++)
		{
			// if prime break from loop and see next number
			if (isprime(convert_to_base(coin,j)))
				break;
			// not prime number. so,search for divisor
			else
				prime_count++;
		}
		if (prime_count == 9)
		{
			fprintf(outptr,"%s%s",coin," ");
			// check for a divisor for the number in every base
			for (int j = 2; j<=10; j++)
			{
				unsigned long int divisor = divisor_check(convert_to_base(coin,j));
				fprintf(outptr,"%lu%s",divisor," ");
			}
			fprintf(outptr,"%s","\n");
			jamcoins++;
			prime_count = 0;
		}
		count++;
	}

	// out the number
	return 0;
}
