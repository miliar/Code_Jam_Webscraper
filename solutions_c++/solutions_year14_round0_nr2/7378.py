#include<cstdio>
#include<iostream>
#include<cmath>
using namespace std;
int main()
{
	int t,k;
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		double c,f,x,y=1.0,t=0.0,z=2.0,p,q;
		scanf("%lf%lf%lf",&c,&f,&x);
		while(1)
		{
			p=x/z+t;
			q=c/z+x/(f+z)+t;		
			if(q<p)
			{
				t+=c/z;
				z+=f;
			}
			else
			{
				t+=x/z;
				printf("Case #%d: %.7lf\n",k,t);
				break;
			}
		}
	}
	return 0;
}
