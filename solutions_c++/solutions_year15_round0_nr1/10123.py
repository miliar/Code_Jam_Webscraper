#include<bits/stdc++.h>
using namespace std;

int main()
{
	long long int i,j,s,m,ans,count,t,test;
	char shy[1005];

	scanf("%lld",&t);
	
	for(test=1;test<=t;test++)
	{
		
		
		scanf("%lld",&s);
		scanf("%s",shy);
		
		ans=0;
		count=shy[0]-'0';
		
		for(i=1;i<=s;i++)
		{
			if(i<=count)
			count=count+shy[i]-'0';
			else
			{
				ans=ans+(i-count);
				count=count+(i-count);
				count=count+shy[i]-'0';				
			}			
		}
		
		printf("Case #%lld: %lld\n",test,ans);		
		
	}


	
}


