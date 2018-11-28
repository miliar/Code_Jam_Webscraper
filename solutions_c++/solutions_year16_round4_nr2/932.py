#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef complex<double> P;
typedef pair<int,int> pii;
#define REP(i,n) for(ll i=0;i<n;++i)
#define REPR(i,n) for(ll i=1;i<n;++i)
#define FOR(i,a,b) for(ll i=a;i<b;++i)

#define DEBUG(x) cout<<#x<<": "<<x<<endl
#define DEBUG_VEC(v) cout<<#v<<":";REP(i,v.size())cout<<" "<<v[i];cout<<endl
#define ALL(a) (a).begin(),(a).end()

#define MOD (ll)(1e9+7)
#define ADD(a,b) a=((a)+(b))%MOD
#define FIX(a) ((a)%MOD+MOD)%MOD

typedef double Real;

Real calc(int n, Real *arr){
  Real dp[2][252];
  REP(i,n+1)dp[0][i] = 0.0;
  dp[0][0] = 1.0;
  REP(i,n){
    REP(j,n+1)dp[1][j] = 0.0;
    REP(_j,n){
      int j = n-1-_j;
      dp[1][j+1] += dp[0][j]*arr[i];
      dp[1][j] += dp[0][j]*(1.0-arr[i]);
    }
    swap(dp[0],dp[1]);
  }
  return dp[0][n/2];
}

void del(Real dp[252], Real val){
  if(val==0.0)return;
  else if(val==1.0){
    REP(i,252-1)dp[i] = dp[i+1];
    dp[252-1] = 0.0;
    return;
  }
  REP(i,252-1){
    dp[i] = dp[i]/(1-val);
    dp[i+1] -= dp[i]*val;
  }
  dp[252-1] = 0.0;
}
void add(Real dp[252],Real val){
  REP(_i,252-1){
    int i = 252-2-_i;
    dp[i+1] += dp[i]*val;
    dp[i] *= (1.0-val);
  }
}

void solve(){
  int n,k;
  scanf("%d%d",&n,&k);
  Real a[n];
  REP(i,n){
    scanf("%lf",a+i);
  }
  sort(a,a+n);
  Real dp[252];
  REP(i,252)dp[i] = 0.0;
  dp[0] = 1.0;
  REP(i,k){
    add(dp,a[n-1-i]);
  }
  Real ans = dp[k/2];
  REP(i,k){
    del(dp,a[n-1-(k-1-i)]);
    add(dp,a[i]);
    ans = max(ans,dp[k/2]);
  }
  // Real b[k];
  // REP(i,k/2){
  //   if(a[i]<=0.5 && a[n-1-i]>=0.5){
  //     b[2*i] = a[i];
  //     b[2*i+1] = a[n-1-i];
  //   }else if(a[i]>0.5){
  //     REP(j,2*(k-i)){
  //       b[2*i+j] = a[i+j];
  //     }
  //     break;
  //   }else if(a[n-1-i]<0.5){
  //     REP(j,2*(k-i)){
  //       b[2*i+j] = a[n-1-i-j];
  //     }
  //     break;
  //   }
  // }
  // Real ans = calc(k,b);
  printf("%.10lf\n",ans);
  return;
}

int main(){
  int t;
  scanf("%d",&t);
  REP(i,t){
    printf("Case #%d: ",i+1);
    solve();
  }
  return 0;
}
