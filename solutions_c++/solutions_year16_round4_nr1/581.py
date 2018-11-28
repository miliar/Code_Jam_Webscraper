#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
using namespace std;
#define REP(i,n) for(int i=0;i<(int)n;++i)
typedef long long int ll;
map<pair<char, int>, string > B;
string expand(char c, int level) {
  if(level==0) return string(1,c);
  if(B.find(make_pair(c,level))!=B.end()) return B[make_pair(c,level)];
  string a,b;
  if( c=='P') {
    a=expand('R',level-1);
    b=expand('P',level-1);
  } 
  if( c=='R') {
    a=expand('R',level-1);
    b=expand('S',level-1);
  } 
  if( c=='S') {
    a=expand('S',level-1);
    b=expand('P',level-1);
  } 
  string X=min(a+b,b+a);
  B[make_pair(c,level)]=X;
  return X;

}
void solve() {
  int n;
  cin>>n;
  int P,R,S;
  cin>>R>>P>>S;
  int X[3]={P,R,S};
  int p=1,r=0,s=0;
  REP(i,n) {
    int p2,r2,s2;
    s2=s+r;
    r2=r+p;
    p2=p+s;
    p=p2;
    r=r2;
    s=s2;
  }
  string D="PRS";
  REP(o,3) {
    int a[3]={0,0,0};
    a[o]=1;

    REP(i,n) {
      int b[3];
      
      REP(j,3) b[j]=a[j];
      b[2]+=a[1];
      b[1]+=a[0];
      b[0]+=a[2];
      REP(j,3) a[j]=b[j];
    }
    int ok=1;
    REP(i,3) if(a[i]!=X[i]) ok=0;
    if(ok) {
      cout<<expand(D[o],n)<<endl;
      return;
    }
  }
  cout<<"IMPOSSIBLE"<<endl;

}
int main() {
  int t;cin>>t;REP(i,t) {
    cout<<"Case #"<<(i+1)<<": ";
    solve();
  }

}
