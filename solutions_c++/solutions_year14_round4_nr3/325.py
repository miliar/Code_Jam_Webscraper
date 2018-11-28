#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <vector>

using namespace std;

#define FOR(prom, a, b) for(int prom = (a); prom < (b); prom++)
#define FORD(prom, a, b) for(int prom = (a); prom > (b); prom--)
#define FORDE(prom, a, b) for(int prom = (a); prom >= (b); prom--)

#define DRI(a) int a; scanf("%d ", &a);
#define DRII(a, b) int a, b; scanf("%d %d ", &a, &b);
#define DRIII(a, b, c) int a, b, c; scanf("%d %d %d ", &a, &b, &c);
#define DRIIII(a, b, c, d) int a, b, c, d; scanf("%d %d %d %d ", &a, &b, &c, &d);
//#define RI(a) scanf("%d ", &a);
#define RII(a, b) scanf("%d %d ", &a, &b);
#define RIII(a, b, c) scanf("%d %d %d ", &a, &b, &c);
#define RIIII(a, b, c, d) scanf("%d %d %d %d ", &a, &b, &c, &d);

#define PB push_back
#define MP make_pair

#define ll long long
#define ull unsigned long long

#define MM(co, cim) memset((co), (cim), sizeof((co)))

#define DEB(x) cerr << ">>> " << #x << " : " << x << endl;

#define UP 0
#define DO 1
#define LE 2
#define RI 3


bool mp[107][507];
bool vis[107][507];
int W,H;
int res;

bool flow(int x, int y, int dir) {
	//cout << "run " << x << " " << y << endl;
	if(mp[x][y]) return false;
	if(vis[x][y]) return false;
	mp[x][y] = true;
	vis[x][y] = true;
	if(y == H) {
		res++;
		return true;
	}
	switch(dir) {
	case UP:
		if(!flow(x-1,y,LE))
			if(!flow(x,y+1,UP))
				if(!flow(x+1,y,RI))
					return mp[x][y] = false;
		break;
	case DO:
		if(!flow(x+1,y,RI))
			if(!flow(x,y-1,DO))
				if(!flow(x-1,y,LE))
					return mp[x][y] = false;
		break;
	case LE:
		if(!flow(x,y-1,DO))
			if(!flow(x-1,y,LE))
				if(!flow(x,y+1,UP))
					return mp[x][y] = false;
		break;
	case RI:
		if(!flow(x,y+1,UP))
			if(!flow(x+1,y,RI))
				if(!flow(x,y-1,DO))
					return mp[x][y] = false;
		break;
	}
	return true;
}

int main ()
{
  DRI(T);
  FOR(t,1,T+1) {
  	MM(mp,false);
  	RII(W,H);
  	DRI(B);
  	FOR(i,0,W+3) mp[i][0] = mp[i][H+1] = true;
  	FOR(i,0,H+3) mp[0][i] = mp[W+1][i] = true;
  	FOR(i,0,B) {
  		DRIIII(x0,y0,x1,y1);
  		FOR(x,x0+1,x1+2) FOR(y,y0+1,y1+2) mp[x][y] = true;
  	}
  	res = 0;
  	FOR(stx,1,W+1) {
	  	MM(vis,false);
  		flow(stx,1,UP);
		}
		printf("Case #%d: %d\n", t, res);
  }
  return 0;
}
