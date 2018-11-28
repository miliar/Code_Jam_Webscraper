#include "sstream"
#include "iostream"
#include "cstdio"
#include "cstring"
#include "cmath"
#include "algorithm"
#include "vector"
#include "map"
#include "set"
#include "queue"
#include "deque"
#include "list"
#include "string"
#include "cassert"

using namespace std;

const long long INF = 1LL<<60;
const int MAXN = 10100;
const long long MOD = 1000002013LL;

struct Edge
{
	int v,next;
    long long cost,cap;
}edges[MAXN*400];

int alloc, N;
int G[MAXN];
int pre[MAXN];
long long dis[MAXN],road[MAXN];//pre[v]存点v的前一个 road[v]存这一条边   反边为^1
bool in[MAXN];

void addEdge(int u,int v,long long cost, long long cap)
{
	edges[alloc].v=v,edges[alloc].cost=cost,edges[alloc].cap=cap;
	edges[alloc].next=G[u];
	G[u]=alloc++;
}

void add(int u,int v, long long cost, long long cap)
{
	addEdge(u,v,cost,cap);
	addEdge(v,u,-cost,0);//-cost 0
}

bool spfa(int s,int t)//寻找一条到t的最短路  且要有流量的
{
	memset(in,0,sizeof(in));
	for(int i=0;i<=N+1;i++)dis[i]=INF;
	dis[s]=0;pre[s]=s;in[s]=1;
	queue<int>Q;Q.push(s);
	while(!Q.empty())
	{
		int u=Q.front();Q.pop();
		in[u]=0;
//        cout << "u" << u << dis[u] << endl;
		for(int son=G[u];son!=-1;son=edges[son].next)
		{
			int v=edges[son].v;
            long long cost=edges[son].cost,cap=edges[son].cap;
			if(cap&&cost+dis[u]<dis[v])
			{
				dis[v]=dis[u]+cost;
				pre[v]=u;
				road[v]=son;
				if(!in[v])
				{
					in[v]=1;
					Q.push(v);
				}
			}
		}
	}
	return dis[t]!=INF;
}

long long costFlow(int s,int t)
{
	long long totalcost = 0;
	while(spfa(s,t))
	{
		long long cap=INF;
		for(int i=t;i!=s;i=pre[i]) {
			cap=min(cap,edges[road[i]].cap);
 //           cout << i << " " << edges[road[i]].cost << endl;
        }
		for(int i=t;i!=s;i=pre[i])
		{
			edges[road[i]].cap-=cap;
			edges[road[i]^1].cap+=cap;
			totalcost+=cap*edges[road[i]].cost;//cap*
		}
  //      cout<<totalcost<<" "<<cap<<endl;
	}
	return totalcost;
}


int o[MAXN], e[MAXN], p[MAXN];
int ok[110][110];

void bfs(int m)
{
    memset(ok, 0, sizeof ok);
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < m; j++) {
            if (o[j] > e[i] || o[i] > e[j]) {
                continue;
            }
            ok[i][j] = 1;
        }
    }
    for (int k = 0; k < m; k++) {
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < m; j++) {
                if (ok[i][j]) continue;
                ok[i][j] = ok[i][k] && ok[k][j];
            }
        }
    }
}

int main()
{
    int T, t = 1;
    for (cin >> T; T--; ) {
        printf("Case #%d: ", t++);
        int n, m;
        int sum = 0;
        long long total = 0;
        scanf("%d%d", &n, &m);
        for (int i = 0; i < m; i++) {
            scanf("%d%d%d", &o[i], &e[i], &p[i]);
            sum += p[i];
            int k = e[i] - o[i];
            total += (long long)p[i]*(2*n-k+1)*k/2;
        }

        bfs(m);
        long long MAX_COST = (n*n+n-2)+10;
        N = 2*m;
        memset(G, -1, sizeof G);
        alloc = 0;
        for (int i = 0; i < m; i++) {
            int u = i+1;
            for (int j = 0; j < m; j++) {
                //if (o[j] > e[i] || o[i] > e[j]) {
                if (!ok[i][j] || o[j] > e[i]) {
                    continue;
                }
                int v = m+(j+1);
                int k = e[i] - o[j];
                //long long cost = MAX_COST - (2*n-k+1)*k/2;
                long long cost = (2*n-k+1)*k/2;
                if (cost < 0) {
                    cout << i << " " << j <<" " << e[i] << " " << o[j] << " " << cost << endl;
                }
                assert(cost >= 0);
                //cout<<u<<" -> "<<v<<" "<<cost<<endl;
                //add(u, v, cost, p[j]);
                add(u, v, cost, INF);
                //add(v, u, cost, INF);
            }
            add(0, u, 0, p[i]);
            add(m+u, N+1, 0, p[i]);
        }
        //long long c = costFlow(0, N+1) - MAX_COST*sum;
        long long c = costFlow(0, N+1);
        total -= c;
        total %= MOD;
        if (total < 0) {
            total += MOD;
        }
        printf("%lld\n", total);
    }
    return 0;
}

