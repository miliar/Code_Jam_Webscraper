#include <stdio.h>

const int N=110,M=110;
int TC,tc;
int n,m,a[N][M],r[N],c[M];

int min(int p,int q)
{
	return p<q?p:q;
}

bool poss()
{
	int i,j;
	for(i=0;i<n;++i)
		for(r[i]=0,j=0;j<m;++j)
			if(a[i][j]>r[i])
				r[i]=a[i][j];
	for(j=0;j<m;++j)
		for(c[j]=0,i=0;i<n;++i)
			if(a[i][j]>c[j])
				c[j]=a[i][j];
	for(i=0;i<n;++i)
		for(j=0;j<m;++j)
			if(a[i][j]!=min(r[i],c[j]))
				return 0;
	return 1;
}

int main()
{
	int i,j;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	for(scanf("%d",&TC),tc=1;tc<=TC;++tc)
	{
		scanf("%d%d",&n,&m);
		for(i=0;i<n;++i)
			for(j=0;j<m;++j)
				scanf("%d",&a[i][j]);
		printf("Case #%d: %s\n",tc,poss()?"YES":"NO");
	}
	return 0;
}