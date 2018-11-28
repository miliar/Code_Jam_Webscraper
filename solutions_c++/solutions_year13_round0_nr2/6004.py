#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<string>
#include<algorithm>

using namespace std;
int T;
int N,M;
int a[101][101];
struct point
{
int x,y;
}P[10010];
bool flag[10010];
int main()
{	
	//freopen("C:\\Users\\think\\Desktop\\B-small-attempt0.in","r",stdin);
	//freopen("C:\\Users\\think\\Desktop\\c.out","w",stdout);
	scanf("%d",&T);
	for(int y=1;y<=T;y++)
		{
		scanf("%d%d",&N,&M);
		memset(a,0,sizeof(a));
		int mini=200;
		for(int i=0;i<N;i++)
			for(int j=0;j<M;j++)
				{
					scanf("%d",&a[i][j]);
					if(a[i][j]<mini)
						mini=a[i][j];
				}
			int cnt=0;
		for(int i=0;i<N;i++)
			for(int j=0;j<M;j++)
				{
				if(a[i][j]==mini)
					{
						P[cnt].x=i;
						P[cnt++].y=j;
					}
				}
	memset(flag,0,sizeof(flag));
		for(int i=0;i<cnt;i++)
			{
				
				int xx=P[i].x;
				int yy=P[i].y;
				int mm;
				for(mm=0;mm<M;mm++)
					{
						if(a[xx][mm]>mini)
							break;
					}
				if(mm==M)
					{
					flag[i]=1;
					continue;
					}
				for(mm=0;mm<N;mm++)
					{
						if(a[mm][yy]>mini)
							break;
					}
				if(mm==N)
					{
						flag[i]=1;
						continue;
					}
			}
		int u;
		for(u=0;u<cnt;u++)
			{	
			if(flag[u]==0)
				{
				break;
				}
			}
		if(u==cnt)
			printf("Case #%d: YES\n",y);
		else 
			printf("Case #%d: NO\n",y);
		}
	return 0;
}

