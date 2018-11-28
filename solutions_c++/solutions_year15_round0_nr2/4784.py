#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define pdd pair<double,double>
#define uint unsigned int
#define LL long long
#define ULL unsigned LL
#define VI vector<int>
#define X first
#define Y second
#define sz(_v) ((int)_v.size())
#define all(_v) (_v).begin(),(_v).end()
#define FOR(_i,a,b) for (int _i(a),_l(b); _i<=_l; ++_i)
#define rept(i,a) FOR(i,0,(int)(a)-1)
#define x1 X1
#define y1 Y1
#define sqr(a) ((a)*(a))
#define C(a) memset((a),0,sizeof (a))
#define MS(a,x) memset((a),(x),sizeof (a))
#define INF 1050000000
#define INFL INF*1ll*INF
#define PI 3.141592653589
#define eps 1e-10
#define MOD 1000000007
#define PRIME 312427
#define MOD2 500000004

using namespace std;

bool can(VI d, int k, int repl) {
	int sum(accumulate(all(d),0));
	int eat(k-repl);
	int more_than(0);
	rept(i,repl) {
		int mx(max_element(all(d))-d.begin());
		if (d[mx]<=eat) continue;
		int can(min(d[mx]-eat,eat));
		d[mx]-=can;
	}
	rept(i,sz(d)) {
		if (d[i]>eat) return false;
	}
	return true;
}

void solve_test() {
	int n;
	scanf("%d",&n);
	VI d(n);
	rept(i,n) scanf("%d",&d[i]);
	FOR(i,1,200) {
		FOR(j,0,i) {
			if (can(d,i,j)) {
				printf("%d\n",i);
				return;
			}
		}
	}
}

void solve() {
	int tst;
	scanf("%d",&tst);
	FOR(i,1,tst) {
		printf("Case #%d: ",i);
		solve_test();
	}
}

int main() {
#ifdef yeti
    freopen("input.txt","r",stdin); // freopen("output.txt","w",stdout);
#endif

#ifdef yeti
    clock_t tm = clock();
    cerr<<setprecision(10);
#endif
    solve();
#ifdef yeti
    cerr<<setprecision(3)<<(clock()-tm+0.)/CLOCKS_PER_SEC<<endl;
#endif
    return 0;
}