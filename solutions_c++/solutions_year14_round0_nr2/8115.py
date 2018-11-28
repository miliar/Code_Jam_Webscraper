#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#define FOR(i, a, b) for(int i = (a); i < (b); ++i)
#define MIN(a, b) ((a) < (b) ? (a) : (b))

using namespace std;

int main()
{
	int t, case_no = 0;
	double c, f, x;
	double cookie_amount, elapsed_time, control;
	bool changed;
	scanf("%d", &t);
	FOR(i, 0, t)
	{
		scanf("%lf %lf %lf", &c, &f, &x);
		cookie_amount = 2.0; changed = true;
		elapsed_time = 0.0;

		// In case x <= 2.0
		if(x <= 2.0)
			elapsed_time = x / 2.0;
		else
		{
			while(changed)
			{
				if(elapsed_time + (x / cookie_amount) >= elapsed_time + ( (c / cookie_amount) + (x / (cookie_amount + f) ) ) )
				{
					elapsed_time += (c / cookie_amount);
					cookie_amount += f;
				}
				else
				{
					elapsed_time += (x / cookie_amount);
					changed = false;
				}
			}
		}
		printf("Case #%d: %.7lf\n", ++case_no, elapsed_time);
	}
	return 0;
}