#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <cstring>
#include <map>
#include <cmath>
#include <vector>
#include <set>
#include <stack>
#include <queue>


using namespace std;

int T;
int cas;
int N,M,B;
struct XD{
	int to,w,re;
	XD(int a,int b,int c){
		to = a, w = b, re = c;
	}
};
vector<XD> adj[100100];
int st,ed;
int use[1005][1005];
int dir[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};

void build()
{
	st = 0, ed = M*N*2+1;
	for( int i = st; i <= ed; i++ )
		adj[i].clear();
	for( int i = 0; i < N; i++ ){
		if( use[i][0] == 0 ){
			int nxt = i*M+1;
			adj[st].push_back(XD(nxt,1,int(adj[nxt].size())));
			adj[nxt].push_back(XD(st,0,int(adj[st].size())-1));
		}
		if( use[i][M-1] == 0 ){
			int nxt = i*M+M-1+1+M*N;
			adj[nxt].push_back(XD(ed,1,int(adj[ed].size())));
			adj[ed].push_back(XD(nxt,0,int(adj[nxt].size())-1));
		}
	}

	for( int i = 0; i < N; i++ ){
		for( int j = 0; j < M; j++ ){
			if( use[i][j] == 0 ){
				int now = i*M+j+1;
				int nxt = i*M+j+1+M*N;
				adj[now].push_back(XD(nxt,1,int(adj[nxt].size())));
				adj[nxt].push_back(XD(now,0,int(adj[now].size())-1));
				now = nxt;
				for( int k = 0; k < 4; k++ ){
					int ii = i+dir[k][0];
					int jj = j+dir[k][1];
					//now = nxt;
					if( ii >= 0 && ii < N && jj >= 0 && jj < M ){
						if( use[ii][jj] == 0 ){
							nxt = ii*M+jj+1;
							adj[now].push_back(XD(nxt,1,int(adj[nxt].size())));
							adj[nxt].push_back(XD(now,0,int(adj[now].size())-1));
						}
					}
				}
			}
		}
	}
}
int vis[100100];
int dfs(int v)
{
	vis[v] = 1;
	if( v == ed ){
		return 1;
	}
	for( int i = 0; i < int(adj[v].size()); i++ ){
		int nxt = adj[v][i].to;
		int ww = adj[v][i].w;
		int rr = adj[v][i].re;
		if( vis[nxt] == 0 && ww > 0 ){
			int tmp = dfs(nxt);
			if( tmp == 1 ){
				adj[v][i].w--;
				adj[nxt][rr].w++;
				return 1;
			}
		}
	}
	return 0;
}


void solve()
{
	int f=0;
	while(true){
		memset(vis,0,sizeof(vis));
		int tmp = dfs(st);
		//if(1)break;
		if( tmp != 1 )break;
		f++;
	}

	printf("Case #%d: %d\n",cas,f);
}



int main()
{
	scanf(" %d",&T);

	int l,r,L,R;
	for( cas = 1; cas <= T; cas++ ){
		scanf(" %d %d %d",&N,&M,&B);
		memset(use,0,sizeof(use));
		for( int i = 0; i < B; i++ ){
			scanf(" %d %d %d %d",&l,&r,&L,&R);
			for( int x = l; x <= L; x++ )
				for( int y = r; y <= R; y++ )
					use[x][y] = 1;
		}


		build();
		solve();
	}

	return 0;
}