#include <iostream>
#include <conio.h>
#include <fstream>
#include <vector>
#include <string>
#include <math.h>
#include <sstream>
#include <iomanip>
#include <algorithm> 
#define LARGE
using namespace std;
int mod (int val)
{
	if(val >0)
		return val;
	else
		return -val;
}

int calculateMin(std::vector<int> myvectorInt, int numStrings)
{
	int min, val=0;
	int anchor = 0;
	for(int i = 0; i < numStrings; i++)
	{
		val = 0;
		for(int j = 0; j < numStrings; j++)
			val += 	mod(myvectorInt[j] - myvectorInt[i]);

		if(i == 0)
			min = val;
		else if(min > val)
			min = val;
	}
	return min;
}

void main()
{
#ifdef SMALL
	freopen("C:\\sample\\CodeJam\\A-small-attempt0.in","rt",stdin);
	freopen("C:\\sample\\CodeJam\\A-small.out","wt",stdout);
#else
	freopen("C:\\sample\\CodeJam\\Lottery\\B-small-attempt0.in","rt",stdin);
	freopen("C:\\sample\\CodeJam\\Lottery\\B-small-attempt0.out","wt",stdout);
#endif
	string str;
	string val;
	int invalidInputError = - 999;

	int numTestCases;
	unsigned long int A, B, K, temp, sum1= 0, sum2=0, sum3=0;
	cin>>numTestCases;
	//int finalResult[50][2];
	for(int y = 0 ; y < numTestCases; y++)
	{
		sum1 = 0, sum2 = 0, sum3 = 0;
		cin>>A>>B>>K;

		for(unsigned long int i =0; i<A; i++)
		{
			for(unsigned long int j =0; j<B; j++)
			{
				temp = i&j;
				if(temp < K)
				{
					//cout<<"\n"<<i<<"\t"<<j;
					++sum1;
					if(sum1 == 0)
					{
						++sum2;
						if(sum2 == 0)
							++sum3;
					}
				}
			}
		}
		cout<<"\nCase #"<<y+1<<": "<<sum1;
	}
	
}
