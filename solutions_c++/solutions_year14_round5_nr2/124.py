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
#define N 110
#define M 3000
#define INF 1e9
int n;
int p[N], t[N], g[N];
void input(){
	int a,b;
	RIII(a,b,n);
	int h;
	REP(i,n){
		RII(h, g[i]);
		t[i] = (h-1)/b;
		h-=t[i]*b;
		p[i] = (h+a-1)/a;
	}
}

int dp[N][M];
inline void update(int& a, int b){a = max(a,b);}
inline bool in(int a){return 0<=a && a<M;}
void solve(){
	//REP(i,n) printf("- %d %d %d\n", p[i], t[i], g[i]);
	REP(i,n+1) REP(j,M) dp[i][j] = -INF;
	//REP(j,10) printf("%d ", dp[0][j]<0?-1:dp[0][j]); puts("");
	dp[0][1] = 0;
	REP(i,n){
		REP(j,M){
			if(in(j+t[i]-p[i])) update(dp[i+1][j+t[i]-p[i]], dp[i][j]+g[i]);
			if(in(j+t[i]+1))    update(dp[i+1][j+t[i]+1], dp[i][j]);
		}
		//REP(j,10) printf("%d ", dp[i+1][j]<0?-1:dp[i+1][j]); puts("");
	}
	int ans = -INF;
	REP(i,M) update(ans, dp[n][i]);
	static int zi=0;
	printf("Case #%d: %d\n", ++zi, ans);

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

