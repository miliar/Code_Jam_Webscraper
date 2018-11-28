#include<iostream>
#include<cstdio>
#include<iomanip>
using namespace std;

int main()
{
	cout.precision(10);
	int t,i;
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
	double T=0.00000000,X,C,F,L=2,ans;
	scanf("%lf %lf %lf",&C,&F,&X);
	while(1)
	{
		if( T + X/L < T + C/L + X/(F + L))
			break;
		else
		{
			T=T+C/L;
			L=L+F;
		}
	}
	ans=T + X/L ;
	printf("Case #%d: %0.7lf\n",i+1,ans);
	
	}
}
