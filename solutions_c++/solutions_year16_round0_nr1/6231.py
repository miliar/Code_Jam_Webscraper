#include<bits/stdc++.h>
using namespace std;

int main()
{
	long long int t;
	scanf("%lld",&t);
	for(long long int i=0;i<t;i++)
	{
		int check[10]={0};
		long long int n;
		scanf("%lld",&n);
		int count=1;
		int val=1;
		int flag=0;
		if(n==0)
		{
			printf("Case #%lld: INSOMNIA\n",i+1);
			continue;
		}
		while(true)
		{
			long long int temp=count*n;
			if(val==11)
			{
				printf("Case #%lld: %lld\n",i+1,temp-n);
				break;
			}
			while(temp)
			{
				if(check[temp%10]==0)
				{
					val++;
					check[temp%10]=1;
				}
				temp/=10;
			}
			count++;
		}
	}
return 0;
}

