#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <complex>
#include <cassert>

using namespace std;

typedef long long ll;
typedef vector<int> VI;
typedef pair<int,int> PII;

#define REP(i,s,t) for(int i=(s);i<(t);i++)
#define FILL(x,v) memset(x,v,sizeof(x))

const int INF = (int)1E9;
#define MAXN 4005
#define MAXFN (MAXN*1005*2)
#define MAXM (MAXFN*5+2005)
int FN, S, T; // set S,T,FN manually before run!
int L, adj[MAXFN];
int dst[MAXFN], gap[MAXFN];
struct llist{
	int id,next,c,f;
	llist(){}
	llist(int _id,int _c,int _next) {id=_id;c=_c;f=0;next=_next;}
} lists[2*MAXM];
inline void insertList(int &a, int b, int c){ 
	lists[L] = llist(b,c,adj[a]);
	adj[a] = L++; 
}
inline void insertEdge(int a, int b, int c){ 
	insertList(a,b,c);
	insertList(b,a,0);
}
void bfs(){
	REP(i,0,FN) dst[i] = FN;
	dst[T] = 0; // bfs from T
	FILL(gap, 0); 
	gap[0] = FN;	// FN nodes with gap 0
	queue<int> que; que.push(T);
	while(!que.empty()){
		int x = que.front(); que.pop();
		int t = adj[x];
		while(t!=-1){
			if(t&1){ // back edge
				int y = lists[t].id;
				if(dst[y]==FN){
					dst[y] = dst[x]+1;
					gap[dst[y]]++;
					que.push(y);
				}
			}
			t = lists[t].next;
		}
	}
}
int sendflow(int x, int inflow){
	if(x==T) return inflow;
	int outflow = inflow, delta = 0, minh = FN-1;
	int t = adj[x];
	while(t!=-1){
		int y = lists[t].id;
		if(lists[t].c != lists[t].f){
			if(dst[x]==dst[y]+1){
				delta = sendflow(y, min(outflow, lists[t].c-lists[t].f));
				lists[t].f += delta;
				lists[t^1].f -= delta;
				outflow -= delta;
				if(dst[S]==FN) return inflow-outflow; // no more flow, cannot advance
				if(outflow==0) break;
			}
			minh = min(minh, dst[y]);
		}
		t = lists[t].next;
	}
	if(inflow==outflow){ // no exit flow possible, relabel
		gap[dst[x]]--;
		if(gap[dst[x]]==0) dst[S] = FN; // exit immediately 
		dst[x] = minh + 1;
		gap[dst[x]]++;
	}
	return inflow-outflow;
}
int sap(){ // initialize f=0 if rerun
	int maxflow = 0;
	bfs();
	while(dst[S]<FN) maxflow += sendflow(S, INF);
	return maxflow;
}

int W,H,B;
int ys[MAXN], Y;
struct bd{
	int x1,y1,x2,y2;
	bd(){}
	bd(int _x1, int _y1, int _x2, int _y2){
		x1 = _x1; y1 = _y1; x2 = _x2; y2 = _y2;
	}
} b[1005];
bool blk[1005][MAXN];
int dir[4][2] = {-1,0,1,0,0,-1,0,1};

int id(int x, int y){
	return y*W+x;
}
int oid(int x, int y){
	return y*W+x  +W*Y;
}
int main(){
	int cs;
	cin >> cs;
	REP(csn,1,cs+1){
		printf("Case #%d: ", csn);
		cin >> W >> H >> B;
		if(csn==26){
			//cerr<<W<<" " <<H << " " << B << endl;
		}
		Y = 0;
		REP(i,0,B){
			int x1,y1,x2,y2;
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			b[i] = bd(x1,y1,x2,y2);
			/*
			ys[Y++] = y1; 
			if(y1-1>=0) ys[Y++] = y1-1;
			if(y1+1<H) ys[Y++] = y1+1;
			ys[Y++] = y2;
			if(y2+1<H) ys[Y++] = y2+1;
			if(y2-1>=0) ys[Y++] = y2-1;
			*/
		}
		/*
		ys[Y++] = 0;
		ys[Y++] = H-1;
		sort(ys,ys+Y);
		Y = unique(ys,ys+Y)-ys;
		*/
		Y = H;
		FILL(blk,0);
		REP(i,0,B){
			//b[i].y1 = lower_bound(ys,ys+Y,b[i].y1)-ys;
			//b[i].y2 = lower_bound(ys,ys+Y,b[i].y2)-ys;
			REP(p,b[i].x1,b[i].x2+1){
				REP(q,b[i].y1,b[i].y2+1){
					blk[p][q] = 1;
				}
			}
		}
		L = 0;
		FILL(adj,-1);
		REP(x,0,W) REP(y,0,Y){
			if(blk[x][y]) continue;
			insertEdge(id(x,y),oid(x,y), y==Y-1?1005:1);
			REP(k,0,4){
				int nx = dir[k][0]+x, ny = dir[k][1]+y;
				if(nx<0||ny<0||nx>=W||ny>=Y||blk[nx][ny]) continue;
				insertEdge(oid(x,y),id(nx,ny),1);
			}
		}
		S = W*Y*2; T = S+1; FN = T+1;
		assert(FN<MAXFN);
		assert(L<MAXM*2);
		REP(x,0,W){
			if(!blk[x][0]) insertEdge(S,id(x,0),1);
			if(!blk[x][Y-1]) insertEdge(oid(x,Y-1),T,1005);
		}
		int ans = sap();
		printf("%d\n", ans);
	}
	return 0;
}