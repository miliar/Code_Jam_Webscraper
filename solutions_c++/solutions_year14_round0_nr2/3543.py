#include<iostream>
#include<cstdio>
#include<limits.h>
using namespace std;
int main()
{
	int t,n=1;
	FILE *f1,*f2;
    f1=fopen("B-large.in","r");
    f2=fopen("output.txt","w");
	fscanf(f1,"%d",&t);
	while(t--)
	{
		double c,f,x,ans=0.0000000;
		double time,s=2.0000000;
		fscanf(f1,"%lf%lf%lf",&c,&f,&x);
		time=x/s;
		while(true)
		{
			ans=ans+(c/s);
			s=s+f;
			if(ans+x/s > time) 
				break;
			time=ans+x/s;
		}
		fprintf(f2,"Case #%d: %0.7Lf\n",n,time);
		n++;
	}
}