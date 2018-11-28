// Template.cpp by kevinptt 20150108
#include <bits/stdc++.h>
/*
#include <cstdio>
#include <cstring>
#include <cmath>

#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
#include <list>
#include <map>
#include <set>

#include <iostream>
// */
using namespace std;

#define REP(I, N) for(int I=0; I<(int)(N); ++I)
#define REP1(I, N) for(int I=1; I<=(int)(N); ++I)
#define REPP(I, A, B) for(int I=(A); I<(int)(B); ++I)
#define REPR(I, N) for(int I=N-1; I>=0; --I)
#define RI(X) scanf("%d", &(X))
#define RII(X, Y) scanf("%d%d", &(X), &(Y))
#define RIII(X, Y, Z) scanf("%d%d%d", &(X), &(Y), &(Z))
#define DRI(X) int X; scanf("%d", &X)
#define DRII(X, Y) int X, Y; scanf("%d%d", &X, &Y)
#define DRIII(X, Y, Z) int X, Y, Z; scanf("%d%d%d", &X, &Y, &Z)
#define MP make_pair
#define PB push_back
#define MSET(x, y) memset(x, y, sizeof(x))
#define F first
#define S second
typedef long long ll;
typedef pair<int,int> pii;

/***************************************************************/

char _dir[] = "v>^<";
int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};
char mapp[105][105];
int edge[10005][4];
vector<int> node;
int curr_dir[10005];
bool loop[10005];
bool vst[10005];
int ans;

inline int dir(char c) {
	REP(i, 4) if( c==_dir[i] ) return i;
	return -1;
}

void dfs(int curr) {
	if( loop[curr] ) return;
	if( vst[curr] ) {
		loop[curr] = true;
		return;
	}
	vst[curr] = true;

	int nxt = edge[curr][curr_dir[curr]];
	if( ~nxt ) {
		dfs(nxt);
		loop[curr] = true;
	} else {
		REP(d, 4) {
			nxt = edge[curr][d];
			if( ~nxt ) {
				dfs(nxt);
				++ans;
				curr_dir[curr] = d;
				loop[curr] = true;
				break;
			}
		}
	}
}

void solve(int n, int m) {
	MSET(edge, -1);
	node.clear();
	REP(i, n)
		REP(j, m)
			if( mapp[i][j] != '.' ) {
				node.PB(i*m+j);
				curr_dir[i*m+j] = dir(mapp[i][j]);
				bool has_edge = false;
				REP(d, 4)
					for(int x=i+dx[d], y=j+dy[d]; x>=0 && y>=0 && x<n && y<m; x+=dx[d], y+=dy[d]) {
						if( mapp[x][y] != '.' ) {
							has_edge = true;
							edge[i*m+j][d] = x*m+y;
							break;
						}
					}
				if( !has_edge ) {
					ans = -1;
					return;
				}
			}
	
	MSET(loop, false);
	int curr;
	ans = 0;
	REP(i, node.size()) {
		curr = node[i];
		if( loop[curr] ) continue;
		else {
			MSET(vst, false);
			dfs(curr);
		}
		/*
		if( loop[edge[curr][curr_dir[curr]]] )
			loop[curr] = true;
		else {
			REP(d, 4)
				if( loop[edge[curr][d]] ) {
					curr_dir[curr] = d;
					loop[curr] = true;
					break;
				}
				else if( curr_dir[edge[curr][d]] == (d+2)%4 ) {
					curr_dir[curr] = d;
					loop[curr] = loop[edge[curr][d]];
					break;
				}
		}*/
	}
}

int main() {
#ifdef KEVINPTT
	//freopen("a.in", "r", stdin);
	//freopen("a.ans", "w", stdout);
#endif
	DRI(T);
	REP1(casen, T) {
		DRII(n, m);
		REP(i, n)
			scanf("%s", mapp[i]);
		solve(n, m);
		if( ans>=0 )
			printf("Case #%d: %d\n", casen, ans);
		else
			printf("Case #%d: IMPOSSIBLE\n", casen);
	}
	
	return 0;
}

