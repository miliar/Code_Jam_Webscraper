#include <stdio.h>
#include <conio.h>
#include <climits>
#include <iostream>
using namespace std;

double solution(double C, double F, double T)
{
	double time = 0, earned = 0, rate = 2,remaining = INT_MAX;

	while(remaining != 0)
	{
		if(T < C)
		{
			time = T / rate;
			earned = T;
			return time;
		}
		else
		{
			double tDir, tFarm;
			remaining = T-earned;
			tDir = remaining / rate;
			tFarm = (C / rate) + (T / (rate + F));
			if(tDir < tFarm)
			{
				time += tDir;
				earned = T;
			}
			else
			{
				time += (C / rate) ;				
				rate += F;				
			}
		}
	}

	return time;
}

int main()
{

	unsigned short int testcases;

    cin >> testcases;

    for(int i=1; i <= testcases; i++) 
	{ 
        
            double C, F, T;
			cin >> C;
			cin >> F;
			cin >> T;
			cout.precision(10);
			printf("Case #%d: %.7f\n", i, (double) solution(C, F, T));
        
    }

	getch();


	return 0;
}