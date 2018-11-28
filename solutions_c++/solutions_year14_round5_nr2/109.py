#include<bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define rrep(i,n) for(int i=(int)(n)-1;i>=0;i--)
#define all(a) (a).begin(),(a).end()
#define INIT(a) memset((a),0,sizeof(a))
#define fs first
#define sc second
#define pb push_back
#define sz size() 
using namespace std;
typedef long long ll;
typedef double D;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<ll> vl;

const static int INF = 1e8;
const static D EPS = 1e-8;

ll dp[110][20][1010];

int main(){
  int testcase;

  cin >> testcase;
  for(int casenum=1;casenum<=testcase;casenum++){
    ll p,q,n;
    cin >> p >> q >> n;
    vl h(n),g(n);
    rep(i,n)cin >> h[i] >> g[i];

    memset(dp,-1,sizeof(dp));
    dp[0][0][1] = 0;

    rep(i,n){
      rep(j,10+1){
	if(j*q >= h[i]+q)break;
	ll rem = h[i] - j*q;
	if(rem <= 0){
	  rep(k,10*n+1){
	    dp[i+1][0][k] = max(dp[i+1][0][k], dp[i][j][k]);
	  }
	}else{

	  ll shot = (rem+p-1)/p;
	  rep(k,10*n+1){
	    if(dp[i][j][k] < 0)continue;
	    dp[i][j+1][k+1] = max(dp[i][j+1][k+1], dp[i][j][k]);
	    if(shot<=k){
	      dp[i+1][0][k-shot] = max(dp[i+1][0][k-shot], dp[i][j][k]+g[i]);
	    }
	  }
	}
      }
    }

    ll ans = 0;
    rep(i,10*n+1){
      ans = max(ans, dp[n][0][i]);
    }
    cout << "Case #" << casenum << ": " << ans << endl;;
  }
}
