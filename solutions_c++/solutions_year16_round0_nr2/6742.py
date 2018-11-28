#include<bits/stdc++.h>
using namespace std;

int main()
{
	int T,l,ans,i,j,now,top;
	char c[105]={'\0'};
	freopen("B-large.in","r",stdin);
	freopen("out.out","w",stdout);
	scanf("%d",&T);
	for(i=1;i<=T;i++)
	{
		memset(c,0,sizeof(c));
		ans=0;
		scanf("%s",c);
		l=strlen(c);
		top=c[0]=='-'?0:1;
		for(j=1;j<l;j++)
		{
			now=c[j]=='-'?0:1;
			if(now!=top)
			{
				top=now;
				ans++;
			}
		}
		if(!top)
		{
			ans++;
		}
		printf("Case #%d: %d\n",i,ans);
	}
}
