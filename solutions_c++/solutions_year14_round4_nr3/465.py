#include <cstdio>
#include <algorithm>
using namespace std;

using namespace std;

#define REP(i,a,b) for (int i = (a); i <= (b); i++)
#define REPD(i,a,b) for (int i = (a); i >=(b); i--)
#define FORI(i,n) REP(i,1,n)
#define FOR(i,n) REP(i,0,int(n)-1)
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define vi vector<int>
#define ll long long
#define SZ(x) int((x).size())
#define DBG(v) cerr << #v << " = " << (v) << endl;
#define FOREACH(i,t) for (auto i = t.begin(); i != t.end(); i++)
#define fi first
#define se second

int px[4] = {0,1,0,-1}, py[4] = {1,0,-1,0};

int w,h,b;
int t[111][555];


bool go(int x, int y, int dir, int vl) {
	//printf("go %d %d %d %d\n", x, y, dir, vl);
	bool fst=true;
	while (true) {
	//printf("go %d %d %d %d\n", x, y, dir, vl);
		t[x][y] = vl;
		if (y==1 && !fst) return false;
		if (y==h) return true;
		int nx = x+px[dir], ny=y+py[dir];
		if (t[nx][ny] == 0 || t[nx][ny] == vl) {
			x = nx;
			y = ny;
			dir = (dir+3) & 3;
		} else {
			dir = (dir+1) & 3;
		}
		fst=false;
	}
}

int test() {
	scanf("%d%d%d", &w, &h, &b);
	FORI(i,w) FORI(j,h) t[i][j] = 0;
	FOR(i,w+2) t[i][0] = t[i][h+1] = -1;
	FOR(i,h+2) t[0][i] = t[w+1][i] = -1;
	FOR(bb,b) {
		int x0,y0,x1,y1;
		scanf("%d%d%d%d", &x0, &y0, &x1, &y1);
		REP(i,x0+1,x1+1) REP(j,y0+1,y1+1) t[i][j]=-1;
	}
	/*
	FORI(i,w) {
		FORI(j,h) printf("%d ", t[i][j]);
		printf("\n");
	}
	*/
	int ret = 0;
	FORI(st,w) if (t[st][1]==0) {
		if (go(st,1,0,st)) ret++;
		/*
		FORI(i,w) {
			FORI(j,h) printf("%d ", t[i][j]);
			printf("\n");
		}
		*/
	}
	return ret;
}

int main() {
	int te;
	scanf("%d", &te);
	for (int tt = 1; tt <= te; tt++) {
		printf("Case #%d: %d\n", tt, test());
	}
	return 0;
}