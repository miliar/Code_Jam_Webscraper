#include <bits/stdc++.h>
using namespace std;

int main()
{
	int k,T;
	double C,F,X,y,rate,cookie;
	scanf("%d",&T);
	k=T;
	while(T--)
	{
		cookie=0;
		rate=2.0;
		y=0;
		scanf("%lf %lf %lf",&C,&F,&X);
		while(cookie<X)
		{
			if(C>=X)
			{
				y=X/rate;
				cookie=X;
				break;
			}
			else if(C<X)
			{
				cookie=C;
				if(((X-C)/rate)>=X/(rate+F))
				{
					y+=C/rate;
					cookie=0;
					rate+=F;
				}
				else if(((X-C)/rate)<X/(rate+F))
				{
					y+=(X/rate);
					cookie=X;
				}
			}
		}
		printf("Case #%d: %.7lf\n",k-T,y);
	}
	return 0;
}
