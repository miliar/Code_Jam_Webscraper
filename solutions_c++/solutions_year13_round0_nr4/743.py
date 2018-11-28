#include<cstdio>
#include<cstring>
struct pp
{
	int x,cnt,y[1000];
}
a[1000];
int n,k,ans[1000],key[1000];
bool f[10000000];
bool dfs(int x)
{
	if(x==(1<<n)-1)return 1;
	if(f[x])return 0;
	for(int i=1;i<=n;i++)
		if(!((x>>(i-1))&1))
		{
			if(key[a[i].x])
			{
				key[a[i].x]--;
				for(int j=1;j<=a[i].cnt;j++)key[a[i].y[j]]++;
				if(dfs(x+(1<<(i-1))))
				{
					ans[++ans[0]]=i;
					return 1;
				}
				for(int j=1;j<=a[i].cnt;j++)key[a[i].y[j]]--;
				key[a[i].x]++;
			}
		}
	f[x]=1;
	return 0;
}
int main()
{
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		memset(ans,0,sizeof(ans));
		memset(key,0,sizeof(key));
		memset(f,0,sizeof(f));
		scanf("%d%d",&k,&n);
		for(int i=1;i<=k;i++)
		{
			int x;
			scanf("%d",&x);
			key[x]++;
		}
		for(int i=1;i<=n;i++)
		{
			scanf("%d%d",&a[i].x,&a[i].cnt);
			for(int j=1;j<=a[i].cnt;j++)scanf("%d",&a[i].y[j]);
		}
		printf("Case #%d:",tt);
		if(!dfs(0))
		{
			printf(" IMPOSSIBLE\n");
		}
		else {
			for(int i=n;i;i--)
			{
				printf(" %d",ans[i]);
			}
			printf("\n");
		}
	}
}
