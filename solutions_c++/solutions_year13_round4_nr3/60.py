#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define REP(i,x)for(int i=0;i<(int)x;i++)
int A[2004],B[2004];
int T,N;
vector<int> ans;
vector<int> k;

bool ok(int pos, int val){
    
}
int dp[2004];
bool dfs(int now){
  if(now > N){
    ans = min(ans, k);
    return true;
  }
  vector<int> inc(N);
  vector<int> dec(N);
  fill(dp,dp+N+1,99999);
  for(int i=0;i<N;i++){
    inc[i] = lower_bound(dp,dp+N,99999) - dp;
    if(k[i] == -1)continue;
    *lower_bound(dp, dp + N, k[i]) = k[i];
  }
  fill(dp,dp+N+1,99999);
  for(int i=N-1;i>=0;i--){
    dec[i] = lower_bound(dp,dp+N,99999) - dp;
    if(k[i] == -1)continue;
    *lower_bound(dp, dp + N, k[i]) = k[i];
  }
  REP(i,N){
    if(k[i] == -1 && (dec[i] >= B[i] || inc[i] >= A[i]))return false;
  }
#if 0
  cout << "----" << " " << now << " -----"<<endl;
  REP(i,N){
    cout << k[i] << ' ';
  }
  cout<<endl;
  REP(i,N){
    cout << inc[i] << " ";
  }
  cout << endl;
  REP(i,N){
    cout << dec[i] << " ";
  }
  cout << endl;
#endif
  bool ok = false;
  for(int i=0;i<N;i++){
    if(k[i] == -1 && inc[i] == A[i] - 1 && dec[i] == B[i] - 1){
      k[i] = now;
      ok |= dfs(now + 1);
      if(ok)return ok;
      k[i] = -1;
    }
  }
  if(!ok){
    cout << "Failed" << endl;
  }
  return ok;
}
int main(){
  cin>>T;
  for(int tc=1;tc<=T;tc++){
    cout<<"Case #" << tc << ":";
    cin>>N;
    REP(i,N)cin>>A[i];
    REP(i,N)cin>>B[i];
    ans= vector<int>(1);
    ans[0] = N + 1;
    k=vector<int>(N,-1);
    dfs(1);
    for(int i=0;i<N;i++){
      cout<<" "<<ans[i];
    }
    cout<<endl;
  }
}
