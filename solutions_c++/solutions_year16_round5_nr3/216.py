#include<cstdio>
#include<cmath>
#include<cstring>
#include<algorithm>
using namespace std;
const int inf=0x3f3f3f3f;
struct edge
{
	int x,y,z;
}E[1010];
int a[1010][1010];
int x[1010],y[1010],z[1010],vx[1010],vy[1010],vz[1010],F[1010],fa[1010],T[1010];
bool vis[1010];
int n,s;
int gmin(int x,int y)
{
	return x<y?x:y;
}
bool cmp(edge a,edge b)
{
	return a.z<b.z;
}
int find(int x)
{
	int y;
	if (fa[x]==0) return x;
	if (fa[fa[x]]==0) return fa[x];
	y=find(fa[x]); fa[x]=y; return y;
}
int main()
{
	int i,j,k,TT,_T,min,p,q;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("c.out","w",stdout);
	scanf("%d",&TT);
	for (_T=1;_T<=TT;_T++)
	{
		scanf("%d%d",&n,&s);
		for (i=1;i<=n;i++) scanf("%d%d%d%d%d%d",&x[i],&y[i],&z[i],&vx[i],&vy[i],&vz[i]);
		for (i=1;i<=n;i++)
			for (j=1;j<=n;j++) a[i][j]=(x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j])+(z[i]-z[j])*(z[i]-z[j]);
		memset(vis,false,sizeof(vis));
		memset(F,0x3f,sizeof(F));
		k=1; vis[1]=true;
		for (i=1;i<=n-1;i++)
		{
			for (j=1;j<=n;j++)
				if ((!vis[j])&&(a[k][j]<F[j]))
 				{
					F[j]=a[k][j]; T[j]=k;
				}
			min=inf;
			for (j=1;j<=n;j++)
				if ((!vis[j])&&(a[T[j]][j]<min))
				{
					min=a[T[j]][j]; k=j;
				}
			E[i].x=T[k]; E[i].y=k; E[i].z=F[k]; vis[k]=true;
		}
		sort(E+1,E+n,cmp);
		memset(fa,0,sizeof(fa));
		for (i=1;i<=n-1;i++)
		{
			p=find(E[i].x); q=find(E[i].y); fa[q]=p;
			if (find(1)==find(2))
			{
				printf("Case #%d: %.10lf\n",_T,sqrt(E[i].z)); break;
			}
		}
	}
	return 0;
}
