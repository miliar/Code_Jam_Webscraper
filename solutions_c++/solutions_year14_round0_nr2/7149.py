// CookieClickerAlpha.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

char ret_string[65535];

void add_result(char *string)
{
	strcat(ret_string, string);
}

void print_result()
{
	printf("%s", ret_string);
}

int main(int argc, char* argv[])
{
	int cases, i;

	scanf(" %d", &cases);

	for (i = 1; i <= cases; i++)
	{
		double C, F, X;					// Variables
		double t = 0, rate = 2.0;		// Initial Constant Value
		double t1, tp, tr;

		scanf(" %lf %lf %lf", &C, &F, &X);

		do
		{
			// t1 -> a time without a rate-up (y=0 to X)
			// tp -> a time when rate up
			// tr -> a time with a rate-up (y=0 to X)
			// if (t1 < tp+tr) then we get the correct time
			t1 = X / rate;
			tp = C / rate;
			rate += F;
			tr = X / rate;
			
			if (t1 > tp + tr)
				t += tp;	// rate-up
			else
			{
				t += t1;
				break;		// finishing
			}
		} while (1);

		char cat_string[1024];
		sprintf(cat_string, "Case #%d: %.7lf\n", i, t);
		add_result(cat_string);
	}

	print_result();

	return 0;
}

