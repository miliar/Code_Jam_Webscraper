#include<cstdio>
#include<vector>
#include<algorithm>
#include<cstring>
#include<assert.h>
using namespace std;
#define FOR(i,a,b) for(int i = a; i <= b; ++i)
#define FORD(i,a,b) for(int i = a; i >= b; --i)
#define RI(i,n) FOR(i,1,n)
#define REP(i,n) FOR(i,0,(n)-1)
#define mini(a,b) a=min(a,b)
#define maxi(a,b) a=max(a,b)
#define mp make_pair
#define pb push_back
#define st first
#define nd second
#define sz(w) (int) w.size()
bool debug;
typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
const int inf = 1e9 + 5;
const ll INF = (ll) inf * inf;
const int nax = 500123;

int dx(char z) {
	if(z == '>') return 1;
	if(z == '<') return -1;
	return 0;
}
int dy(char z) {
	if(z == 'v') return 1;
	if(z == '^') return -1;
	return 0;
}
int yy[nax], xx[nax];
char sl[1005][1005];

void te() {
	int H, W;
	scanf("%d%d", &H, &W);
	REP(y, H) scanf("%s", sl[y]);
	REP(y, H) yy[y] = 0;
	REP(x, W) xx[x] = 0;
	REP(y, H) REP(x, W) if(sl[y][x] != '.') {
		yy[y]++;
		xx[x]++;
	}
	int res = 0;
	REP(y, H) REP(x, W) if(sl[y][x] != '.') {
		pii memo = mp(x,y);
		if(yy[y] == 1 && xx[x] == 1) {
			puts("IMPOSSIBLE");
			return;
		}
		int pomx = dx(sl[y][x]);
		int pomy = dy(sl[y][x]);
		bool ok = false;
		x+=pomx; y+=pomy;
		while(0 <= x && x < W && 0 <= y && y < H) {
			if(sl[y][x] != '.') ok = true;
			x += pomx;
			y += pomy;
		}
		if(!ok) ++res;
		x=memo.st;
		y=memo.nd;
	}
	printf("%d\n", res);
}

int main(int argc, char *argv[])
{
	debug = argc > 1;
	
	int z;
	scanf("%d", &z);
	RI(nr, z) {
		printf("Case #%d: ", nr);
		te();
	}
	
	return 0;
}
