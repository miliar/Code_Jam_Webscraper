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
int a[4][4],b[4][4];
int an,bn;
void input(){
	RI(an);
	REP(i,4) REP(j,4) RI(a[i][j]);
	RI(bn);
	REP(i,4) REP(j,4) RI(b[i][j]);
}

void solve(){
	static int zi=0;
	VI ans;
	REP1(t,1,16){
		int res = 0;
		REP(i,4) if(a[an-1][i]==t) res++;
		REP(i,4) if(b[bn-1][i]==t) res++;
		if(res==2) ans.PB(t);
	}
	printf("Case #%d: ",++zi);
	if(SZ(ans)==0) puts("Volunteer cheated!");
	else if(SZ(ans)>1) puts("Bad magician!");
	else printf("%d\n",ans[0]);
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

