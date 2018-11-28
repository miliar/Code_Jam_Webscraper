#include <bits/stdc++.h>

using namespace std;

const int N = 205;
double dp[N][N];
double a[N];
double p[N];

double solve(int n) {
  for(int i = 1;i <= n;i++) {
    for(int j = 0;j <= n;j++) {
      dp[i][j] = 0;
    }
  }
  dp[0][0] = 1;
  for(int i = 1;i <= n;i++) {
    for(int j = 0;j <= n;j++) {
      dp[i][j] = dp[i - 1][j] * (1 - a[i]) + dp[i - 1][j - 1] * a[i];
    }
  }
  return dp[n][n/2];
}
void solve() {
  int n,k; cin>>n>>k;
  for(int i = 1;i <= n;i++) 
    cin>>p[i];
  sort(p+1,p+1+n);
  double ans = 0;
  for(int i = 0;i <= k;i++) {
    int cc = 1;
    for(int j = 1;j <= i;j++) {
      a[cc++] = p[j];
    }
    for(int j = n - k + i + 1;j <= n;j++) {
      a[cc++] = p[j];
    }
    ans = max(ans,solve(k));
  }
  printf("%12.12lf\n",ans);
}

int main() {
  assert(freopen("input.txt","r",stdin));
  assert(freopen("output3.txt","w",stdout));
  int t; cin>>t;
  for(int i = 1;i <= t;i++) {
    cerr<<"Executing Case #"<<i<<endl;
    cout<<"Case #"<<i<<": ";
    solve();
  }

}
