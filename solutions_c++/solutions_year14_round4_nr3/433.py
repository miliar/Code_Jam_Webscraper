#include <stdio.h>
#include <memory.h>
#include <vector>
#define MH 500
#define MW 100
#define MN 1+MH*MW*2+1
using namespace std;
struct EDGE {
	int p, f, c;
	EDGE(int _p = 0, int _f = 0, int _c = 0) {
		p = _p; f = _f; c = _c;
	}
};
int W, H, B;
bool d[MH][MW];
int n;
vector<EDGE> E;
vector<int> l[MN];
void help(int p, int q)
{
	E.push_back(EDGE(q,0,1));
	l[p].push_back(E.size()-1);
	E.push_back(EDGE(p,1,1));
	l[q].push_back(E.size()-1);
}
int qu[MN], qs, qe;
bool vis[MN]; int path[MN];
bool bfs()
{
	int p, i, q;
	
	memset(vis,0,sizeof(vis));
	qs = qe = 0;
	qu[qe++] = 0; vis[0] = 1;
	while (qs < qe) {
		p = qu[qs++];
		for (i = 0; i < l[p].size(); i++) {
			if (E[l[p][i]].f < E[l[p][i]].c) {
				q = E[l[p][i]].p;
				if (vis[q]) continue;
				qu[qe++] = q; vis[q] = 1; path[q] = l[p][i];
			}
		}
	}
	if (vis[1+W*H*2+0]) {
		for (p = 1+W*H*2+0; p != 0; p = E[path[p]^1].p) {
			E[path[p]].f++;
			E[path[p]^1].f--;
		}
		return true;
	}
	else return false;
}
int main()
{
	freopen("input.txt","r",stdin);
	FILE *out=fopen("output.txt","w");
	int t, T, i, j, k;
	int x0, y0, x1, y1;
	
	scanf("%d",&T);
	for (t = 1; t <= T; t++) {
		printf("%d\n",t);
		fprintf(out,"Case #%d: ",t);
		scanf("%d%d%d",&W,&H,&B);
		memset(d,0,sizeof(d));
		for (i = 0; i < B; i++) {
			scanf("%d%d%d%d",&x0,&y0,&x1,&y1);
			for (j = y0; j <= y1; j++) {
				for (k = x0; k <= x1; k++)
					d[j][k] = 1;
			}
		}
		E.clear();
		for (i = 0; i < MN; i++)
			l[i].clear();
		n = 1+W*H*2+1;
		for (i = 0; i < W; i++)
			help(0,1+i);
		for (i = 0; i < H; i++) {
			for (j = 0; j < W; j++) {
				if (d[i][j] == 0)
					help(1+i*W+j,1+H*W+i*W+j);
				if (j-1 >= 0)
					help(1+H*W+i*W+j,1+i*W+(j-1));
				if (j+1 < W)
					help(1+H*W+i*W+j,1+i*W+(j+1));
				if (i-1 >= 0) // TODO : ?
					help(1+H*W+i*W+j,1+(i-1)*W+j);
				if (i+1 < H)
					help(1+H*W+i*W+j,1+(i+1)*W+j);
			}
		}
		for (i = 0; i < W; i++)
			help(1+H*W+(H-1)*W+i,1+H*W*2+0);
		printf("hi\n");
		int r = 0;
		while (bfs()) r++;
		fprintf(out,"%d\n",r);
	}
	fclose(out);
	return 0;
}