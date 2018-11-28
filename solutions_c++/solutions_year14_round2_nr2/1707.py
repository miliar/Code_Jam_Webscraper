#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

ll a,b,k;
void input(){
  cin>>a>>b>>k;
}
typedef pair<ll,ll> pll;
/*
void solve(){
  set<pll> ans;
  for(int i=0;i<a;i++){
    for(int j=0;j<b;j++){
      if((i&j)<k){
        ans.insert(pll(i,j));
      }
    }
  }
  cout<<ans.size()<<endl;
}
*/

void solve(){
  a = min(a,k);
  b = min(b,k);
  cout<<(a*b)<<endl;
}


int main(){
  int t;
  cin>>t;
  for(int i=0;i<t;i++){
    input();
    cout<<"Case #"<<i+1<<": ";
    solve();
  }
}
