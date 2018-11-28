#include <iostream>

using namespace std;

int main()
{
		unsigned int t;
		double C,F,X;
		double cookieRate;
		double totaltime;
		int case1;
	
	case1 = 1;
	
	scanf ("%d", &t);

	while (t)
	{
		scanf ("%lf", &C);
		scanf ("%lf", &F);
		scanf ("%lf", &X);

		cookieRate = 2;
		totaltime = 0;
		
		while (1)
		{
			if ((X/cookieRate) < ((C/cookieRate) + (X/(cookieRate + F))))
			{
				totaltime += X/cookieRate;
	
				printf ("Case #%d: %f\n", case1, totaltime);
				
				case1++;

				break;
			}

			totaltime += C/cookieRate;

			cookieRate += F;
		}

		t--;

	}

}