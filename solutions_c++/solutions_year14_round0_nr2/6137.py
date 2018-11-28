#include<iostream>
#include<cstdio>
#include<cmath>
#include<map>
#include<algorithm>
#include<vector>

using namespace std;

int main()
{
	int t,i,j,k,cntt;
	double c,f,x,inc;
	double tmp1,tmp2,tmp3;
	scanf("%d",&t);
	cntt=1;
	while(t--)
	{
		inc = 2.0;
		scanf("%lf %lf %lf",&c,&f,&x);
		if(c>=x)
		{
			printf("Case #%d: %.7lf\n",cntt,x/inc);
			cntt++;
			continue;
		}
		tmp1 = x/inc;
		tmp2 = c/inc + x/(inc+f); 
		while(1)
		{
			if(tmp1<tmp2)
			{
				printf("Case #%d: %.7lf\n",cntt,tmp1);
				break;
			}
			else
			{
				inc+=f;
				tmp3 = tmp2;
				tmp1 = tmp2;
				tmp2 = tmp3-(x/inc)+(c/inc)+(x/(inc+f));
			}
		}
		cntt++;
	}
	return 0;
}