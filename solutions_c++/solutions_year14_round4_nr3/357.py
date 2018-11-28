#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#define N 200010
#define M 2000010
#define oo 1000000000
using namespace std;
struct edge
{
	int next,v,flow;
}e[M];
int head[N],last[N],d[N],que[N],cnt,ans,s,t;
void addedge(int u,int v,int f)
{
	e[cnt].v = v;
	e[cnt].flow = f;
	e[cnt].next = head[u];
	head[u] = cnt ++;
}

void addEdge(int x,int y,int z)
{
    addedge(x,y,z);
    addedge(y,x,0);
}

int bfs()
{
	memset(d,-1,sizeof(d));
	d[s] = 0;
	int top = 0, tail = 1;
	que[0] = s;
	while(top < tail) {
		int u = que[top++];
		for(int i = head[u];i != -1; i = e[i].next) {
			if(e[i].flow > 0 && d[e[i].v] == -1) {
				d[e[i].v] = d[u] + 1;
				que[tail++] = e[i].v;
				if(e[i].v == t) break;
			}
		}
	}
	return d[t] != -1;
}

void dfs()
{
	for(int i = s; i <= t; i++) last[i] = head[i];
	int top = 1,tmp,x;
	que[1] = s;
	while(top) {
		x = que[top];
		if(x == t) {
			int minf = oo;
			for(int i = 1; i < top; i ++)
				if(e[last[que[i]]].flow < minf) {
					minf = e[last[que[i]]].flow;
					tmp = i;
				}
				for(int i = 1; i < top; i ++) {
					int m = last[que[i]];
					e[m].flow -= minf;
					e[m^1].flow += minf;
				}
			ans += minf;
			top = tmp;
			continue;
		}
		int i;
		for(i = last[x]; i != -1; i = e[i].next) 
			if(e[i].flow > 0 && d[e[i].v] == d[x] + 1) {
				que[++top] = e[i].v;
				break;
			}
		last[x] = i;
		if(last[x] == -1) {
			top --;
			last[que[top]] = e[last[que[top]]].next;
		}
	}
}

bool vis[510][510];
int map[510][510];
int dir[4][2] = {0,1,0,-1,1,0,-1,0};
int n,m;

bool check(int x,int y)
{
    return x >= 0 && x < n && y >= 0 && y < m && vis[x][y];
}

void solve()
{
    int r,x1,y1,x2,y2;
    scanf("%d%d%d",&n,&m,&r);
    memset(vis,true,sizeof(vis));
    while(r --) {
        scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
        for(int i = x1; i <= x2; i ++)
            for(int j = y1; j <= y2; j ++)
                vis[i][j] = false;
    }
	memset(head,-1,sizeof(head));
    memset(map,-1,sizeof(map));
    int cc = 0;
    for(int i = 0; i < n; i ++)
        for(int j = 0; j < m; j ++)
            if(vis[i][j]) map[i][j] = ++ cc;
	cnt = 0;
    s = 0,t = 2 * cc + 10;
    for(int i = 0; i < n; i ++)
        for(int j = 0; j < m; j ++)
            if(vis[i][j]) addEdge(map[i][j],map[i][j] + cc,1);
    for(int i = 0; i < n; i ++)
        if(vis[i][0]) {
            addEdge(s,map[i][0],1);
        }
    for(int i = 0; i < n; i ++)
        if(vis[i][m - 1]) {
            addEdge(map[i][m - 1],t,1);
        } 
    for(int i = 0; i < n; i ++)
        for(int j = 0; j < m; j ++) {
            if(!vis[i][j]) continue;
            int x,y;
            for(int k = 0; k < 4; k ++) {
                x = i + dir[k][0];
                y = j + dir[k][1];
                if(!check(x,y)) continue;
                addEdge(map[i][j] + cc,map[x][y],1);
                //cout << i << " " << j << " " << x << " " << y << endl;
            }
        }
	ans = 0;
	while(bfs()) dfs();
	printf("%d\n",ans);
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas = 1; cas <= T; cas ++) {
        printf("Case #%d: ",cas);
        solve();
    }
    return 0;
}
