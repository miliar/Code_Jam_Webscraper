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
  string s;
  cin>>s;
  int rval=0;
  int ppl=0;
  REP(i,n+1) {
    int need=i-rval-ppl;
    if(need>0) rval+=need;
    ppl+=s[i]-'0';
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
