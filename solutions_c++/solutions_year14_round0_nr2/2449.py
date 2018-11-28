#include<iostream>
#include<cstdio>
#include<limits.h>
using namespace std;
int main()
{
	int t,h=1;
	FILE *fp1,*fp2;
    fp1=fopen("B-large.in","r");
    fp2=fopen("output.txt","w");
	fscanf(fp1,"%d",&t);
	while(t--)
	{
		long double c,f,x,ans=0.0000000,temp=INT_MAX,s=2.0000000;
		fscanf(fp1,"%Lf%Lf%Lf",&c,&f,&x);
		temp=x/s;
		while(1)
		{
			ans+=(c/s);
			s+=f;
			if(ans+x/s>temp)
				break;
			temp=ans+x/s;
		}
		fprintf(fp2,"Case #%d: %0.7Lf\n",h,temp);
		h++;
	}
}