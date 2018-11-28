#include <cstdio>
#include <iostream>

using namespace std;

int TT,T;
double c,f,x,per,tot;

int main()
{
	scanf("%d",&T);TT=T;
	while (T--)
	{
		scanf("%lf%lf%lf",&c,&f,&x);
		printf("Case #%d: ",TT-T);
		if (c>=x)
		{
			printf("%.7f\n",x/2);
		}
		else
		{
			per=2,tot=c/per;
			while ((x-c)/per>x/(per+f))
			{
				per+=f;
				tot+=c/per;
			}
			tot+=(x-c)/per;
			printf("%.7f\n",tot);
		}
	}
}