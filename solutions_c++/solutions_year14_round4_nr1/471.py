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
  int X;cin>>X;
  multiset<int> s;
  REP(i,n) {
    int a;
    cin>>a;
    s.insert(-a);
  }
  int rval=0;
  while(s.size()) {
    rval++;
    multiset<int>::iterator it2=s.begin();
    int c=*it2;
    s.erase(it2);
    int rem=X+c;
//    cout<<rem<<endl;
    if(s.size()) {
      multiset<int>::iterator it=s.lower_bound(-rem);
      if(it!=s.end() && *it>=-rem) {
      //  cout<<"A"<<endl;
        s.erase(it);
      }
    }
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
