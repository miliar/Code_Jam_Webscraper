#include <cstdio>
using namespace std;

int main()
{
	int t;
	double c, f, x, r, time;
	scanf("%d",&t);
	for(int k=1; k<=t; k++)
	{
		scanf("%lf %lf %lf", &c, &f, &x);
		r = 2.0;
		time = 0.0;
		while((x/r) > ( (x/(r+f)) + (c/r) ))
		{
			time += (c/r) ;
			r += f;
		}
		time += (x/r);
		printf("Case #%d: %0.7lf\n", k, time);
	}
	return 0;
}
