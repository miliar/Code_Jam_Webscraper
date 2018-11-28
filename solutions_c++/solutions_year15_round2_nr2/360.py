#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>
#include<assert.h>
using namespace std;
#define FOR(i,a,b) for(int i = a; i <= b; ++i)
#define FORD(i,a,b) for(int i = a; i >= b; --i)
#define RI(i,n) FOR(i,1,n)
#define REP(i,n) FOR(i,0,(n)-1)
#define pb push_back
#define mp make_pair
#define st first
#define nd second
#define mini(a,b) a=min(a,b)
#define maxi(a,b) a=max(a,b)
#define sz(w) (int)w.size()
bool debug;
typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
const int inf = 1e9 + 5;
const int nax = 100005;

bool kr(int a, int A) { return a == 1 || a == A; }
bool vis[nax];
void te() {
	
	int h, w, n;
	scanf("%d%d%d", &h, &w, &n);
	
	if(n <= (h * w + 1) / 2) {
		puts("0");
		return;
	}
	
	if(h > w) swap(h, w);
	if(h == 1) {
		RI(i, w) vis[i] = false;
		for(int i = 1; i <= w; i += 2) {
			vis[i] = true;
			--n;
		}
		int start = w;
		if(vis[start]) --start;
		for(int i = start; i >= 1 && n; i -= 2) {
			vis[i] = true;
			--n;
		}
		int res = 0;
		RI(i, w - 1) if(vis[i] && vis[i+1]) ++res;
		printf("%d\n", res);
		return;
	}
	
	int res = inf;
	
	REP(parz, 2) {
		vi vec;
		RI(x, w) RI(y, h) if((x + y) % 2 == parz) {
			if(kr(x, w) && kr(y, h)) vec.pb(2);
			else if(kr(x,w) || kr(y,h)) vec.pb(3);
			else vec.pb(4);
		}
		sort(vec.begin(), vec.end());
		int zostalo = n;
		RI(x, w) RI(y, h) if((x + y) % 2 != parz) --zostalo;
		assert(zostalo <= sz(vec));
		int moze = 0;
		REP(i, zostalo) moze += vec[i];
		mini(res, moze);
	}
	
	printf("%d\n", res);
}

int main(int argc, char * argv[]) { 
	debug = argc > 1;
	
	int zz;
	scanf("%d", &zz) ?: 0;
	RI(nr, zz) {
		printf("Case #%d: ", nr);
		te();
	}
	
	return 0;
}
