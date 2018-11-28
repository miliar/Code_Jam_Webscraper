#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
	int T = 1;
	double CPS = 2.00000;
	bool Win = false;
	double C = 30.50000; //0.0;
	double F = 3.14159; //0.0;
	double X = 1999.19990; //0.0;
	double sec = 0.0000000;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		Win = false;
		sec = 0.0000000;
		CPS = 2;
		scanf("%lf %lf %lf", &C, &F, &X);
		printf("Case #%d: ", i);

		while(!Win)
		{
			if(C / CPS + X / (CPS + F) < X / CPS)
			{
				sec += C / CPS;
				CPS += F;
			}
			else
			{
				sec += X / CPS;
				Win = true;
			}
			
		}
		printf("%.7f\n", sec);
	}
	
	
}