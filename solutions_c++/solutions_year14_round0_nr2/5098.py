#include<stdio.h>
#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
	int z,k,t;
	float c,f,x,s,r;
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		z=0;
		scanf("%f %f %f",&c,&f,&x);
		r=2.0;
		s=0.0;
		while(z!=1)
		{
			if((x/r)>((c/r)+(x/(r+f))))
			{
				s+=(c/r);
				r+=f;
			}
			else
			{
				s+=(x/r);
				z=1;
			}				
		}
		printf("Case #%d: %.7f\n",k,s);
	}
	return 0;
}