#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,i,smax,sum,temp,ans,tc;
	string s;
	scanf("%d",&t);
	tc=1;
	while(tc<=t)
	{
		ans=0;
		scanf("%d",&smax);
		cin>>s;
		sum=s[0]-'0';
		for(i=1;i<smax+1;i++)
		{
			temp=s[i]-'0';
			if(sum<i)
			{
				ans=ans+i-sum;
				sum=i+temp;
			}
			else
			{
				sum+=temp;
			}
		}
		printf("Case #%d: %d\n",tc,ans);
		tc++;
	}
	return 0;
}