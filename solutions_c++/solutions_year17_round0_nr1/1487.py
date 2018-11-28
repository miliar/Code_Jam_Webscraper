#include <bits/stdc++.h>
using namespace std;

const int MAXL=1005;

char s[MAXL];

void solve()
{
	int k;
	scanf("%s%d",s,&k);
	int l=strlen(s);
	for (int i=0;i<l;i++)
		s[i]=(s[i]=='+'?1:0);
	int ans=0;
	for (int i=0;i+k<=l;i++)
		if (!s[i])
		{
			for (int j=i;j<i+k;j++)
				s[j]^=1;
			ans++;
		}
	for (int i=l-k+1;i<l;i++)
		if (s[i]==0)
		{
			puts("IMPOSSIBLE");
			return;
		}
	printf("%d\n",ans);
}

int main()
{
	freopen("read.txt","r",stdin);
	freopen("write.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for (int i=1;i<=T;i++)
	{
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}
