#include<iostream>
#include<stdio.h>
#include<stdlib.h>

using namespace std;

int main()
{
	int t;
	double c,f,x,temp1,temp2;
	scanf("%d",&t);	
	for(int i=1;i<=t;i++)
	{
		scanf("%lf%lf%lf",&c,&f,&x);
		double time=0,present=2;
		while(1)
		{
			temp1=time+x/present;
			temp2=time+c/present+(x/(present+f));
			if(temp1<temp2)
			{
				time=temp1;
				break;
			}
			else
			{
				time=time+c/present;
				present+=f;
			}
		}
		printf("Case #%d: %.7lf\n",i,time);
	}
	return 0;
}
