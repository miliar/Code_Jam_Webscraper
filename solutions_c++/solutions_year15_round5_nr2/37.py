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

int n,k;
int inp[1010];
int v[1010];

typedef pair<int, int> P;
P itv[1010];

P ext(P x, int y) {
	return P(min(x.first, y), max(x.second, y));
}
int inrang(int x, int mi, int mx) {
	return x>=mi && x<=mx;
}
void lemon() {
	scanf("%d%d", &n,&k);  
	rep(i,0,k-1) itv[i] = P(0,0);
	rep(i,0,n-k) scanf("%d", &inp[i]);
	memset(v, 0, sizeof(v));
	rep(i,0,n-k-1) {
		int dif = inp[i+1] - inp[i];
		v[i+k] = v[i] + dif;
		itv[i%k] = ext(itv[i%k], v[i+k]);
	}
	int mxi = 0;
	rep(i,0,k-1) {
		mxi = max(mxi, itv[i].second - itv[i].first);
	}
	int ans = mxi;
	int res = (inp[0] + k*10000) % k;
	int ini = 0;
	int amr = 0;
	rep(i,0,k-1) {
		ini += -itv[i].first;
		amr += mxi - (itv[i].second - itv[i].first);
	}
	ini %= k;
	debug(res);
	debug(mxi);
	debug(ini);
	debug(amr);
	if (inrang(res, ini, ini + amr) || inrang(res+k, ini, ini+amr)) {
		ans = mxi;
	} else {
		ans = mxi+1;
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