#include<stdio.h>
#include<iostream>
#include<map>
#include<vector>
#include<math.h>
#include<string.h>
#include<limits.h>
#include<algorithm>
using namespace std;
#define mod 1000000007
int oper=0;
long long func(long long A,long long x)
{
    while(A<=x)
	{
		A=A+A-1;
		oper++;
	}
	return A;
}
int main()
{
	long long ar[205],A,a;
	int m,k=0;
	freopen("F:/A-large.in","r",stdin);
	freopen("F:/o.txt","w",stdout);
	int t,n;
	scanf("%d",&t);
	while(t--)
	{
		k++;
		printf("Case #%d: ",k);
		scanf("%lld%d",&a,&n);
        //{printf("%lld %d\n",a,n);continue;}
		for(int i=0;i<n;i++)
		{
			scanf("%lld",&ar[i]);
		}
        if(a==1)
		{printf("%d\n",n);continue;}
		sort(ar,ar+n);
		m=INT_MAX;
		for(int i=0;i<=n;i++)
		{
			oper=0;
			A=a;
			for(int j=0;j<n-i;j++)
			{
				if(ar[j]<A)
				A+=ar[j];
				else
				{
					A=func(A,ar[j])+ar[j];
				}
				
			}
			oper+=i;
			m=min(m,oper);
            //printf("oper=%d\n",oper);
		}
		printf("%d\n",m);
	
	}
}
