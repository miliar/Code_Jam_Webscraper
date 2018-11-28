#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
//////////////////////////O(V^2E)
#define MAXN 100000
#define MAXE 1100000
#define INF 0x7fffffff
int ne,nv,s,t;
int size,net[MAXN];
struct EDGE{
	int v,next;
	int cap;
	int flow;
}edge[MAXE];

void init(){
	size=0;
	memset(net,-1,sizeof(net));
}
void add(int u,int v,int cap){
	edge[size].v = v;
	edge[size].cap = cap;
	edge[size].flow = 0;
	edge[size].next = net[u];
	net[u] = size;
	++size;

	edge[size].v = u;
	edge[size].cap = 0;
	edge[size].flow = 0;
	edge[size].next = net[v];
	net[v] = size;
	++size;
}

int gap[MAXN];//gap优化
int dist[MAXN];//距离标号
int pre[MAXN];//前驱
int curedge[MAXN];//当前弧

int ISAP(){
	int cur_flow,u,temp,neck,i;
	int max_flow;
	memset(gap,0,sizeof(gap));
	memset(pre,-1,sizeof(pre));
	memset(dist,0,sizeof(dist));
	for(i=1;i<=nv;i++) curedge[i]=net[i];//将当前弧初始话成邻接表的第一条边
	gap[nv]=nv;
	max_flow=0;
	u=s;
	while(dist[s]<nv){
	    //cout<<s<<" "<<" "<<dist[s]<<" "<<nv<<endl;
		if(u==t){//找到一条增广路
			cur_flow=INF;
			for(i=s;i!=t;i=edge[curedge[i]].v){//沿着增广路找到最小增广流量
				if(cur_flow>edge[curedge[i]].cap){
					neck=i;
					cur_flow=edge[curedge[i]].cap;
				}
			}
			for(i=s;i!=t;i=edge[curedge[i]].v){//更新
				temp=curedge[i];
				edge[temp].cap-=cur_flow;
				edge[temp].flow+=cur_flow;
				temp^=1;
				edge[temp].cap+=cur_flow;
				edge[temp].flow-=cur_flow;
			}
			max_flow+=cur_flow;
			u=neck;//下次直接从关键边的u开始新一轮的增广
		}
		for(i=curedge[u];i!=-1;i=edge[i].next)//找到一条允许弧
			if(edge[i].cap>0&&dist[u]==dist[edge[i].v]+1)
				break;
		if(i!=-1){//如果找到 将u指向v
			curedge[u]=i;
			pre[edge[i].v]=u;
			u=edge[i].v;
		}
		else{//找不到
			if(0==--gap[dist[u]]) break;//出现断层
			curedge[u] = net[u];//把当前弧重新设为邻接表中满足要求的第一条弧
			for(temp=nv,i=net[u];i!=-1;i=edge[i].next)
				if(edge[i].cap > 0)
				temp=temp<dist[edge[i].v]?temp:dist[edge[i].v];
			dist[u]=temp+1;//将这个点的距离标号设为由它出发的所有弧的终点的距离标号的最小值加1
			++gap[dist[u]];
			if(u!=s)u=pre[u];
		}
    }
    return max_flow;
}
int mp[550][110];
int id[550][110];
int dir[4][2] = {0,1,0,-1,1,0,-1,0};
int main(){
    int T,cas;
    cin>>T;
    for(cas = 1;cas <= T; cas++){
        int n,m,b;
        init();
        cin>>n>>m>>b;
        memset(mp,0,sizeof(mp));
        for(int i = 1; i <= b; i++){
            int x1,y1,x2,y2;
            scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
            for(int j = x1; j <= y1; j++)
                for(int k = x2; k <= y2; k++){
                    mp[j][k] = 1;
                }
        }
        s = 1;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                id[i][j] = i * m + j + 2;
            }
        }
        t = (n-1) * m + m - 1 + 4;
        nv = t;
        for(int i = 0; i < n; i++)
            for(int j = 0; j < m; j++){
                if(mp[i][j]) continue;
                if(j == 0){
                    add(s,id[i][j],1);
                }
                if(j == m - 1) add(id[i][j],t,1);
                for(int k = 0; k < 4; k++){
                    int x = dir[k][0] + i;
                    int y = dir[k][1] + j;
                if(x < 0 || x >= n || y < 0 || y >= m){
                    continue;
                }
                if(mp[x][y]) continue;
                add(id[i][j],id[x][y],1);
            }
        }
        cout<<ISAP()<<endl;


    }


}
