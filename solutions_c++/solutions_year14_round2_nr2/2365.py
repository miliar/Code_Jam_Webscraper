#include<stdio.h>
#include<iostream>
#include<iomanip>
#include<string.h>
#include<string>
#include<stdlib.h>
#include<limits.h>
using namespace std;
int main()
{
	int t,n;
	scanf("%d",&t);
	int T=t;
	while(t--)
	{
		long long int a,b,k,count=0;
		scanf("%lld %lld %lld",&a,&b,&k);
		for(long long int i=0;i<a;i++ )
		{
			 for(long long int j=b-1;j>=0;j--)
			{
				if((j&i)<k)
				//{
					count+=1;
				//	break;
				//}
			}
		}
		printf("Case #%d: %lld\n",T-t,count);
	}
}
