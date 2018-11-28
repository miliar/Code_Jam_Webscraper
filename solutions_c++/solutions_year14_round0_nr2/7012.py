#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <math.h>

using namespace std;

int main()
{
	int T;
	scanf("%d",&T);

	for (int i = 1; i <= T; ++i)
	{
		double c,f,x;
		scanf("%lf %lf %lf",&c,&f,&x);

		double timer = 0.0;
		double k = 2.0;

		while(true)
		{	
			if( c > x)
			{
				timer += x/2;
				break;
			}

			if (k*c/f + c - x >= 0)
			{
				timer += x/k;
				break;
			}

			timer += c/k;
			k += f;
		}

		printf("Case #%d: %.7lf\n",i,timer);
	}

}