#include <bits/stdc++.h>
#define ll long long int

using namespace std;

int main()
{
	int t,sum,ans,s;
	char n[1010];
	cin>>t;
	for(int l=1;l<=t;l++)
	{
		sum=ans=0;
		cin>>s;
		scanf("%s",n);
		for(int i=0;i<=s;i++)
		{
			if(sum<i)
			{
				ans+=i-sum;
				sum+=i-sum;
			}
			sum+=n[i]-48;
		}
		printf("Case #%d: %d\n",l,ans);
	}
	return 0;
}