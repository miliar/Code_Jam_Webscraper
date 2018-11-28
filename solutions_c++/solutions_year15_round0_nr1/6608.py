#include <bits/stdc++.h>
using namespace std;

 long long int tt=1,n ,sum,ans,i,t;
 char s[1105];

int main()
{
	scanf("%lld",&t);
	while(tt<=t)
	{
	scanf("%lld",&n);
	scanf("%s",s);
	sum = s[0]-'0';
	ans = 0;
	for(i=1;i<=n;i++)
	{
		if(s[i]=='0')continue;

		if(i > sum )
		{
			ans += i - sum;
			sum = i + (s[i]-'0');

		}
		else if(i<=sum)
		{
			sum += (s[i]-'0');
		}
	}
	printf("Case #%lld: %lld\n",tt,ans);
	tt++;
	}
	return 0;
}
