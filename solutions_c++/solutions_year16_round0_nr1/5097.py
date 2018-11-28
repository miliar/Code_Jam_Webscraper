#include<stdio.h>
#include<iostream>
#define size 100
using namespace std;
int main()
{
	int t;
	long long ans[size];
	scanf("%d",&t);
	for(int k=0;k<t;k++)
	{
		long long int n,flag[10],n1,cnt=1;
		scanf("%lld",&n);
		for(int i=0;i<10;i++)
			flag[i]=0;
		if(n==0)
			ans[k]=-1;
		else
		{
			n1=n;
			while(true)
			{
				while(n!=0)
				{
					flag[n%10]=1;
					n=n/10;
				}
				int temp=0;
				for(int i=0;i<10;i++)
				{
					if(flag[i]==0)
					{
						temp=1;
						break;
					}
				}
				if(temp==0)
				{
					ans[k]=cnt*n1;
					break;
				}
				else
				{
					n=(++cnt)*n1;
				}
			}
		}		
	}
	for(int k=0;k<t;k++)
	{
		printf("Case #%d: ",k+1);
		if(ans[k]==-1)
		{
			printf("INSOMNIA\n");
		}
		else
		{
			printf("%lld\n",ans[k]);
		}
	}
	return 0;
}
		
		
		
	
