#include <stdio.h>
#include <algorithm>
#include <memory.h>
#include <vector>
#include <iostream>
#include <string>
#include <string.h>
#include <set>
#include <map>
#include <queue>
#include <stdlib.h>
using  namespace std;

typedef __int64 LL;
const int INF = 100000;
int n,m;
int l[1000 + 5],r[1000 + 54],p[1000 + 5];
struct Edge{
    int from,to,cap,flow,cost;
};
const int MAXN = 3000 + 5;
struct MCMF{
    int n,m,s,t;
    vector<Edge>edges;
    vector<int> G[MAXN];
    int inq[MAXN];
    int d[MAXN];
    int p[MAXN];
    int a[MAXN];
    void init(int n){
        this->n=n;
        for(int i=0;i<=n;i++)G[i].clear();
        edges.clear();
    }
    void AddEdge(int from,int to,int cap,int cost){
        edges.push_back((Edge){from,to,cap,0,cost});
        edges.push_back((Edge){to,from,0,0,-cost});
        m=edges.size();
        G[from].push_back(m-2);
        G[to].push_back(m-1);
    }
    bool BellmanFord(int s,int t,int& flow,int& cost){
        for(int i=0;i<=n;i++)d[i]=INF;
            memset(inq,0,sizeof(inq));
        d[s]=0;inq[s]=1;p[s]=0;a[s]=INF;

        queue<int>Q;
        Q.push(s);
        while(!Q.empty()){
            int u=Q.front();Q.pop();
            inq[u]=0;
            for(int i=0;i<G[u].size();i++){
                Edge& e=edges[G[u][i]];
                if(e.cap>e.flow&&d[e.to]>d[u]+e.cost){
                    d[e.to]=d[u]+e.cost;
                    p[e.to]=G[u][i];
                    a[e.to]=min(a[u],e.cap-e.flow);
                    if(!inq[e.to]){
                        Q.push(e.to);
                        inq[e.to]=1;
                    }
                }
            }
        }
        if(d[t]==INF)return false;
        flow+=a[t];
        cost+=d[t]*a[t];
        int u=t;
        while(u!=s){
            edges[p[u]].flow+=a[t];
            edges[p[u]^1].flow-=a[t];
            u=edges[p[u]].from;
        }
        return true;
    }
    int Mincost(int s,int t){
        int flow=0,cost=0;
        while(BellmanFord(s,t,flow,cost));
        return cost;
    }
};
MCMF G;
bool can(int l0,int r0,int l1,int r1) {
	 if(r1 < l0 || r0 < l1) return false;
	 return true;
}
int cost[1000 + 5];
const int MOD = 1000002013;
int M[100+5][100+5];
int main(){
	freopen("A-small-attempt4.in","r",stdin);
	freopen("A-small-attempt4.out","w",stdout);
	int t,cas = 0;
	scanf("%d",&t);
	while(t--) {
		scanf("%d %d",&n,&m);
		int sum = 0;
		memset(cost,0,sizeof(cost));
		cost[0] = 0;
		for(int i = 1;i < n;i++) {
			cost[i] = cost[i-1] + n + 1 - i;
		}
		for(int i = 0;i < m;i++) {
			scanf("%d %d %d",&l[i],&r[i],&p[i]);
			sum += p[i] * cost[r[i]-l[i]];
		}
		G.init(n * 2 + 2);
		int ss = 0,tt = 2 * n + 1;
		memset(M,0,sizeof(M));
		for(int i = 0;i < m;i++)
			for(int j = 0;j < m;j++) {
				if(can(l[i],r[i],l[j],r[j])) {
					M[i][j] = 1;
				}
			}
		for(int k = 0;k < m;k++)
			for(int i = 0;i < m;i++)
				for(int j = 0;j < m;j++) {
					if(M[i][k]&&M[k][j])M[i][j]=1;
				}
		for(int i = 0;i < m;i++) {
			G.AddEdge(ss,l[i],p[i],0);
			G.AddEdge(n + r[i],tt,p[i],0); 
			for(int j = 0;j < m;j ++) {
				if(M[i][j] && r[j] >= l[i]) {
					G.AddEdge(l[i],n+r[j],INF,cost[r[j]-l[i]]);
				}
			}
		}
		printf("Case #%d: %d\n",++cas,(sum-G.Mincost(ss,tt))%MOD);
	}
	return 0;
}