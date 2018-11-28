#include<iostream>
#include<cmath>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cstdlib>
using namespace std;

typedef unsigned long long ull;

#define mod 1000000007
#define findmax(a,b) (a)>(b)?a:b
#define findmin(a,b) (a)<(b)?a:b

int main()
{
	int t;
	
	FILE *in,*out;
	in=fopen("B-large.in","r");
	out=fopen("B.out","w");
	fscanf(in,"%d",&t);
	for(int z=1;z<=t;z++)
	{
		double c,f,x,sum=0.0,time=0,rate=2.0;
			fscanf(in,"%lf %lf %lf",&c,&f,&x);
		while(sum!=x)
		{
			double t=x/rate;
			double t1=(c/rate)+(x/(rate+f));
			if(t1<t)
			{ 
				time+=(c/rate);
				rate+=f;
				sum=0;
			}
			else
			{time+=t;sum=x;}
		
		}
	fprintf(out,"Case #%d: %.7lf\n",z,time);	
	}//end of while
	
	return 0;
}