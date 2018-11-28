
#include <cstdio>
#include <cstring>

long long src,dst;
int cases,n,m;
int innum[101],outnum[101];

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("1.txt","w",stdout);
	scanf("%d",&cases);
	for(int i=0;i<cases;++i)
	{
		scanf("%d%d",&n,&m);
		src=0;
		dst=0;
		memset(innum,0,sizeof(innum));
		memset(outnum,0,sizeof(outnum));
		for(int j=0;j<m;++j)
		{
			int o,e,p;
			scanf("%d%d%d",&o,&e,&p);
			innum[o]+=p;
			outnum[e]+=p;
			src+=p*(n+n-e+o+1)*(e-o)/2;
		}
		for(int i=1;i<=n;++i)
		{
			int p=i;
			while(outnum[i]!=0)
			{
				while(innum[p]==0)--p;
				if(innum[p]>=outnum[i])
				{
					dst+=outnum[i]*(n+n-i+p+1)*(i-p)/2;
					innum[p]-=outnum[i];
					outnum[i]=0;
				}
				else
				{
					dst+=innum[p]*(n+n-i+p+1)*(i-p)/2;
					outnum[i]-=innum[p];
					innum[p]=0;
				}
			}
		}
		printf("Case #%d: %d\n",i+1,(src-dst)%1000002013);
	}
}