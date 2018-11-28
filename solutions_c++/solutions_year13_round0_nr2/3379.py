#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int a[100][100],b[100][100],t,n,m,pl;

struct node
{
	int e,i,j;
}p[10000];

bool CP(const node &p1,const node &p2)
{
	return p1.e<p2.e;
}

int ck(int i,int j)
{
	int k;
	for(k=0;k<n;k++) if(a[k][j]>a[i][j]) break;
	if(k==n)
	{
		for(k=0;k<n;k++) b[k][j]=1;
		return 0;
	}
	for(k=0;k<m;k++) if(a[i][k]>a[i][j]) break;
	if(k==m)
	{
		for(k=0;k<m;k++) b[i][k]=1;
		return 0;
	}
	return 1;
}

main()
{
	int i,j,tag;
	scanf("%*d");
	while(~scanf("%d%d",&n,&m))
	{
		tag=pl=0;
		memset(b,0,sizeof(b));
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				scanf("%d",&a[i][j]);
				p[pl].e=a[i][j];
				p[pl].i=i;
				p[pl].j=j;
				pl++;
			}
		}
		sort(p,p+pl,CP);
		for(i=0;i<pl;i++)
		{
			if(!b[p[i].i][p[i].j]&&ck(p[i].i,p[i].j)) tag=1;
		}
		printf("Case #%d: ",++t);
		puts(tag?"NO":"YES");
	}
}
