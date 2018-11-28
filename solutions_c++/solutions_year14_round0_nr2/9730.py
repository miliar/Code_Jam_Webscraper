#include <stdio.h>
#include <string.h>
#include <algorithm>
#define eps 1e-8
using namespace std;

int main()
{
	freopen("B-small-attempt3.in", "r", stdin);
	freopen("data.out", "w", stdout);

	double c,f,x;
	int test;
	scanf("%d",&test);
	for(int item = 1; item <= test; item++)
	{
		scanf("%lf %lf %lf",&c,&f,&x);

		double s = 2.0;

		while(1)
		{
			double t3 = x/s;

			double t1 = c/s;
			double t2 = x/(s+f);

			if( t1+t2 > t3)
				break;
			else
				s += f;
		}

		double speed = 2.0;

		double time = 0;

		while( (s-speed) > eps)
		{
			time += c/speed;
			speed += f;
		}

		time += x/speed;

		printf("Case #%d: %.7lf\n",item,time);

	}
	return 0;
}
