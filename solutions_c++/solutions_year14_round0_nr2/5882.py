#include <iostream>
#include <string>
#include <vector>
#include <stdio.h>

using namespace std;

int main()
{
	int T;
	double C, F, X;
	double cookiePerSec = 2;
	double a,b;
	double sec;
	
	cin >> T;

	for(int i=0;i<T;i++)
	{
		sec = 0;
		cookiePerSec = 2;

		cin >> C;
		cin >> F;
		cin >> X;

		a = X/cookiePerSec;
		b = C/cookiePerSec;
	
		while(a > b+(X/(cookiePerSec+F)))
		{
			sec += b;
			cookiePerSec += F;
			a = X/cookiePerSec;
			b = C/cookiePerSec;
		}

		sec += a;

		printf("Case #%d: %.7f\n",i+1,sec);
	}

	return 0;
}
