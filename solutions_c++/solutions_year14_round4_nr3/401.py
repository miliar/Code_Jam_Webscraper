#include <bits/stdc++.h>



using namespace std;





#define fr(i,a,b) for(int i=a;i<b;++i)
typedef long long ll;
typedef pair<int,int> pii;
#define F first
#define S second
#define mp make_pair
const int oo = 0x3f3f3f3f;

int t,r,c,b;
int gr[110][510];

int S, T;
int in[110][510], out[110][510];
int nno;
int dx[] = {0,1};
int dy[] = {1,0};

const int maxv = 110*510*4;
const int maxe = 5000000;
int level[maxv], fila[maxv], adj[maxv], copy_adj[maxv];
int from[maxe], to[maxe], cap[maxe], ant[maxe], pa;

void add(int f, int t, int c){
	from[pa] = f, to[pa] = t, cap[pa] = c, ant[pa] = adj[f]; adj[f] = pa++;
	from[pa] = t, to[pa] = f, cap[pa] = 0, ant[pa] = adj[t]; adj[t] = pa++;
}

int bfs(int so, int si){
	memset(level, -1, sizeof level);
	level[so] = 0;
	int pos = 0, tam = 0;
	fila[tam++] = so;
	while(pos < tam){
		int now = fila[pos++];
		for(int i = adj[now]; ~i; i = ant[i]){
			if(cap[i] && level[to[i]] == -1){
				level[to[i]] = level[now]+1;
				fila[tam++] = to[i];
			}
		}
	}
	return level[si] != -1;
}


int dfs(int no, int si, int fl){
	if(no == si) return fl;
	for(int &i = copy_adj[no]; i >= 0; i = ant[i]){
		if(cap[i] && level[no]+1 == level[to[i]]){
			int nflow = dfs(to[i], si, min(fl,cap[i]));
			if(nflow){
				cap[i] -= nflow, cap[i^1] += nflow;
				return nflow;
			}
		}
	}
	return 0;
}


int maxflow(int so, int si){
	int mf = 0;
	while(true){
		if(bfs(so, si)){
			memcpy(copy_adj, adj, sizeof adj);
			while(true){
				int add = dfs(so, si, 1<<30);
				if(add) mf += add;
				else break;
			}
		}
		else break;
	}
	return mf;
}


void limpa(){
	memset(adj, -1, sizeof adj);
	pa = 0;
}


bool valid(int a, int b){
	if(a >= 0 && a < r && b >= 0 && b < c) return true;
	return false;
}

int main(){
	scanf("%d",&t);
	fr(cas,1,t+1){
		limpa();
		memset(gr, 0, sizeof gr);
		scanf("%d %d %d",&r,&c,&b);
		fr(k,0,b){
			int x0, x1,y0, y1;
			scanf("%d %d %d %d",&x0,&y0,&x1,&y1);
			fr(i,x0,x1+1){
				fr(j,y0,y1+1){
					gr[i][j] = 1;
				}
			}
		}
		nno = 0;
		S = nno++;
		fr(i,0,r){
			fr(j,0,c){
				in[i][j] = nno++;
				out[i][j] = nno++;
			}
		}
		T = nno++;
		fr(i,0,r){
			if(gr[i][0] == 0){
//				printf("S -> %d\n",i);
				add(S,in[i][0],1);
			}
			if(gr[i][c-1] == 0){
//				printf("%d -> T\n",i);
				add(out[i][c-1],T,1);
			}
		}
		fr(i,0,r){
			fr(j,0,c){
				fr(k,0,2){
					int ni = i + dx[k], nj = j + dy[k];
					if(valid(ni,nj) && gr[i][j] == 0 && gr[ni][nj] == 0){
//						printf("%d %d -> %d %d\n",i,j,ni,nj);
						add(out[i][j],in[ni][nj],1);
						add(out[ni][nj],in[i][j],1);
					}
				}
				if(gr[i][j] == 0) add(in[i][j],out[i][j],1);
			}
		}
		printf("Case #%d: %d\n",cas,maxflow(S,T));
	}
	return 0;
}























