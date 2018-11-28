#include<bits/stdc++.h>
using namespace std;
#define FOR(i,a,b) for(int i = (a); i <= (b); ++i)
#define FORD(i,a,b) for(int i = (a); i >= (b); --i)
#define RI(i,n) FOR(i,1,(n))
#define REP(i,n) FOR(i,0,(n)-1)
#define mini(a,b) a=min(a,b)
#define maxi(a,b) a=max(a,b)
#define mp make_pair
#define pb push_back
#define st first
#define nd second
#define sz(w) (int) w.size()
typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
const int inf = 1e9 + 5;
const int nax = 1e6 + 5;

int in[nax];
int h, w;

bool edge(int mask, int x, int y) {
	return mask & (1 << (x + y * w));
}

bool inside(int x, int y) {
	return 0 <= x && x < w && 0 <= y && y < h;
}

pii dfs_rec(int x, int y, int dx, int dy, int mask) {
	if(!inside(x, y)) {
		return mp(x, y);
	}
	swap(dx, dy);
	if(edge(mask, x, y)) {
		dx *= -1;
		dy *= -1;
	}
	return dfs_rec(x + dx, y + dy, dx, dy, mask);
}

pii dfs(int x, int y, int dx, int dy, int mask) {
	pii tmp = dfs_rec(x,y,dx,dy,mask);
	//printf("(%d,%d) -> (%d,%d)\n", x,y,tmp.first, tmp.second);
	return tmp;
}

int haszuj_rec(pii p) {
	int x = p.first;
	int y = p.second;
	if(y == -1) return x;
	if(x == w) return w + y;
	if(y == h) return w + h + (w - 1 - x);
	assert(x == -1);
	return w + h + w + (h - 1 - y);
}

int haszuj(pii p) {
	int tmp = haszuj_rec(p);
	//printf("hasz(%d,%d) = %d\n", p.first, p.second, tmp);
	return tmp;
}

void te() {
	scanf("%d%d", &h, &w);
	REP(i, 2 * (w + h)) {
		int x;
		scanf("%d", &x);
		in[x-1] = i;
		//scanf("%d", &in[i]);
		//--in[i];
	}
	REP(mask, (1 << (h * w))) {
		//puts("------------");
		bool ok = true;
		REP(x, w) {
			if(in[haszuj(mp(x,-1))]/2 != in[haszuj(dfs(x,0,0,1,mask))]/2)
				ok = false;
			if(in[haszuj(mp(x,h))]/2 != in[haszuj(dfs(x,h-1,0,-1,mask))]/2)
				ok = false;
		}
		REP(y, h) {
			if(in[haszuj(mp(-1,y))]/2 != in[haszuj(dfs(0,y,1,0,mask))]/2)
				ok = false;
			if(in[haszuj(mp(w,y))]/2 != in[haszuj(dfs(w-1,y,-1,0,mask))]/2)
				ok = false;
		}
		if(ok) {
			REP(y, h) {
				REP(x, w)
					printf(edge(mask, x, y) ? "/" : "\\");
				puts("");
			}
			return;
		}
	}
	puts("IMPOSSIBLE");
}

int main() {
	int T;
	scanf("%d", &T);
	RI(nr, T) {
		printf("Case #%d:\n", nr);
		te();
	}
	return 0;
}
