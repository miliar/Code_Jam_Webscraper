#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <iostream>

using namespace std;

typedef long long big;

const int N=55;
struct node
{
	int x,y;
	node(){}
	node(int _x,int _y):x(_x),y(_y){}
};
int x,n,m,dis[N][N];
bool f[N][N][N*N];
int pre[N][N][N*N];
char str[N][N];
bool in(int x,int y)
{
	return x>=1&&x<=n&&y>=1&&y<=m;
}
int main()
{
	int cas,cass,i,j,k,p,t;
	int h,tail;
	double now,ans;
	node s;
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&cas);
	bool flag;
	for(cass=1;cass<=cas;cass++)
	{
		scanf("%d%d%d",&n,&m,&x);
		memset(f,false,sizeof(f));
		for(i=0;i<=m;i++)
			f[1][i][i]=(i!=1);
		for(i=2;i<=n;i++)
			for(j=0;j<=m;j++)
				if(j!=1)
				{
					for(p=0;p<=j;p++)
					{
						for(k=0;k<=n*m-j;k++)
							if(f[i-1][p][k])
							{
								if(i!=n||j==p)
								{
									f[i][j][k+j]=true;
									pre[i][j][k+j]=p;
								}
							}
					}
				}
		flag=false;
		for(j=1;j<=m;j++)
			if(f[n][j][n*m-x])flag=true;
		printf("Case #%d:\n",cass);
		if(n==1&&m==1)
		{
			puts("c");
		}
		else if(x==n*m-1)
		{
			for(i=1;i<=n;i++,puts(""))
				for(j=1;j<=m;j++)
				{
					if(i==1&&j==1)printf("c");
					else printf("*");
				}
		}
		else if(n==1)
		{
			printf("c");
			for(i=2;i<=m-x;i++)
				printf(".");
			for(;i<=m;i++)
				printf("*");
			puts("");
		}
		else if(m==1)
		{
			puts("c");
			for(i=2;i<=n-x;i++)
				puts(".");
			for(;i<=n;i++)
				puts("*");
		}
		else
		{
			if(flag)
			{
				i=n;j=m;p=n*m-x;
				for(j=1;j<=m;j++)
					if(f[n][j][n*m-x])break;
				memset(str,0,sizeof(str));
				for(;i;i--)
				{
					for(k=1;k<=j;k++)
						str[i][k]='.';
					for(;k<=m;k++)
						str[i][k]='*';
					t=pre[i][j][p];
					p-=j;
					j=t;
				}
				str[n][1]='c';
				for(i=1;i<=n;i++,puts(""))
					for(j=1;j<=m;j++)
						printf("%c",str[i][j]);
			}
			else puts("Impossible");
		}
	}
}
