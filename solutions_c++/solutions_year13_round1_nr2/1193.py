#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<map>
#include<vector>
#include<deque>
using namespace std;
#define pi 3.141592653589793238
int v[1000];
int T,e,r,n;
long long ans;
void solve(int jobnum,int have,long long gain){
  if(jobnum==n){
    ans=max(ans,gain);
    return;
  }else if(jobnum<n){
    int temp=(r+have-e);
    for(int i=0;i<=have;i++){
      //cout<<jobnum<<"  "<<i<<" "<<gain+(i*v[jobnum])<<endl;
      solve(jobnum+1,min(have-i+r,e),gain+(i*v[jobnum]));
    }
  }
}
int main(){
  cin>>T;
  for(int tc=1;tc<=T;tc++){
    cin>>e>>r>>n;
    printf("Case #%d: ",tc);
    for(int i=0;i<n;i++)cin>>v[i];
    ans=-1;
    solve(0,e,0);
    cout<<ans<<endl;
  }
  return 0;
}
