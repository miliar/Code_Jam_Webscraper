#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	int t;	
	cin >> t;

	for (int i = 1; i <= t; i++)
	{
		printf("Case #%d: ", i);
		double c, f, x;	
		cin >> c >> f >> x;
		double total = 0, time = 0, rate = 2;
		while(1)
		{
			double t1 = x / rate;
			double t2;
				t2 = c/rate + (x)/(rate+f);
			if ( t1 < t2)
			{
				time += t1;
				printf ("%f\n", time);
				break;	
			}
			else
			{
				time += c/rate;
				rate += f;
				total -= c;
			}
		}

	}





	return 0;
}	
