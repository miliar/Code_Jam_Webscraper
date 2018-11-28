/*
 * aa.cpp
 *
 *  Created on: Apr 12, 2014
 *      Author: wd007
 */

#include <stdlib.h>
#include <stdio.h>


int main()
{
	int i,j, t, T;

	double c, f, x, r = 2, t1, t2, time = 0;

	scanf("%d", &t);

	T = t;
	while(t--)
	{
		scanf("%lf%lf%lf", &c, &f, &x);

		r = 2;
		t1 = c/r + x/(r+f);
		t2= x/r;
		time = 0;

		while (t1 < t2)
		{
			time += c/r;
			r += f;

			t1 = c/r + x/(r+f);
			t2= x/r;
		}
		time += t2;
		printf("Case #%d: %.7lf\n", T-t, time);
	}
}

