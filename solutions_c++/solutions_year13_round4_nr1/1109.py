#include<iostream>
#include<queue>
#include<stdio.h>
#include<vector>
#include<string.h>

using namespace std;

#define min(a,b) (a < b ? a : b)
#define INF 0x3f3f3f3f

struct Edge{
	int e,v,rev,cost;
};

struct Pos{
	int x,y;
};

vector<Edge> edge[1010];
int s,t,n,m,N;

Pos prev[1010];
int dis[1010],flow[1010];
bool inQ[1010];

void addedge(int x,int y,int cap,int length){
//	printf("adding %d %d %d %d\n",x,y,cap,length);
	Edge temp;
	temp.e = y;
	temp.v = cap;
	temp.cost = length;
	edge[x].push_back(temp);
	temp.e = x;
	temp.v = 0;
	temp.cost = -length;
	temp.rev = edge[x].size() - 1;
	edge[y].push_back(temp);
	edge[x][edge[x].size() - 1].rev = edge[y].size() - 1;
}

bool spfa(){
	memset(dis,INF,sizeof(dis));
	memset(inQ,0,sizeof(inQ));
	queue<int> q;
	q.push(s);
	inQ[s] = true;
	dis[s] = 0;
	flow[s] = INF;
	while(!q.empty()){
		int u = q.front();
		q.pop();
		inQ[u] = false;
		for(int i = 0;i < edge[u].size();++i){
			if(edge[u][i].v && dis[u] + edge[u][i].cost < dis[edge[u][i].e]){
				flow[edge[u][i].e] = min(flow[u],edge[u][i].v);
				dis[edge[u][i].e] = dis[u] + edge[u][i].cost;
				prev[edge[u][i].e].x = u;
				prev[edge[u][i].e].y = i;
				if(!inQ[edge[u][i].e]){
					inQ[edge[u][i].e] = true;
					q.push(edge[u][i].e);
				}
			}
		}
	}
	return dis[t] != INF;
}

int maxflown;

int maxflow(){
	int ret = 0;
	maxflown = 0;
	while(spfa()){
		int f = flow[t],u = t;
		maxflown += f;
		while(u != s){
			int x = prev[u].x,y = prev[u].y;
			ret += edge[x][y].cost * f;
			edge[x][y].v -= f;
			edge[edge[x][y].e][edge[x][y].rev].v += f;
			u = x;
		}
	}
	return ret;
}

int calccost(int a,int b){
	int x = b - a;
	if(x == 0)
		return 0;
	if(x == 1)
		return n;
	
	int t = (n + n - x + 1) * x / 2;
//	printf("cost %d %d %d\n",a,b,t);
	return t;
}

int o[110],e[110],p[110];



struct Type{
	int o,e,p;
	bool operator<(Type x) const{
		if(o == x.o)
			return e < x.e;
		return o < x.o;
	}
};

Type a[1010];

struct Interval{
	int a,b;
};

vector<Interval> intervals;
vector<int> startidx;


bool cango(int a,int b){
	if(a > b)
		return false;
	if(a == b)
		return true;
	for(int i = 0;i < intervals.size();++i)
		if(a >= intervals[i].a && b <= intervals[i].b)
			return true;
	return false;
}


int main()
{
	FILE *fp;
	FILE *fp2;
	fp = fopen("A-small-attempt0.in","r");
	fp2 = fopen("output.txt","w");
	int T;
	fscanf(fp,"%d",&T);
	for(int caseT = 1;caseT <= T;++caseT){
		for(int i = 0;i <= 1000;++i)
			edge[i].clear();
		fscanf(fp,"%d%d",&n,&m);
		int sum = 0;
		for(int i = 1;i <= m;++i){
			fscanf(fp,"%d%d%d",&o[i],&e[i],&p[i]);
			a[i].o = o[i];
			a[i].e = e[i];
			a[i].p = p[i];
			sum += calccost(o[i],e[i]) * p[i];
		}
		sort(a + 1,a + 1 + m);

	startidx.clear();
		intervals.clear();
		int left = a[1].o,right = a[1].e;
		int sti = 1;
		for(int i = 2; i <= m;++i){
			if(a[i].o <= right)
				right = max(right,a[i].e);
			else{
				Interval t;
				t.a = left;
				t.b = right;
				intervals.push_back(t);
				startidx.push_back(sti);
				sti = i;
				left = a[i].o;
				right = a[i].e;
			}
		}
		Interval tt;
		tt.a = left;
		tt.b = right;
		intervals.push_back(tt);
		startidx.push_back(sti);
		s = 0;
		t = m + m + 1;
		for(int i = 1;i <= m;++i){
			addedge(s,i,p[i],0);
			addedge(i + m,t,p[i],0);
			addedge(i,i + m,INF,calccost(o[i],e[i]));
		}
		for(int i = 1;i <= m;++i)
			for(int j = 1;j <= m;++j){
				if(i == j)
					continue;
				if(cango(o[i],e[j]))
					addedge(i,j + m,INF,calccost(o[i],e[j]));
			}
	//	printf("done\n");
		fprintf(fp2,"Case #%d: %d\n",caseT,sum - maxflow());
	//	system("pause");
	}
	fclose(fp);
	fclose(fp2);
	return 0;
}
