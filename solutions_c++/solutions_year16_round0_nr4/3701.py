#include<iostream>
#include<algorithm>
#include<vector>
#include<string>

using namespace std;
#define REP(i,n) for(int i=0;i<(int)n;++i)
typedef long long int ll;
void solve() {
  int k,c,s;
  cin>>k>>c>>s;
  if(s<k) { cout<<"IMPOSSIBLE"<<endl; return;}
  REP(i,k) { if(i)cout<<" "; cout<<i+1;}
  cout<<endl;
}
int main() {
  int t;cin>>t;REP(i,t) {
    cout<<"Case #"<<(i+1)<<": ";
    solve();
  }

}
