#include<cstdio>
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<cstring>
#include<cstdlib>
#include<cassert>

using namespace std;

typedef long long ll;
typedef pair<int,int> pint;

#define mp make_pair
#define pb push_back

#define repp(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define rep(i,n) repp(i,0,(n)-1)

int n;
ll b;
ll x[40];
ll xx[40];

double solve(){
	cin >> b >> n;
	rep(i,n) cin >> x[i];
	repp(i,n,37) x[i] = 0;
	sort(x, x+37);
//	reverse(x,x+37);
	xx[0] = 0;
	repp(i,1,37) xx[i] = xx[i-1] + x[i-1];
//	repp(i,n+1,38) xx[i] = xx[i-1];
//rep(i,37) cout << x[i] << ' '; cout << endl;
//rep(i,38) cout << xx[i] << ' '; cout << endl;

	double res = 0.0;
	repp(i,1,36){
		if(x[i] == x[i-1]) continue;
		ll a = xx[i];
		if(a + b < i * x[i-1] ) continue;
		ll c = a + b - i * x[i-1];
		rep(j,i){
			if(c < j) continue;
//			ll d = (c - j) / i;
			ll d = min( (c - j) / i, x[i]-x[i-1]-1 );
//			if(j==0)d = max( (c - j) / i, x[i]-x[i-1] );
			ll e = (ll)(i-j) * (x[i-1] + d) - xx[i-j];
			if(res < e*36.0/(i-j) - i*(x[i-1]+d) - j + a){
//cout << "i=" << i << ", j=" << j << ", a=" << a << ", b=" << b << ", c=" << c << ", d=" << d << ", e=" << e << endl;
				res = e*36.0/(i-j) - i*(x[i-1]+d) - j + a;
			
			}
		}

	}
	return res;
}

int main(){
	int casenum; cin >> casenum;
	rep(cas, casenum){
		printf("Case #%d: %.9f\n", cas+1, solve());
	}
	return 0;
}

