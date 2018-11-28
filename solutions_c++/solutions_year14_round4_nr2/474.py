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
  int n;
  cin>>n;
  vector<int> a(n);
  REP(i,n) cin>>a[i];
  int rval=0;
  REP(i,n) {
    int x=0;
    REP(j,a.size()) if(a[j]<a[x])x=j;
    int c1=x;
    int c2=(int)a.size()-1-x;
    rval+=min(c1,c2);
    for(int k=x;k<(int)a.size();++k) {
      a[k]=a[k+1];
    }
    a.resize(a.size()-1);
  }
  cout<<rval;
}
int main() {
int T;cin>>T;
REP(i,T) {
  cout<<"Case #"<<(i+1)<<": ";
  solve();
  cout<<endl;
}
}
