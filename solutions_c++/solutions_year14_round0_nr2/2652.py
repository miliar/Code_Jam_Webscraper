#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
#include<iostream>
#include<queue>
using namespace std;
#define ll long long
#define inf 0x3f3f3f3f

double C,F,X;
double com(double x)
{
	int t1=(int)x;
	int t2=t1+1;
	double sum1=0,sum2=0;
	int i;
	for(i=0;i<t1;i++)
		sum1+=C/(F*i+2);
	sum1+=X/(F*t1+2);
	for(i=0;i<t2;i++)
		sum2+=C/(F*i+2);
	sum2+=X/(F*t2+2);
	return min(sum1,sum2);
}
int main()
{
	int t;
	scanf("%d",&t);
	int he=0;
	while(t--)
	{
		he++;
		scanf("%lf%lf%lf",&C,&F,&X);
		double tt=X/C-2/F-1;
		printf("Case #%d: ",he);
		if(tt<=0.0)
			printf("%.7lf\n",X/2);
		else
			printf("%.7lf\n",com(tt));
	}
}