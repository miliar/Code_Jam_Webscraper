#include <stdio.h>
#include <string.h>
#include <climits>
#include <algorithm>
using namespace std;
const int MAXN=102000,MAXM=1040000;

struct Dinic {
struct edge {
int x,y; //��������
int c; //����
int f; //��ǰ����
edge *next,*back; //��һ���ߣ������
edge(int x,int y,int c,edge *next):x(x),y(y),c(c),f(0),next(next),back(0) {}
void *operator new(size_t, void *p) {
return p;
}
}*E[MAXN],*data; //E[i] ���涥�� i �ı߱�
char storage[2*MAXM *sizeof(edge)];
int S,T; //Դ����
int Q[MAXN]; //DFS �õ��� queue
int D[MAXN]; //�����ţ�-1 ��ʾ���ɴ�
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
edge *cur[MAXN]; //��ǰ��
edge *path[MAXN]; //��ǰ�ҵ�������·
int flow() {
int res=0; //�������������
int path_n; //path �Ĵ�С
for(;;) {
DFS();
if(D[T]==-1)break;
memcpy(cur,E,sizeof(E));
path_n=0;
int i=S;
for(;;) {
if(i==T) { //���ҵ�һ������·������֮
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
path_n=mink; //����
i=path[path_n]->x;
res+=delta;
}
edge *e;
for(e=cur[i]; e; e=e->next) {
if(e->c==0)continue;
int j=e->y;
if(D[i]+1==D[j])break; //�ҵ�һ�������ӵ�·����
}
cur[i]=e; //��ǰ���ṹ�����ʹ��Ĳ�������Ļ������ٷ���
if(e) {
path[path_n++]=e;
i=e->y;
} else { //�ýڵ���û���κο�����Ļ�����ͼ��ɾȥ������һ��
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
void add_edge(int x,int y,int w) { //�ӽ�һ�� x �� y ����Ϊ w �ıߣ���Ҫ��֤ 0<=x,y<MAXN��0\
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
