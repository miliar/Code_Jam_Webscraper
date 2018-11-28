#include<bits/stdtr1c++.h>
using namespace std;
typedef long long LL;
typedef long long ULL;
string s[20][2];
int n;
int dp[1<<17];
int vis[1<<17], ID;

int check(int ind,int m) {
  int s1=0,s2=0;
  for(int i=0;i<n;i++) {
    if((m&(1<<i)) ==0) continue;
    if(s[ind][0] == s[i][0]) s1=1;
    if(s[ind][1] == s[i][1]) s2=1;
  }
  return (s1==1 && s2==1);
}
int solve(int m) {
  if(m == ((1<<n)-1)){
    return 0;
  }
  int &ret = dp[m];
  int &tv = vis[m];
  if(tv == ID)
    return ret;
  tv = ID;
  ret =0;
  for(int i=0;i<n;i++) {
    if((m & (1<<i))) continue;
    ret = max(ret,check(i,m) + solve(m|(1<<i)));
  }
  return ret;
}

int main() {
#ifndef ONLINE_JUDGE
  freopen("2.in", "r", stdin);
  freopen("2.out", "w", stdout);
#endif // ONLINE_JUDGE  ios::sync_with_stdio(false);  cin.tie(NULL);
  cout.tie(NULL);

  int T;
  cin >> T;
  for (int ic = 1; ic <= T; ic++) {
    cin>>n;
    for(int i=0;i<n;i++){
      cin >> s[i][0]>>s[i][1];
    }
    ID++;
    cout << "Case #" << ic << ": ";
    cout<<solve(0)<<endl;
  }
  return 0;

}
