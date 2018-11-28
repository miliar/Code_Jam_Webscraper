#include <cstdio>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);i++)

const int MAXV=100*500*2+100;
const int MAXE=16*MAXV;

struct building
{
	int x0,y0, x1,y1;
	building(int x0, int y0, int x1, int y1):x0(x0),y0(y0),x1(x1),y1(y1){}
};

int w,h,b;
int hd[MAXV];
int used[MAXV];
int to[MAXE];
int nxt[MAXE];
int cap[MAXE];

int ecnt;

void add_edge(int a, int b)
{
	to[ecnt]=b;
	nxt[ecnt]=hd[a];
	cap[ecnt]=1;
	hd[a]=ecnt;
	ecnt++;

	to[ecnt]=a;
	nxt[ecnt]=hd[b];
	cap[ecnt]=0;
	hd[b]=ecnt;
	ecnt++;
}

int mp[1000][1000];
int dx[4]={1,-1,0,0};
int dy[4]={0,0,1,-1};

int id(int i, int j, int layer)
{
	return layer+2*(i+h*j);
}

int flow(int s, int t)
{
	if(s==t) return true;
	if(used[s]) return false;
	used[s]=true;
	for(int i=hd[s];i!=-1;i=nxt[i])
	{
		if(cap[i] && flow(to[i],t))
		{
			cap[i]--;
			cap[i^1]++;
			return true;
		}
	}
	return false;
}

int main()
{
	int T;
	scanf("%d",&T);
	for(int test=1;test<=T;test++)
	{
		fprintf(stderr,"%d\n",test);
		ecnt=0;
		REP(i,MAXV)
			hd[i]=-1;
		vector<building> v;
		scanf("%d%d%d",&w,&h,&b);
		REP(i,b)
		{
			int x0, y0, x1,y1;
			scanf("%d%d%d%d",&x0,&y0,&x1,&y1);
			assert(x0<=x1);
			assert(y0<=y1);
			v.push_back(building(x0,y0,x1,y1));
		}
		REP(i,h) REP(j,w)
			mp[i][j]=0;
		REP(i,b)
		{
			int x0, y0, x1,y1;
			x0=v[i].x0;
			x1=v[i].x1;
			y0=v[i].y0;
			y1=v[i].y1;
			for(int j=x0;j<=x1;j++)
				for(int k=y0;k<=y1;k++)
					mp[k][j]=1;
		}
		int source=2*h*w;
		int sink=source+1;
		REP(i,h) REP(j,w)
		{
			if(!mp[i][j])
				add_edge(id(i,j,0),id(i,j,1));
			for(int k=0;k<4;k++)
			{
				int nx=i+dx[k];
				int ny=j+dy[k];
				if(0<=nx && nx<h && 0<=ny && ny<w)
					add_edge(id(i,j,1),id(nx,ny,0));
			}
		}
		REP(j,w)
		{
			add_edge(source,id(0,j,0));
			add_edge(id(h-1,j,1),sink);
		}
		int res=0;
		while(1)
		{
			memset(used,0,sizeof(used));
			if(flow(source,sink)) res++;
			else break;
		}
		printf("Case #%d: %d\n",test,res);
	}
	return 0;
}
