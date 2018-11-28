#include<iostream>
#include<cstdio>
#include<limits.h>
using namespace std;
int main()
{
	int t,cases=1;
	FILE *fp1,*fp2;
    fp1=fopen("B-large.in","r");
    fp2=fopen("output.txt","w");
	fscanf(fp1,"%d",&t);
	while(t--)
	{
		double c,f,x,ans=0.0000000;
		double time,s=2.0000000;
		fscanf(fp1,"%lf%lf%lf",&c,&f,&x);
		time=x/s;
		while(true)
		{
			ans=ans+(c/s);
			s=s+f;
			if(ans+x/s > time) 
				break;
			time=ans+x/s;
		}
		fprintf(fp2,"Case #%d: %0.7Lf\n",cases,time);
		cases++;
	}
}