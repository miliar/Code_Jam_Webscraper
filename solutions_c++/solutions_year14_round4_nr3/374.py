#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>
#include<iostream>
using namespace std;
const int NN = 505;
const int INF = 1000000005;
int vx[NN],vy[NN],kx,ky;
struct P
{
	int x1,x2,y1,y2;
	void in()
	{
		scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
		x2++;
		y2++;
	}
}dt[NN];
int st[NN][NN],ed[NN][NN],c[4][2]={1,0,0,1,-1,0,0,-1};
bool u[NN][NN];
const int MMax = NN*NN*8 ;
const int NMax = NN*NN;
#define OPT(_) (epool+(((_)-epool)^1))
struct edge{
	int e,f;
	edge *next;
}epool[MMax+MMax],*etop;
edge *E[NMax];
int N;

void addedge(int u,int v,int a,int b){
	etop->e=v;etop->f=a;etop->next=E[u];E[u]=etop;etop++;
	etop->e=u;etop->f=b;etop->next=E[v];E[v]=etop;etop++;
}

int SAP(){
	static int d[NMax],g[NMax+1],Q[NMax];
	static edge *c[NMax],*pre[NMax];
	edge *p;
	int ret=0,x=0,bot,i;
	for (i=0;i<N;i++)c[i]=E[i],d[i]=g[i]=0;
	pre[g[N]=0
    ]=NULL;
	Q[(bot=1)-1]=N-1;
	for (i=0;i<bot;i++)for (edge *p=E[Q[i]];p;p=p->next)
		if (OPT(p)->f && p->e!=N-1 && d[p->e]==0)d[Q[bot++]=p->e]=d[Q[i]]+1;
	for (i=0;i<N;i++)g[d[i]]++;
	while (d[0]<N){
		while (c[x] && (!c[x]->f || d[c[x]->e]+1!=d[x]))c[x]=c[x]->next;
		if (c[x]){
			pre[c[x]->e]=OPT(c[x]);
			x=c[x]->e;
			if (x==N-1){
				int t=~0u>>1;
				for (p=pre[N-1];p;p=pre[p->e])if (t>OPT(p)->f)t=OPT(p)->f;
				for (p=pre[N-1];p;p=pre[p->e])
					p->f+=t,OPT(p)->f-=t;
				ret+=t;
				x=0;
			}
		}else{
			int od=d[x];
			g[d[x]]--;
			d[x]=N;
			for (edge *p=c[x]=E[x];p;p=p->next)if (p->f && d[x]>d[p->e]+1)d[x]=d[p->e]+1;
			g[d[x]]++;
			if (x)x=pre[x]->e;
			if (!g[od])break;
		}
	}
	return ret;
}
int id[NN][NN];
int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,ca=1;
	scanf("%d",&T);
	while(T--)
	{
		cerr << T << endl;
		printf("Case #%d: ",ca++);
		int w,h,n,i,j;
		scanf("%d%d%d",&w,&h,&n);
		kx=w;ky=h;
		for(i=0;i<n;i++)
		{
			dt[i].in();
		}
		/*vx[kx++]=w;
		vy[ky++]=h;
		sort(vx,vx+kx);
		sort(vy,vy+ky);
		kx=unique(vx,vx+kx)-vx;
		ky=unique(vy,vy+ky)-vy;
		//for(i=0;i<kx;i++)printf("i:%d x:%d \n",i,vx[i]);
		//for(i=0;i<ky;i++)printf("i:%d y:%d \n",i,vy[i]);
		for(i=0;i<n;i++)
		{
			dt[i].x1=lower_bound(vx,vx+kx,dt[i].x1)-vx;
			dt[i].y1=lower_bound(vy,vy+ky,dt[i].y1)-vy;
			dt[i].x2=lower_bound(vx,vx+kx,dt[i].x2)-vx;
			dt[i].y2=lower_bound(vy,vy+ky,dt[i].y2)-vy;
			//printf("i:%d x1:%d y1:%d x2:%d y2:%d \n",i,dt[i].x1,dt[i].y1,dt[i].x2,dt[i].y2);
		}*/
		for(i=0;i<kx;i++)for(j=0;j<ky;j++)u[i][j]=true;
		for(i=0;i<n;i++)
		{
			for(j=dt[i].x1;j<dt[i].x2;j++)
			{
				for(int h=dt[i].y1;h<dt[i].y2;h++)
				{
					u[j][h]=false;
				}
			}
		}
		/*for(i=0;i<kx;i++)
		{
			for(j=0;j<ky;j++)printf("%d ",u[i][j]);puts("");
		}*/
		int k=0;
		for(i=0;i<kx;i++)
		{
			for(j=0;j<ky;j++)
			{
				id[i][j]=++k;
			}
		}
		N=k+k+2;
		for (int i=0;i<N;i++)E[i]=NULL;
		etop=epool;
		for(i=0;i<kx;i++)
		{
			for(j=0;j<ky;j++)if(u[i][j])
			{
				addedge(id[i][j]*2,id[i][j]*2+1,1,0);
				if(!j)
				{
					addedge(0,id[i][j]*2,1,0);
				}
				if(j==ky-1)
				{
					addedge(id[i][j]*2+1,N-1,1,0);
				}
				if(j>0&&u[i][j-1])
				{
					addedge(id[i][j-1]*2+1,id[i][j]*2,1,0);
					addedge(id[i][j]*2+1,id[i][j-1]*2,1,0);
				}
				if(j<ky-1&&u[i][j+1])
				{
					addedge(id[i][j]*2+1,id[i][j+1]*2,1,0);
					addedge(id[i][j+1]*2+1,id[i][j]*2,1,0);
				}
				if(i>0&&u[i-1][j])
				{
					addedge(id[i][j]*2+1,id[i-1][j]*2,1,0);
					addedge(id[i-1][j]*2+1,id[i][j]*2,1,0);
				}
				if(i<kx-1&&u[i+1][j])
				{
					addedge(id[i][j]*2+1,id[i+1][j]*2,1,0);
					addedge(id[i+1][j]*2+1,id[i][j]*2,1,0);
				}
			}
		}
		int ret=SAP();
		printf("%d\n",ret);
	}
	return 0;
} 