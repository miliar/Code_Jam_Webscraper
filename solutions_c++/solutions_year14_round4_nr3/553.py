#include <stdio.h>
#include <string.h>
#include <climits>
#include <algorithm>
using namespace std;
const int MAXN=102000,MAXM=1040000;

struct Dinic {
struct edge {
int x,y; //两个顶点
int c; //容量
int f; //当前流量
edge *next,*back; //下一条边，反向边
edge(int x,int y,int c,edge *next):x(x),y(y),c(c),f(0),next(next),back(0) {}
void *operator new(size_t, void *p) {
return p;
}
}*E[MAXN],*data; //E[i] 保存顶点 i 的边表
char storage[2*MAXM *sizeof(edge)];
int S,T; //源、汇
int Q[MAXN]; //DFS 用到的 queue
int D[MAXN]; //距离标号，-1 表示不可达
void DFS() {
memset(D,-1,sizeof(D));
int head=0,tail=0;
Q[tail++]=S;
D[S]=0;
for(;;) {
int i=Q[head++];
for(edge *e=E[i]; e; e=e->next) {
if(e->c==0)continue;
int j=e->y;
if(D[j]==-1) {
D[j]=D[i]+1;
Q[tail++]=j;
if(j==T)return;
}
}
if(head==tail)break;
}
}
edge *cur[MAXN]; //当前弧
edge *path[MAXN]; //当前找到的增广路
int flow() {
int res=0; //结果，即总流量
int path_n; //path 的大小
for(;;) {
DFS();
if(D[T]==-1)break;
memcpy(cur,E,sizeof(E));
path_n=0;
int i=S;
for(;;) {
if(i==T) { //已找到一条增广路，增广之
int mink=0;
int delta=INT_MAX;
for(int k=0; k<path_n; ++k) {
if(path[k]->c < delta) {
delta = path[k]->c;
mink=k;
}
}
for(int k=0; k<path_n; ++k) {
path[k]->c -= delta;
path[k]->back->c += delta;
}
path_n=mink; //回退
i=path[path_n]->x;
res+=delta;
}
edge *e;
for(e=cur[i]; e; e=e->next) {
if(e->c==0)continue;
int j=e->y;
if(D[i]+1==D[j])break; //找到一条弧，加到路径里
}
cur[i]=e; //当前弧结构，访问过的不能增广的弧不会再访问
if(e) {
path[path_n++]=e;
i=e->y;
} else { //该节点已没有任何可增广的弧，从图中删去，回退一步
D[i]=-1;
if(path_n==0)break;
path_n--;
i=path[path_n]->x;
}
}
}
return res;
}
int cut(int *s) {
int rst=0;
for(int i=0; i<MAXN; ++i)
if(D[i]==-1&&E[i])
s[rst++]=i;
return rst;
}
void init(int _S,int _T) {
S=_S,T=_T;
data=(edge *)storage;
memset(E,0,sizeof(E));
}
void add_edge(int x,int y,int w) { //加进一条 x 至 y 容量为 w 的边，需要保证 0<=x,y<MAXN，0\
<w<=INT_MAX
E[x]=new((void *)data++) edge(x,y,w,E[x]);
E[y]=new((void *)data++) edge(y,x,0,E[y]);
E[x]->back = E[y];
E[y]->back = E[x];
}
};

const int MAN = 101, MAM = 501;

int a[MAN][MAM], in[MAN][MAM], out[MAN][MAM];
int W, H, B;

int dx[] = {1, -1, 0, 0},
	dy[] = {0, 0, -1, 1};

bool valid(int x, int y) {
	return x >= 0 && x < W && y >= 0 && y < H && a[x][y] == 0;
}

Dinic dinic;

int main() {
	int T;
	freopen("x.txt", "r", stdin);freopen("w.txt", "w", stdout);
	
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		memset(a, 0, sizeof(a));
		memset(in, 0, sizeof(in));
		memset(out, 0, sizeof(out));
		scanf("%d%d%d", &W, &H, &B);
		int S=0, T=1;
		dinic.init(S, T);
		int N = 2;
		for (int i = 0; i < B; i++) {
			int x, xx, y, yy;
			scanf("%d%d%d%d", &x, &y, &xx, &yy);
			for (int j = x; j <= xx; j++) {
				for (int k = y; k <= yy; k++) {
					a[j][k] = 1;
				}
			}
		}
		for (int i = 0; i < W; i++) {
			for (int j = 0; j < H; j++) {
				if (a[i][j] == 0) {
					in[i][j] = N++;
					out[i][j] = N++;
				}
				
			}
		}
		/*
		for (int i = 0; i < W; i++) {
			for (int j = 0; j < H; j++) {
				printf("%d ", in[i][j]);
			}
			puts("");
		}
		for (int i = 0; i < W; i++) {
			for (int j = 0; j < H; j++) {
				printf("%d ", out[i][j]);
			}
			puts("");
		}
		*/
		
		for (int i = 0; i < W; i++) {
			for (int j = 0; j < H; j++) {
				if (a[i][j]) continue;
				dinic.add_edge(in[i][j], out[i][j], 1);
				for (int k = 0; k < 4; k++) {
					int x = i + dx[k], y = j + dy[k];
					if (!valid(x, y)) continue;
					// if (i != 1 && j != 1)
					
					dinic.add_edge(out[x][y], in[i][j], 1);
					dinic.add_edge(out[i][j], in[x][y], 1);
				}
			}
		}
		for (int i = 0; i < W; i++) {
			if (a[i][0] == 0) {
				dinic.add_edge(S, in[i][0], 1);
			}
			if (a[i][H-1] == 0) {
				dinic.add_edge(out[i][H-1], T, 1);
			}
		}
		int ans = dinic.flow();
		printf("Case #%d: %d\n", cas, ans);
	}
}
