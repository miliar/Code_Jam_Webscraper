// CookieClicker.cpp : Defines the entry point for the console application.
//

#include <stdio.h>


int main()
{
	int t;

	scanf("%d", &t);
	double c, f, x;
	while (t--) {
		double rate = 2.0;
		scanf("%lf", &c);
		scanf("%lf", &f);
		scanf("%lf", &x);
	
		
		bool done = false;
		double timePassed = 0.0000000;
		while (!done) {
			if (x/rate < c/rate + x/(rate + f)) {
				timePassed += x/rate;
				done = true;
			} else {
				timePassed += c/rate;
				rate += f;
			}
		}
		static int id = 0;
		printf("Case #%d: %.7f\n", ++id, timePassed);
	}
	
	return 0;
}

