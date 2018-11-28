#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>

using namespace std;
int T,n,a[1010],f[1010][1010],y[1010],p[1010],g[1010],h[1010],q[1010];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int i,j,k;
	scanf("%d",&T);
	for (int ii=1;ii<=T;++ii)
	{
		scanf("%d",&n);
		memset(g,0,sizeof(g));
		memset(h,0,sizeof(h));
		for (i=1;i<=n;++i)
			scanf("%d",&a[i]),y[i]=a[i];
		sort(y+1,y+1+n);
		for (i=1;i<=n;++i)
		{
			for (j=1;j<=n;++j)
				if (a[i]==y[j])
				{
					p[j]=i;
					q[i]=j;
					break;
				}
		}
		for (i=1;i<=n;++i)
		{
			for (j=1;j<i;++j)
				if (a[j]>a[i])
					++g[q[i]];
			for (j=i+1;j<=n;++j)
				if (a[j]>a[i])
					++h[q[i]];
		}
		memset(f,63,sizeof(f));
		int ans=f[0][0];
		f[0][0]=0;
		for (i=1;i<=n;++i)
		{
			for (j=0;j<=i;++j)
			{
				k=n-(i-j)+1;
				f[i][j]=min(f[i][j],f[i-1][j]+h[i]);
				if (j)
					f[i][j]=min(f[i][j],f[i-1][j-1]+g[i]);
			}
		}
		for (i=0;i<=n;++i)
			ans=min(ans,f[n][i]);
		printf("Case #%d: %d\n",ii,ans);
	}
	
	//system("pause");
	return 0;
}
