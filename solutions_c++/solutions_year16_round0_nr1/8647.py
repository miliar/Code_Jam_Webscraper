#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("D://Al.in","r",stdin);
	freopen("D://Aout.out","w",stdout);
	int test=0,t;
	scanf("%d",&t);
	while(test!=t)
	{
		unsigned long long int n,i,num=0,ans;
		scanf("%llu",&n);
		int a[10]={0},count=0;
		
		num=n;
		if(n==0)
		printf("\nCase #%d: INSOMNIA",test+1);
		else
		{
			do
			{
				int no=num,sum=0,rem;
				while(no>0)
				{
					rem=no%10;
					if(a[rem]==0)
					{
						a[rem]=1;
						count++;
					}
					no=no/10;
				}
				if(count==10)
				{
					ans=num;
					break;
				}
				num=num+n;
			}while(1);
			printf("\nCase #%d: %llu",test+1,ans);
		}
		test++;
	}
}
