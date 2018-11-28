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
#define ull unsigned long long 
int T,arr[10000001],a,n,ans;
void solve(ull cur,int pos,int moves){
  if(pos==n){
    ans=min(moves,ans);
  }else{
    if(cur>arr[pos]){
      solve(cur+arr[pos],pos+1,moves);
    }else{
      int mtemp=moves;
      ull ctemp=cur;
      while(ctemp<=arr[pos]){
        ctemp+=ctemp-1;
        mtemp++;
      }
      solve(ctemp+arr[pos],pos+1,mtemp);
      solve(cur,pos+1,moves+1);
    }
  }
}
int main(){
  cin>>T;
  for(int tc=1;tc<=T;tc++){
    cin>>a>>n;
    for(int i=0;i<n;i++)cin>>arr[i];
    sort(arr,arr+n);
    printf("Case #%d: ",tc);
    ans=10000;
    if(a==1)ans=n;
    else solve(a,0,0);
    cout<<ans<<"\n";
  }
  return 0;
}
