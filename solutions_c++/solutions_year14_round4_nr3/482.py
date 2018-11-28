#include<cstdio>
#include<cstring>
#include<algorithm>
#include<queue>
using namespace std;
const int maxn=1010;
const int maxw=1010;
const int maxN=maxw*maxn*4+3;
const int oo=1e9+7;
struct edge{
	int v,w;
	edge *next,*op;
};
int N;
int lev[maxN];
edge pool[maxN*4],*E[maxN],*tp;

void add(int u,int v,int w,int w2)
{
	tp->v=v;tp->w=w;tp->next=E[u];E[u]=tp++;
	tp->v=u;tp->w=w2;tp->next=E[v];E[v]=tp++;
	E[u]->op=E[v];E[v]->op=E[u];
}

bool mklevel()
{
	static queue<int> q;
	for(int i=1;i<=N;i++) lev[i]=-1;
	lev[0]=0;
	q.push(0);
	while(!q.empty())
	{
		int u=q.front();q.pop();
		for(edge *e=E[u];e;e=e->next)
			if(e->w && lev[e->v]==-1)
			{
				lev[e->v]=lev[u]+1;
				q.push(e->v);
			}
	}
	return ~lev[N];
}
int aug(int u,int b)
{
	if(u==N)return b;
	int c=0,dt;
	for(edge *e=E[u];e && c<b;e=e->next)
		if(lev[e->v]==lev[u]+1 && e->w)
		{
			dt=aug(e->v,min(b-c,e->w));
			c+=dt;
			e->w-=dt;e->op->w+=dt;
		}
	if(c==0) lev[u]=-1;
	return c;
}
int dinic()
{
	int ans=0;
	while(mklevel()) ans+=aug(0,oo);
	return ans;
}
struct rec{
	int x1,y1,x2,y2;
};
struct event{
	int y,nu,flag;
	event(int _y,int _n,int _f):y(_y),nu(_n),flag(_f){}
	bool operator < (const event &e)const{
		if(y<e.y)return true;
		if(y>e.y)return false;
		return flag>e.flag;
	}
};
int w,h,n;
rec r[maxn];
bool mark[maxw][maxn*2];
int nu[maxw][maxn*2][2];
int ny=0,y[maxn*2];

int main()
{
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		scanf("%d%d%d",&w,&h,&n);
		//nx=ny=0;
		ny=0;
		y[ny++]=0;
		for(int i=0;i<n;i++) 
		{
			scanf("%d%d%d%d",&r[i].x1,&r[i].y1,&r[i].x2,&r[i].y2);
			//r[i].x2++;r[i].y2++;
			//y[ny++]=r[i].y1;
			//y[ny++]=r[i].y2;
		}
		y[ny++]=h;
		sort(y,y+ny); ny=unique(y,y+ny)-y;
		memset(mark,0,sizeof mark);
		for(int i=0;i<n;i++)
		{
			/*
			int y1=lower_bound(y,y+ny,r[i].y1)-y,
				y2=lower_bound(y,y+ny,r[i].y2)-y;
				*/
			for(int x=r[i].x1;x<=r[i].x2;x++)
				for(int y=r[i].y1;y<=r[i].y2;y++)
					mark[x][y]=true;
		}
		N=1;
		for(int i=0;i<w;i++)
			for(int j=0;j<h;j++)
			{
				if(mark[i][j])continue;
				nu[i][j][0]=N++;
				nu[i][j][1]=N++;
			}
		tp=pool;
		for(int i=0;i<=N;E[i++]=0);
		for(int i=0;i<w;i++)
			for(int j=0;j<h;j++)
			{
				if(mark[i][j])continue;
				add(nu[i][j][0],nu[i][j][1],1,0);
				if(j>0    && !mark[i][j-1])  add(nu[i][j][1],nu[i][j-1][0],1,0);
				if(j<h-1 && !mark[i][j+1])  add(nu[i][j][1],nu[i][j+1][0],1,0);
				if(i<w-1 && !mark[i+1][j]) add(nu[i][j][1],nu[i+1][j][0],1,0);
				if(i>0 && !mark[i-1][j])  add(nu[i][j][1],nu[i-1][j][0],1,0);
			}
		for(int i=0;i<w;i++) if(!mark[i][0]) add(0,nu[i][0][0],1,0);
		for(int i=0;i<w;i++) if(!mark[i][h-1]) add(nu[i][h-1][1],N,1,0);
		printf("Case #%d: %d\n",t,dinic());
		//printf("N=%d\n",N);
	}
	return 0;
}
