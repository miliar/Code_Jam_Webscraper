// TwT514 {{{
#include <bits/stdc++.h>
#define SZ(x) ((int)(x).size())
#define FOR(i,c) for (auto i=(c).begin(); i!=(c).end(); i++)
#define REP(i,n) for (int i=0; i<(n); i++)
#define REP1(i,a,b) for (int i=(int)(a); i<=(int)(b); i++)
#define ALL(x) (x).begin(),(x).end()
#define MS0(x,n) memset(x,0,(n)*sizeof(*x))
#define MS1(x,n) memset(x,-1,(n)*sizeof(*x))
#define MP make_pair
#define PB push_back
#define RI(a) scanf("%d",&(a))
#define RII(a,b) scanf("%d%d",&(a),&(b))
#define RIII(a,b,c) scanf("%d%d%d",&(a),&(b),&(c))
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
// }}}
#define N 1001001
int n;
LL a[N];
void input(){
	RI(n);
	LL p,q,r,s;
	cin >> p >> q >> r >> s;
	REP(i,n) a[i] = (i * p + q) % r + s;
}
LL sm;
bool good(LL d){
	LL x = 0, y = 0;
	for(int i=0; i<n; i++){
		if(x+a[i]<=d) x+=a[i];
		else break;
	}
	for(int i=n-1; i>=0; i--){
		if(y+a[i]<=d) y+=a[i];
		else break;
	}
	return sm-x-y<=d;
}

void solve(){
	sm = 0;
	REP(i,n) sm+=a[i];
	LL mn = 0, mx = sm, md;
	while(mn<mx){
		md = (mn+mx)/2;
		if(good(md)) mx = md;
		else mn = md+1;
	}
	static int zi = 0;
	printf("Case #%d: %.12f\n", ++zi, 1.0*(sm-mn)/sm);
}

int main() {
	int zn;
	RI(zn);
	while(zn--){
		input();
		solve();
	}
    return 0;
}

