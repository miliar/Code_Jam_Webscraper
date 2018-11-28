#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstring>


using namespace std;

#define maxn 10020
#define maxm 100020
#define inf 0x3fffffff
#define INF 100000000000000000
#define LL long long

int v[maxn];
int EN, R;
int n;


struct Edge{ int u,v,cap;LL cost;int x; }E[maxm];
int e,l[maxn];
inline void init(){ e=0;
for (int i = 0; i < n + 6; i++) l[i] = -1;
/*memset(l,-1,sizeof(l)*);*/ }
inline void insert(int u,int v,int cap,LL cost){ //�����
	E[e].u=u; E[e].v=v; E[e].cap=cap; E[e].cost= cost; E[e].x=l[u]; l[u]=e++;
	E[e].u=v; E[e].v=u; E[e].cap=0  ; E[e].cost=-cost; E[e].x=l[v]; l[v]=e++;
}
int q[20*maxn],s,t, inq[maxn];LL dis[maxn];int eid[maxn];
void min_cost_max_flow(int src,int sink,int &cap,LL &cost){//0~n-1
	cost=cap=0;
	while( true ){ //��������
		//begin spfa
		for(int i=0;i<n + 10 ;i++) dis[i]=-INF; //-inf  ����
		s=t=0; q[t++]=src; inq[src]=1; dis[src]=0;
		while(s<t){
			int u=q[s++]; inq[u]=0;
			for(int p=l[u];p>=0;p=E[p].x){
				if( E[p].cap<=0 ) continue;
				int v=E[p].v;
				if( dis[v]<dis[u]+E[p].cost ){  //<
					dis[v]=dis[u]+E[p].cost; eid[v]=p;
					if( inq[v]==0 ){
						inq[v]=1; q[t++]=v;
					}
				}
			}
		} //end spfa
		if( dis[sink]<=-INF ) return;  //<=-inf
		int c=inf;
		for(int i=sink;i!=src;i=E[eid[i]].u) c=min(c,E[eid[i]].cap);
		cost+=dis[sink]*(LL)c;  cap+=c;
		for(int i=sink;i!=src;i=E[eid[i]].u) {
			int p=eid[i];  E[p].cap-=c; E[p^1].cap+=c;
		}
	}
}//*****************ģ�����*******************


/*
int main(){
	int n,m,u,v,cap,cost;
	while(scanf("%d%d",&n,&m)!=EOF ){
		init(); //��ʼ��
		for(int i=1;i<=m;i++){
			scanf("%d %d %d %d",&u,&v,&cap,&cost);
			insert(u,v,cap,cost);
		}
		min_cost_max_flow(0,n-1,cap,cost);
		printf("capicity: %d cost: %d\n",cap,cost);
	}
}
*/




int main()
{
    freopen("bl.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T, ca = 0;
    scanf("%d", &T);
    while (T--)
    {
        scanf("%d%d", &EN, &R);
        scanf("%d", &n);
        for (int k = 1; k <= n; k++)
            scanf("%d", v + k);
        R = min(R, EN);
        init();
        insert(0, 1, EN, 0);
        for (int k = 2; k <= n; k++)
            insert(0, k, R, 0);
        for (int k = 1; k < n; k++)
            insert(k, k + 1, EN - R, 0);
        for (int k = 1; k <= n; k++)
            insert(k, n + 1, EN, (LL)v[k]);
        int temp;
        LL ans;
        min_cost_max_flow(0,n + 1, temp, ans);
        printf("Case #%d: %I64d\n", ++ca, ans);
    }
    return 0;
}
