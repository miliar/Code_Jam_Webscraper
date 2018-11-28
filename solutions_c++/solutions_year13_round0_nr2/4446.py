#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
int t,m,n,mx1[105],mx2[105],map[105][105];
int check()
{
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
			if(map[i][j]<mx1[i] && map[i][j]<mx2[j])return 0;
		}
	}
	return 1;
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	for(int kk=1;kk<=t;kk++)
	{
		scanf("%d%d",&n,&m);
		memset(mx1,0,sizeof(mx1));
		memset(mx2,0,sizeof(mx2));
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				scanf("%d",&map[i][j]);
				mx1[i]=max(mx1[i],map[i][j]);
				mx2[j]=max(mx2[j],map[i][j]);
			}
		}
		int ans=check();
		if(ans)printf("Case #%d: YES\n",kk);
		else printf("Case #%d: NO\n",kk);
	}
	return 0;
}
