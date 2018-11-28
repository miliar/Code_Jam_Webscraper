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

const static ll INF = 1e15;
const static D EPS = 1e-8;

ll dp[20][1<<15];

int main(){
  int testcase;

  cin >> testcase;
  for(int casenum=1;casenum<=testcase;casenum++){
    ll n;
    cin >> n;
    char door[1010];
    vl id(n),tmp;

    rep(i,n)cin >> door[i] >> id[i];

    rep(i,n){
      if(id[i])tmp.push_back(id[i]);
    }
    sort(all(tmp));
    tmp.erase(unique(all(tmp)),tmp.end());


    rep(i,n){
      rep(j,tmp.sz){
	if(id[i]!=0 && id[i] == tmp[j])id[i] = j+1;
      }
    }

    int m = n;

    rep(i,n+1){
      rep(j,1<<m)dp[i][j] = INF;
    }
    
    rep(i,1<<m)dp[0][i] = __builtin_popcount(i);

    rep(i,n){
      rep(j,1<<m){
	if(dp[i][j] == INF)continue;
	if(door[i] == 'L'){
	  if(id[i] == 0){
	    rep(k,m){
	      if((j>>k) & 1){
		int nxt = j & (~(1<<k));
		dp[i+1][nxt] = min(dp[i+1][nxt], dp[i][j] - 1);
	      }
	    }
	  }else{
	    if((j>>(id[i]-1)) & 1){
	      int nxt = j & (~(1<<(id[i]-1)));
	      dp[i+1][nxt] = min(dp[i+1][nxt], dp[i][j] - 1);
	    }
	  }
	}else{
	  if(id[i] == 0){
	    rep(k,m){
	      if(((j>>k) & 1) == 0){
		int nxt = j | (1<<k);
		dp[i+1][nxt] = min(dp[i+1][nxt], dp[i][j] + 1);
	      }
	    }
	  }else{
	    if(( (j>>(id[i]-1)) & 1) == 0){
	      int nxt = j | (1<<(id[i]-1));
	      dp[i+1][nxt] = min(dp[i+1][nxt], dp[i][j] + 1);
	    }
	  }
	}
      }
    }
    /*
    rep(i,n+1){
      rep(j,n+1){
	rep(k,1<<m)cout << dp[i][j][k] << " ";
	cout << endl;
      }
      cout << endl;
    }
    */

    ll ans = INF;
    rep(i,1<<m){
      ans = min(ans, dp[n][i]);
    }
    
    cout << "Case #" << casenum << ": ";
    if(ans==INF)cout << "CRIME TIME" << endl;
    else cout << ans << endl;
  }
}
