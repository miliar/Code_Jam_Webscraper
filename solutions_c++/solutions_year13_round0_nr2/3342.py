#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
int t,m,p,n,i,j,k,c[105],l[105],a[105][105],b[105][105];
int main()
{
	//freopen("lawn.in","r",stdin);
	//freopen("lawn.out","w",stdout);
	scanf("%d",&t);
	for (int w=1;w<=t;w++)
	{
		scanf("%d %d",&n,&m);
		memset(l,0,sizeof(l));
		memset(c,0,sizeof(c));
		for (i=1;i<=n;i++)
		{
			for (j=1;j<=m;j++)
			{
				scanf("%d",&a[i][j]);
				l[i]=max(l[i],a[i][j]);
				c[j]=max(c[j],a[i][j]);
			}
		}
		bool ok=false;
		for (i=1;i<=n;i++)
			for (j=1;j<=m;j++)
				{
					b[i][j]=min(l[i],c[j]);
					if (b[i][j]!=a[i][j] && !ok)
					{
						ok=true;
						printf("Case #%d: NO\n",w);
					}
			}
		if (!ok)
			printf("Case #%d: YES\n",w);
	}
}