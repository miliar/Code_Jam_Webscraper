#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

#define N 600

int c1[N], d1[N],c2[N], d2[N];
int n, n1, n2;
#define EPS 1e-9

#define maxn 600
#define maxm 4000
#define inf 100000000000000
struct Edge{ int u,v,cap,x; double cost; }E[maxm];
int e,l[maxn];
inline void init(){ e=0; memset(l,-1,sizeof(l)); }
inline void insert(int u,int v,int cap,double cost){ //单向边
	E[e].u=u; E[e].v=v; E[e].cap=cap; E[e].cost= cost; E[e].x=l[u]; l[u]=e++;
	E[e].u=v; E[e].v=u; E[e].cap=0  ; E[e].cost=-cost; E[e].x=l[v]; l[v]=e++;
}
int q[20*maxn],s,t, inq[maxn],eid[maxn];
double dis[maxn];
void min_cost_max_flow(int src,int sink,int &cap,double &cost){//0~n-1
	cost=0;
    cap=0;
	while( true ){ //不断增广
		//begin spfa
		//for(int i=0;i<maxn;i++) dis[i]=inf; //-inf  最大费
		for (int i = 0; i < n + 10; i++) dis[i] = -inf;
		s=t=0; q[t++]=src; inq[src]=1; dis[src]=0;
		while(s<t){
			int u=q[s++]; inq[u]=0;
			for(int p=l[u];p>=0;p=E[p].x){
				if( E[p].cap<=0 ) continue;
				int v=E[p].v;
			//	if( dis[v]>dis[u]+E[p].cost ){  //<
			    if (dis[v] < dis[u] + E[p].cost) {
					dis[v]=dis[u]+E[p].cost; eid[v]=p;
					if( inq[v]==0 ){
						inq[v]=1; q[t++]=v;
					}
				}
			}
		} //end spfa
		if( dis[sink]<=-inf + EPS) return;  //<=-inf
		int c=inf;
		for(int i=sink;i!=src;i=E[eid[i]].u) c=min(c,E[eid[i]].cap);
		cost+=dis[sink]*c;  cap+=c;
		for(int i=sink;i!=src;i=E[eid[i]].u) {
			int p=eid[i];  E[p].cap-=c; E[p^1].cap+=c;
		}
	}
}//*****************模板结束*******************
/*
int main(){
	int n,m,u,v,cap,cost;
	while(scanf("%d%d",&n,&m)!=EOF ){
		init(); //初始化
		for(int i=1;i<=m;i++){
			scanf("%d %d %d %d",&u,&v,&cap,&cost);
			insert(u,v,cap,cost);
		}
		min_cost_max_flow(0,n-1,cap,cost);
		printf("capicity: %d cost: %d\n",cap,cost);
	}
}
*/




double solve(double K)
{
    init();
    for (int i = 1; i <= n; i++)
        insert(0, i, 1, 0);
    for (int i = 1; i <= n; i++)
        insert(i, n + 1, 1, (double)d1[i] - K * (double)c1[i]);
    for (int i = 1; i <= n; i++)
        insert(i, n + 2, 1, (double)d2[i] - K * (double)c2[i]);
    insert(n + 1, n + 3, n1, 0);
    insert(n + 2, n + 3, n2, 0);
    int temp;
    double cost0;
    min_cost_max_flow(0,n + 3,temp,cost0);
    return cost0;
}





int main()
{
   // freopen("in.txt", "r", stdin);
    int T, ca = 0;
    scanf("%d", &T);
    while (T--)
    {
        scanf("%d%d%d", &n, &n1, &n2);
        for (int i = 1; i <= n; i++)
            scanf("%d%d%d%d", &d1[i], &c1[i], &d2[i], &c2[i]);
        double L = 0, R = 1100000;
        while (L + EPS < R)
        {
            double mid = (L + R)/2;
            double ans = solve(mid);
            if (ans > 0) L = mid;
            else R = mid;
        }
        printf("Case #%d: %.6lf\n", ++ca, L);
    }

}
