#include<iostream>
#include<string>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<ctime>
#include<algorithm>
#include<map>
using namespace std;

struct edge { int nxt, des, cap, flow, rev; };
#define N 210000
#define M 2100000
#define L 510
edge e[M];
int dis[N], que[N], hd[N], ce[N], vst[L][L];
const int dr[] = { 1, -1, 0, 0 };
const int dc[] = { 0, 0, 1, -1 };
int n, m, nr, nc, cnt;
const int ss = 200000;
const int tt = 200010;
const int INF_FLOW = 10000;

inline int getmin(int x, int y) { return x<y?x:y; }

void insert(int x, int y, int z) {
	++cnt; e[cnt].des=y; e[cnt].nxt=hd[x]; hd[x]=cnt;
	e[cnt].rev=cnt+1; e[cnt].cap=z; e[cnt].flow=0; 
	++cnt; e[cnt].des=x; e[cnt].nxt=hd[y]; hd[y]=cnt;
	e[cnt].rev=cnt-1; e[cnt].cap=0; e[cnt].flow=0;
}

int dinic_dfs(int s, int t, int mf) {
	int i, f, tf;
	if (dis[s]==dis[t]) return s==t?mf:0;
	for (i=ce[s], f=mf; f&&i; i=f?e[i].nxt:i)
		if (e[i].cap && dis[e[i].des]==dis[s]+1) {
			tf=dinic_dfs(e[i].des, t, getmin(f, e[i].cap));
			e[i].cap-=tf; e[i].flow+=tf; e[e[i].rev].cap+=tf; e[e[i].rev].flow-=tf; f-=tf;
		}
	ce[s]=i; return mf-f;
}

int dinic(int s, int t) {
	int i, f, u, head, tail;
	for (f=0; 1; ) {
		memset(dis, -1, sizeof(dis)); memcpy(ce, hd, sizeof(hd));
		for (head=tail=dis[u=s]=0; head<=tail; u=que[++head]) 
			for (i=hd[u]; i; i=e[i].nxt) if (e[i].cap && dis[e[i].des]<0) 
				dis[que[++tail]=e[i].des] = dis[u]+1;
		if (dis[t]<0) return f;
		f+=dinic_dfs(s, t, INF_FLOW);
	}
}

inline int valid(int tr, int tc) {
	if (tr<0 || tr>=nr) return 0;
	if (tc<0 || tc>=nc) return 0;
	if (vst[tr][tc]) return 0;
	return 1;
}

void conduct() {
	int i, j, k, sc, sr, lc, lr, tr, tc;
	scanf("%d%d%d", &nc, &nr, &m);
	memset(vst, 0, sizeof(vst));
	for (i=0; i<m; ++i) {
		scanf("%d%d%d%d", &sc, &sr, &lc, &lr);
		for (j=sr; j<=lr; ++j) for (k=sc; k<=lc; ++k) vst[j][k]=1;
	}
	memset(hd, 0, sizeof(hd)); cnt=0; n=nc*nr;
	for (i=0; i<nr; ++i) for (j=0; j<nc; ++j) {
		insert(i*nc+j, i*nc+j+n, 1);
		for (k=0; k<4; ++k) {
			tr=i+dr[k]; tc=j+dc[k];
			if (valid(tr, tc)) insert(i*nc+j+n, tr*nc+tc, 1);
		}
	}
	for (i=0; i<nc; ++i) if (!vst[0][i]) insert(ss, i, 1);
	for (i=0; i<nc; ++i) if (!vst[nr-1][i]) insert((nr-1)*nc+i+n, tt, 1);
	printf("%d\n", dinic(ss, tt));
}

int main() {
	int time; scanf("%d", &time);
	for (int i=1; i<=time; ++i) {
		printf("Case #%d: ", i);
		conduct();
	}
	return 0;
}
