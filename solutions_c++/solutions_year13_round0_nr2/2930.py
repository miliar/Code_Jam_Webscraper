#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_N 110
template<class T> T Max(T a,T b){return a<b?b:a;}
int T;
int n,m;
int map[MAX_N][MAX_N];
int hx[MAX_N],hy[MAX_N];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&T);
	int i,j;
	for(int Ti=1;Ti<=T;++Ti)
	{
		scanf("%d%d",&n,&m);
		for(i=1;i<=n;i++)
			for(j=1;j<=m;++j)
				scanf("%d",&map[i][j]);
		for(i=1;i<=n;i++)
		{
			hx[i]=0;
			for(j=1;j<=m;++j)
				hx[i]=Max(hx[i],map[i][j]);
		}
		for(i=1;i<=m;i++)
		{
			hy[i]=0;
			for(j=1;j<=n;++j)
				hy[i]=Max(hy[i],map[j][i]);
		}
		for(i=1;i<=n;++i)
		{
			for(j=1;j<=m;++j)
				if(map[i][j]<hx[i] && map[i][j]<hy[j])
					break;
			if(j<=m) break;
		}
		if(i<=n)
			printf("Case #%d: NO\n",Ti);
		else
			printf("Case #%d: YES\n",Ti);
	}
	return 0;
}
