#include<cstdio>
#include<iostream>
#include<algorithm>
#include<set>
#include<map>
#include<vector>
#include<string>
using namespace std;
#define REP(i,n) for(int i=0;i<(int)n;++i)
int is_palindrome(int x) {
  char p[111];
  sprintf(p,"%d",x);
  string a=p;
  string b=p;
  reverse(b.begin(), b.end());
  return a==b;
}
int b[1111];
int m=1001;
int main() {
int T;cin>>T;
REP(i,m) b[i]=0;
REP(i,36) {
  if(is_palindrome(i) && i*i<m && is_palindrome(i*i)) {
    b[i*i]=1;
  }
}
REP(tt,T) {
  int A,B;
  cin>>A>>B;
  int ans=0;
  for(int i=A;i<=B;++i) ans+=b[i];
  cout<<"Case #"<<(tt+1)<<": "<<ans<<endl;
}
}
// issue choosing small type
