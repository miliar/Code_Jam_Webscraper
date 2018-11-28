#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
		int t;
		double c, f, x;
		double cookie, cookieIn;
		double time;
		double t1, t2;

		scanf("%d", &t);
		for (int ii = 0; ii < t; ++ii)
		{
				scanf("%lf %lf %lf", &c, &f, &x);
				cookie = 0.0;
				cookieIn = 2.0;
				time = 0.0;

				while (cookie < x)
				{
								if (cookie >= x)
												break;

								time += (double)(c / cookieIn);
								t1 = t2 = time;

								t1 +=  (double)(x - c) / cookieIn;
								t2 += x / (double)(cookieIn + f);
								if (t1 < t2)
								{
												cookie += c; 
								}
								else 
								{
												cookieIn += f; 
												cookie = 0.0;
								}

				}
				if (cookie != x)
					time -= (double)(cookie - x) / cookieIn;


				printf("Case #%d: %.7lf\n", ii+1, time);

		}
}
