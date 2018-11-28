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

const int mlp[4][4]={{1,2,3,4},{2,-1,4,-3},{3,-4,-1,2},{4,3,-2,-1}};

int convert(char c) {
	if (c=='i') return 2;
	if (c=='j') return 3;
	if (c=='k') return 4;
}

int do_mul(int a, int b) {
	bool neg((a<0)^(b<0));
	a=abs(a),b=abs(b);
	int m(mlp[a-1][b-1]);
	if (neg) m=-m;
	return m;
}

void solve_test() {
	int n,x;
	scanf("%d%d\n",&n,&x);
	string s;
	getline(cin,s);
	string rs;
	rept(i,x) rs+=s;
	VI d(sz(rs));
	rept(i,sz(rs)) d[i]=convert(rs[i]);
	int s_mlp(1);
	rept(i,sz(d)) s_mlp=do_mul(s_mlp,d[i]);
	if (s_mlp!=-1) {
		printf("NO\n");
		return;
	}
	int up_to(0);
	int now(1);
	bool ok(true);
	while (up_to<sz(d) && now!=2) {
		now=do_mul(now,d[up_to]);
		++up_to;
	}
	if (now!=2) ok=false;
	int down_to(sz(d)-1);
	now=1;
	while (down_to>=0 && now!=4) {
		now=do_mul(d[down_to],now);
		--down_to;
	}
	if (now!=4) ok=false;
	if (ok && up_to<=down_to) {
		printf("YES\n");
	} else {
		printf("NO\n");
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