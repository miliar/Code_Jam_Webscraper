#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <iostream>
#include <stdint.h>

char str[30];

bool palindrom(unsigned long long int num)
{
	sprintf(str, "%llu", num);
	int len = strlen(str);
	int halflen = len/2;
	for(int i = 0; i < halflen; i++)
	{
		if (str[i] != str[len-i-1])
			return false;
	}
	return true;
}

void doCase(int caseNumber)
{
	unsigned long long int omin, omax, min, max, result = 0;

	scanf("%llu %llu",&omin, &omax);

	min = (unsigned long long int)ceil(sqrt(omin));
	max = (unsigned long long int)floor(sqrt(omax));
	
	for(unsigned long long int i = min; i <= max; i++)
	{
		if (palindrom(i) && palindrom(i*i))
			result++;
	}

	printf("Case #%d: %llu\n",caseNumber,result);
}

int main(int argc, char const *argv[])
{
	int testCases;
	scanf("%d",&testCases);

	for(int i = 0; i < testCases; i++)
		doCase(i+1);

	return 0;
}
