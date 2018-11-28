#include<bits/stdc++.h>
using namespace std;
#define maxn 4000000+10
char s[maxn];
int sum[maxn];

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,cas=0,n;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		scanf("%s",s);
		sum[0]=s[0]-'0';
		for (int i=1;i<=n;i++) sum[i]=sum[i-1]+s[i]-'0';
		int ans=0,tp=sum[0];
		for (int i=1;i<=n;i++)
		{
			if (tp<i) 
			{
				ans+=i-tp;
				tp=i;
			}
			tp+=s[i]-'0';
		}
		printf("Case #%d: %d\n",++cas,ans);
	}
	return 0;
}
