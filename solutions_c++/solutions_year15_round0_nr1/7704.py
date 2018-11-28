#include<cstdio>
#include<iostream>
using namespace std;
int cas,n;
char s[1010];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&cas);
	for (int ii=1;ii<=cas;ii++)
	{
		scanf("%d",&n);
		scanf("%s",s);
		int now=0,ans=0;
		for (int i=0;i<=n;i++)
		{
			now+=s[i]-'0';
			ans=min(ans,now-i-1);
		}
		printf("Case #%d: %d\n",ii,-ans);
	}
	return 0;
}
