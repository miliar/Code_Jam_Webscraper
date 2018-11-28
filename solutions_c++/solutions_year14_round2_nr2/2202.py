// CookieClicker.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <iomanip>

using namespace std;

#define	MaxCards	4


int main()
{
	int T,testCounter = 1;
	cin>>T;
	while (T--)
	{
		unsigned long long a, b, k, totalPairs = 0; 
		cin>>a>>b>>k;

		for (unsigned long long i=0; i<a; i++)
		{
			for (unsigned long long j=0; j<b; j++)
			{
				if ( (i&j) < k)
				{
					totalPairs++;
				}
			}
		}

		
		printf("Case #%d: %lld\n",testCounter, totalPairs);
		testCounter++;		
	}

	return 0;
}

