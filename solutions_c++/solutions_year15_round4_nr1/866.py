#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <queue>
using namespace std;
#define ll long long
#define pii pair<int,int>

void SetIO(){
	char in[] = "A-large.in";
	char out[] = "A-large.out";
	freopen(in,"r",stdin);
	freopen(out,"w",stdout);
}

const int N = 110;
int T;
int n,m;
char g[N][N];
bool ok[N][N];

int dir(char c){
	if(c == '>') return 0;
	if(c == 'v') return 1;
	if(c == '<') return 2;
	return 3;
}
int dx[] = {0,1,0,-1};
int dy[] = {1,0,-1,0};

bool In(int x,int y){
	return 1 <= x && x <= n && 1 <= y && y <= m;
}

bool find(int x,int y){
	for(int d=0;d<4;++d)
		for(int nx=x+dx[d],ny=y+dy[d];In(nx,ny);){
			if(g[nx][ny] != '.')
				return true;
			nx = nx + dx[d];
			ny = ny + dy[d];
		}
	return false;
}

int Out[N][N];
void ff(int x,int y){
	int d = dir(g[x][y]);
	for(int nx=x+dx[d],ny=y+dy[d];In(nx,ny);){
		if(g[nx][ny] != '.'){
			Out[x][y]++;
			return;
		}
		nx = nx + dx[d];
		ny = ny + dy[d];
	}
}


int run(){
	for(int i=1;i<=n;++i)
		for(int j=1;j<=m;++j)
			Out[i][j] = 0;
	for(int i=1;i<=n;++i)
		for(int j=1;j<=m;++j)
			if(g[i][j] != '.' && !find(i,j))
				return -1;
	for(int i=1;i<=n;++i)
		for(int j=1;j<=m;++j)
			ff(i,j);
	int ret = 0;
	for(int i=1;i<=n;++i)
		for(int j=1;j<=m;++j)
			if(g[i][j] != '.' && Out[i][j] == 0)
				ret++;
	return ret;
}

int main(){
	SetIO();
	scanf("%d",&T);
	for(int re=1;re<=T;++re){
		scanf("%d%d",&n,&m);
		for(int i=1;i<=n;++i)
			scanf("%s",g[i] + 1);
		int gt = run();
		printf("Case #%d: ",re);
		if(gt == -1)
			puts("IMPOSSIBLE");
		else printf("%d\n",gt);
	}
	return 0;
}


