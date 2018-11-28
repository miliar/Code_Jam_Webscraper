#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int t;
	scanf("%d",&t);
	int id = 0;
	while(t--)
	{
		double c,f,x;
		double p = 2;
		scanf("%lf%lf %lf",&c,&f,&x);
		double time = 0;
		while(x * f> c*(p + f))
		{
			time += c / p;
			p += f;
		}
		time += x/p;
		printf("Case #%d: %.7lf\n",++id,time);
	}
	return 0;
}

