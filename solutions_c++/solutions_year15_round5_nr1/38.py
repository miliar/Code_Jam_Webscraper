#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstring>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
#define SIZE(x) (int((x).size()))
#define rep(i,l,r) for (int i=(l); i<=(r); i++)
#define repd(i,r,l) for (int i=(r); i>=(l); i--)
#define repn(i,l,r,s) for (int i=(l); i<=(r); i+=s)
#define repdn(i,r,l,s) for (int i=(r); i>=(l); i-=s)
#define rept(i,c) for (typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)

#ifdef DEBUG
#define debug(x) { cerr<<#x<<" = "<<(x)<<endl; }
#else
#define debug(x) {}
#endif

#define MAXN 1000010

int n, d;
int par[MAXN], sal[MAXN];
int inq[MAXN];
vector<int> chd[MAXN];

typedef pair<int, int> P;
set<P> evt;

int cmax, siz;

void ins(int x) {
	if (x != 0 && !inq[par[x]]) return;
	inq[x] = 1;
	siz++;
	rep(i,0,SIZE(chd[x])-1) {
		int v = chd[x][i];
		if (!inq[v]) {
			if (sal[v] <= cmax && sal[v] >= cmax - d) {
				ins(v);
			} else if (sal[v] > cmax) {
				evt.insert(P(sal[v]*2+1, v));
			}
		}
	}
	evt.insert(P((sal[x]+d+1)*2, x));
}
void del(int x) {
	if (!inq[x]) return;
	inq[x] = 0;
	siz--;
	rep(i,0,SIZE(chd[x])-1) {
		int v = chd[x][i];
		if (inq[v]) {
			del(v);
		}
	}
}

void lemon() {  
	scanf("%d%d", &n, &d);
	LL s0, as, cs, rs;
	LL m0, am, cm, rm;
	scanf("%lld%lld%lld%lld%lld%lld%lld%lld", &s0, &as, &cs, &rs, &m0, &am, &cm, &rm);
	rep(i,0,n-1) {
		if (i) {
			par[i] = m0 % i;
		}
		sal[i] = s0;
		s0 = (s0 * as + cs) % rs;
		m0 = (m0 * am + cm) % rm;
		chd[i].clear();
	}	
	rep(i,1,n-1) {
		chd[par[i]].push_back(i);
	}
	evt.clear();
	evt.insert(P(sal[0]*2+1, 0));
	siz = 0;
	cmax = 0;
	int ans = 0;
	while (evt.size()) {
		P h = *evt.begin();
		evt.erase(h);
		cmax = max(cmax, (h.first)/2);
		if (h.first % 2) {
			ins(h.second);
		} else {
			del(h.second);
		}
		ans = max(ans, siz);
	}
	printf("%d\n", ans);
}

int main() {
    ios::sync_with_stdio(true);
    int n;
    scanf("%d", &n);
    rep(i,1,n) {
  	    printf("Case #%d: ", i);
  	    lemon();
    }
    return 0;
}