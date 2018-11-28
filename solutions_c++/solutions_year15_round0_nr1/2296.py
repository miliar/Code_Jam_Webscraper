#include<bits/stdc++.h>

using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	int t,smax;
	char string[1005];
	scanf("%d",&t);
	for(int z=1;z<=t;z++)
	{
		scanf("%d",&smax);
		cin>>string;
		int ans=0;
		int len=strlen(string);
		for(int i=0;i<len;i++)
		{
			int temp=0;
			for(int j=0;j<i;j++)
			{
				temp+=string[j]-'0';
			}
			if(i==0)
			{
				
				continue;
			}
			
			if(ans+temp<i)
			{
				int val=i-temp-ans;
				ans+=val;
			}
			
		}
		printf("Case #%d: %d\n",z,ans);
	}
}
