#include<iostream>
#include<vector>
#include<set>
#include<queue>
#include<algorithm>
#include<map>
#include<string>

using namespace std;
#define REP(i,n) for(int i=0;i<(int)n;++i)
void solve() {
  int n;cin>>n;
  vector<int> p(n);REP(i,n) cin>>p[i];
  int rval=1000;
  vector<int> cd(n,0);
  priority_queue<pair<int, int> > Q;
  int div=0;
  REP(i,n)  Q.push(make_pair(p[i],i));
  while(1) {
    pair<int, int> x=Q.top();Q.pop();
    rval=min(rval, div+x.first);
    div++;
    int m=cd[x.second];
    cd[x.second]++;
    m+=2;
    Q.push(make_pair(((p[x.second]+m-1) /m),x.second));
    if(x.first<=1) break;
  }
  cout<<rval<<endl;
}
int main() {
  int T;
  cin>>T;
  REP(i, T) {
    cout<<"Case #"<<(i+1)<<": ";
    solve();
  }
}
