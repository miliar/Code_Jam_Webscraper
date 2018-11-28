#include<cstdio>

int h[101];
int g[101];
int d[101][1001];

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int tc,tcn;
	scanf("%d",&tcn);
	for(tc=1;tc<=tcn;tc++)
	{
		int i,j,n,p,q;
		scanf("%d%d%d",&p,&q,&n);
		for(i=1;i<=n;i++)scanf("%d%d",&h[i],&g[i]);
		for(i=0;i<=n;i++)for(j=0;j<=1000;j++)d[i][j]=-987654321;
		d[0][1]=0;
		for(i=0;i<n;i++)
		{
			for(j=999;j>=0;j--)if(d[i][j]<d[i][j+1])d[i][j]=d[i][j+1];
			for(j=0;j<=1000;j++)
			{
				if(j+(h[i+1]+q-1)/q<=1000&&d[i+1][j+(h[i+1]+q-1)/q]<d[i][j])
					d[i+1][j+(h[i+1]+q-1)/q]=d[i][j];
				if(j+(h[i+1]-1)/q-((h[i+1]-1)%q+p)/p>=0&&j+(h[i+1]-1)/q-((h[i+1]-1)%q+p)/p<=1000&&d[i+1][j+(h[i+1]-1)/q-((h[i+1]-1)%q+p)/p]<d[i][j]+g[i+1])
					d[i+1][j+(h[i+1]-1)/q-((h[i+1]-1)%q+p)/p]=d[i][j]+g[i+1];
			}
		}
		for(j=999;j>=0;j--)if(d[n][j]<d[n][j+1])d[n][j]=d[n][j+1];
		printf("Case #%d: %d\n",tc,d[n][0]);
	}
	return 0;
}