#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string>
#include<string.h>
#include<vector>
using namespace std;



long long checker(double x)
{

	double c=x;
	long long rtn=0;
	while(c<1)
	{
		c*=2;
		rtn++;
	}
	if(c-(long long)c>0.000000001) rtn=-1;
	return rtn;
}
int log2_is_int(double x)
{
	double c=log10(x)/log10(2);
	if(c-(long long)c>0.000000001) return 0;
	else return 1;
	
}
long long max(double x)
{
	int c=log10(x)/log10(2);
	return c;
	
}








int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	long long a[100]={0},b[100]={0};
	int i=0,T=0,c=0;
	char *ptr;
	char str[100]={0};
	double check=1,ex=0;
	long long cnt=0,d=0;
	int bol=0;
	scanf("%d",&T);
	for(i=0;i<T;i++)
	{
		scanf("%s",&str);
		ptr=strtok(str,"/");
		a[i]=atol(ptr);
		ptr=strtok(NULL,"/");
		b[i]=atol(ptr);
	}

	for(i=0;i<T;i++)
	{

		if(log2_is_int((double) b[i])!=1)
		{
			if(b[i]%a[i]!=0)printf("Case #%d: impossible\n",i+1);
			else
			{
				ex=log10(b[i])/log10(2);
				ex=ex-(long long)ex;
				d=pow((double)2,(double)ex);
				if(a[i]%d==0)
				{
					a[i]=a[i]/d;
					b[i]=b[i]/d;
					cnt=max((double)b[i])-max((double)a[i]); printf("Case #%d: %lld\n",i+1,cnt);

				}
				else printf("Case #%d: impossible\n",i+1);


			}

		
		}
		else
		{
			cnt=max((double)b[i])-max((double)a[i]); printf("Case #%d: %lld\n",i+1,cnt);
		}

	}
	

	
}