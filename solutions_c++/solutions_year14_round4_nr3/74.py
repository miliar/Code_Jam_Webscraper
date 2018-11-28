#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<iostream>
#include<map>
#include<set>
#include<string>
#include<vector>
using namespace std;
typedef long long lld;
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define inf 0xfffffff
#define maxn 1010
struct Edge
{
	int v,next,s;
}edge[4000010];
int head[maxn];
int pos;
void insert(int x,int y,int s)
{
	edge[pos].v=y;
	edge[pos].s=s;
	edge[pos].next=head[x];
	head[x]=pos++;
}
int dis[maxn];
int queue[maxn];
int rear,front;
bool vis[maxn];
void spfa(int n)
{
	for(int i=0;i<=n+1;i++)
	{
		dis[i]=inf;
		vis[i]=false;
	}
	rear=front=0;
	queue[front++]=0;
	dis[0]=0;
	while(rear != front)
	{
		int now=queue[rear++];
		if(rear == maxn)
			rear=0;
		vis[now]=false;
		for(int i=head[now];i;i=edge[i].next)
		{
			int v=edge[i].v;
			if(dis[now]+edge[i].s < dis[v])
			{
				dis[v]=dis[now]+edge[i].s;
				if(!vis[v])
				{
					vis[v]=true;
					queue[front++]=v;
					if(front == maxn)
						front=0;
				}
			}
		}
	}
}
struct Node
{
	int x0,y0,x1,y1;
	void in()
	{
		scanf("%d %d %d %d",&x0,&y0,&x1,&y1);
	}
}p[1010];
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		int n,m,Q;
		scanf("%d %d %d",&n,&m,&Q);
		memset(head,0,sizeof(head));
		pos=1;
		insert(0,Q+1,n);
		for(int i=1;i<=Q;i++)
		{
			p[i].in();
			insert(0,i,p[i].x0);
			insert(i,Q+1,n-1-p[i].x1);
		}
		for(int i=1;i<=Q;i++)
			for(int j=i+1;j<=Q;j++)
			{
				int dx=max(p[i].x0-p[j].x1-1,p[j].x0-p[i].x1-1);
				dx=max(0,dx);
				int dy=max(p[i].y0-p[j].y1-1,p[j].y0-p[i].y1-1);
				dy=max(0,dy);
				int d=max(dx,dy);
//				printf("---%d %d\n",dx,dy);
				if(d > n)
					continue;
				insert(i,j,d);
				insert(j,i,d);
			}
		spfa(Q);
		printf("Case #%d: %d\n",cc,dis[Q+1]);
	}
	return 0;
}
/*
2
3 3 2
2 0 2 0
0 2 0 2
5 6 4
1 0 1 0
3 1 3 3
0 2 1 3
1 5 2 5

1
5 6 4
1 0 1 0
3 1 3 3
0 2 1 3
1 5 2 5


 */
