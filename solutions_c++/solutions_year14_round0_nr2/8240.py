#include<iostream>
#include<fstream>
#include<iomanip>
#include<stdio.h>
using namespace std;
double c,f,x;
double a[1000000],ans,t1;
int main()
{
	int t;
	scanf("%d",&t);
	for(int loop=1;loop<=t;loop++)
	{
		ans=0;
		scanf("%lf %lf %lf",&c,&f,&x);
		ans=x/2;
		for(int i=1;i<=1000000;i++)
		{
			a[i]=a[i-1]+c/(2.0+(double)(i-1)*f);
			ans=min(ans,a[i]+x/(2.0+(double)(i)*f));
		}
		printf("Case #%d: %.7lf\n",loop,ans);
	}
	return 0;
}