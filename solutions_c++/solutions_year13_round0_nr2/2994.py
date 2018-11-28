#include<stdio.h>
int a[120][120];
int n,m;
bool Can(int x,int y)
{
	int i;
	int flag=0;
	for(i=1;i<=n;i++)
		if(a[i][y]>a[x][y])
		{
			flag=1;
			break;
		}
	if(!flag)
		return true;
	for(i=1;i<=m;i++)
		if(a[x][i]>a[x][y])
			return false;
	return true;
}
int main()
{
//	freopen("B-small-attempt5.in","r",stdin);
//	freopen("output","w",stdout);
	int t,cnt;
	scanf("%d",&t);
	for(cnt=1;cnt<=t;cnt++)
	{
		int i,j;
		bool can=1;
		scanf("%d%d",&n,&m);
		for(i=1;i<=n;i++)
			for(j=1;j<=m;j++)
				scanf("%d",&a[i][j]);
		for(i=1;i<=n;i++)
			for(j=1;j<=m;j++)
				if(!Can(i,j))
				{
					can=0;
					break;
				}
		printf("Case #%d: %s\n",cnt,can?"YES":"NO");
	}
	return 0;
}