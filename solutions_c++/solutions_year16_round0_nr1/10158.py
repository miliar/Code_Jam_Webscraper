#include<bits/stdc++.h>

using namespace std;

long long int dp[1000001]={0};

int main()
{
	dp[0] = -1;
	long long int n,temp,i,p,t,ans;
	set<int> digits;
	cin>>t;
	for(p=0;p<t;p++)
	{
		scanf("%lld",&n);
		
		if(dp[n])
		{
			if(dp[n]!=-1)                
				printf("Case #%lld: %lld\n",(p+1),(dp[n]));
			else
				printf("Case #%lld: INSOMNIA\n",(p+1));
		}
		else
		{
			i=1;            
			while(digits.size()!=10)
			{
				temp = n*i;
				while(temp>0)
				{
					digits.insert(temp%10);
					temp/=10;
				}	
				ans = i*n;
				i++;
			}
			dp[n]=ans;
			printf("Case #%lld: %lld\n",(p+1),(dp[n]));
			digits.clear();
		}		
	}
	return 0;
}