#include<cstdio>
#include<cmath>
#include<iostream>
#include<cstring>
#include<cstdlib>
using namespace std;

int main()
{
	int i,t;
	double c,f,x,t1,t2,cRate=2.0,time=0.0;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		time = 0.0;
		cRate = 2.0;
		scanf("%lf%lf%lf",&c,&f,&x);
		t1 = x/cRate;
		t2 = c/cRate + x/(cRate+f);
		if(t2 < t1)
		{
			//printf("cRate->%f t1->%f t2->%f time->%f\n",cRate,t1,t2,time);
			while(t2 < t1)
			{
				time += (c/cRate);
				cRate += f;
				t1 = x/cRate;
				t2 = c/cRate + x/(cRate+f); 
				//printf("cRate->%f t1->%f t2->%f time->%f\n",cRate,t1,t2,time);
			}
			time += t1;
			//printf("cRate->%f t1->%f t2->%f time->%f\n",cRate,t1,t2,time);
		}
		else
		{
			time = t1;
		}
		printf("Case #%d: %.7lf\n",i,time);
	}
	return 0;
}
