#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
int main() 
{
	int t,i;
	double c,f,x,time1,time2,time3,res,j;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{	res=0.0;
		scanf("%lf%lf%lf",&c,&f,&x);
		j=2;
		while(j)
		{
			time1=c/j;
			time2=x/(j+f);
			time3=x/j;
			time2+=time1;
			if(time2<time3)
			res+=time1;
			else
			{ 
				res+=time3; break; }
			j+=f;
		}
		printf("Case #%d: %.7lf\n",i,res);
	}
	return 0;
}