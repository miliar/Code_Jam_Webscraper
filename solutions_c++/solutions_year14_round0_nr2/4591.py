#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
int main() 
{
	int t,k;
	double c,f,x,time1,time2,time3,ans,i;
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{	ans=0.0;
		scanf("%lf%lf%lf",&c,&f,&x);
		i=2;
		while(i)
		{
			time1=c/i;
			time2=x/(i+f);
			time3=x/i;
			time2+=time1;
			//printf("%lf %lf %lf %lf || %lf\n",time1,time2,time4,time3,ans);
			if(time2<time3)
			ans+=time1;
			else
			{ ans+=time3; break; }
			i+=f;
		}
		printf("Case #%d: %.7lf\n",k,ans);
	}
	return 0;
}