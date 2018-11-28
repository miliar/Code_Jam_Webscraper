#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t; scanf("%d",&t);
	for(int test=1;test<=t;test++)
	{
		long long int n,temp,count=0,mul=2;
		int dig[10]={0};
		scanf("%lld",&n);
		temp=n;
		if(n==0) printf("Case #%d: INSOMNIA\n",test);
		else
		{
			while(1)
			{
				//cout<<temp<<endl;
				while(temp>0)
				{
					int r=temp%10;
					temp/=10;
					if(dig[r]==0) 
					{
						count++;
						dig[r]=1;
					}
				}
				if(count==10)
				{
					temp=n*(mul-1);
					break;	
				} 
				temp=n*mul;
				mul++;
			}
			printf("Case #%d: %lld\n",test,temp);
		}
	}
	return 0;
}