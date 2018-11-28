#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
	int t;
	double d,c,f,x;
	scanf("%d",&t);
	for(int k=1;k<=t;k++)
	{
		scanf("%lf",&c);
		scanf("%lf",&f);
		scanf("%lf",&x);
		d=2;
		double min1;
		min1=x/2;
		double min2=min1;
		int i=1;
		double prev=0,temp=0,temp1=0;
		while(temp1<min1)
		{
			temp=temp+c/d;
			d=d+f;
			temp1=temp+x/d;
			if(temp1<min2)
			{
				min2=temp1;
			}
			else
			{
				break;
			}
		}
		printf("Case #%d: %.7lf\n",k,min2);
	}
	return 0;
}
