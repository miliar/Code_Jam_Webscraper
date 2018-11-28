#include<iostream>
#include<cstdio>
using namespace std;
double c,f,x,c0,c1;
int t;
double C(int p)
{
	return x/(2.0+p*f);
}

int main()
{
	scanf("%d",&t);
	for (int test=1;test<=t;++test)
	{
		scanf("%lf%lf%lf",&c,&f,&x);
		c0=0;
		for (int i=1;;i++)
		{
			c1=c0+c/(2.0+(i-1)*f);
			if (C(i)+c1>C(i-1)+c0)
			{
				printf("Case #%d: %.7lf\n",test,C(i-1)+c0);
				break;
			}
			c0=c1;
		}
	}
	return 0;
}