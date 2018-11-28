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
		double c,f,x;
		double r = 2.0;
		double totalTime = 0.0;
		cin>>c>>f>>x;

		while(true)
		{
			totalTime += (double)(c/r);

			double stopVal = (double)((x-c)/r);
			double nextVal = (double)(x/(r+f));

			if (nextVal < stopVal)
			{
				r += f;
				continue;
			}
			else
			{
				totalTime += stopVal;
				break;
			}
		}
		printf("Case #%d: %0.7f\n",testCounter, totalTime);
		testCounter++;		
	}

	return 0;
}

