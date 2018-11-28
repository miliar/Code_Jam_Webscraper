#include <iostream>
using namespace std;
int  a[4][4],b[4][4];
int main()
{
	int  Cases;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&Cases);
	for (int i = 1; i<= Cases; ++i)
	{
		printf("Case #%d: ", i);
		double C,F,X, tot=0,mon=0,speed=2;
		scanf("%lf%lf%lf",&C,&F,&X);
		double tmp = F*(X/C-1);
		if(X<=C) printf("%.7lf\n",X/speed);
		else
		{
			while(1)
			{
				tot+=C/speed;
				if(speed>= tmp)    //  F/speed<C/(X-C)
				{
					tot+= (X-C)/speed;
					printf("%7lf\n",tot);
					break;
				}
				else
				{
					speed+=F;
				}
			}
		}
		
	}
	return 0;
}