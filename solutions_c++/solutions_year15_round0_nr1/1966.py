#include<bits/stdc++.h>

using namespace std;

int T,S;

char s[1010];

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		scanf("%d%s",&S,s);
		int cnt=0,ans=0;
		for(int i=0;i<=S;i++)
		{
			if (cnt<i)
			{
				ans+=i-cnt;
				cnt=i;
			}
			cnt+=s[i]-'0';
		}
		printf("Case #%d: %d\n",tt,ans);
	}
	
	return 0;
}