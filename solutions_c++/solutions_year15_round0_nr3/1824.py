#include<iostream>
#include<vector>
#include<set>
#include<queue>
#include<algorithm>
#include<map>
#include<string>

using namespace std;
#define REP(i,n) for(int i=0;i<(int)n;++i)
int to_quat(char c) {
  if(c=='i') return 2;
  if(c=='j') return 3;
  if(c=='k') return 4;
}
int quat_exp(int q, int exp) {
  if(exp==0 || q==1) return 1;
  if(q==-1) {
    if(exp%2) return -1;else return 1;
  }
  int z=exp%4;
  if(z==4) return 1;
  if(z==2) return -1;
  if(z==1) return q;
  return -q;
}
int qm(int q1, int q2) {
  if(q1==1) return q2;
  if(q1==q2) return -1;
  if(q2==1) return q1;
  if(q1<q2) return -qm(q2,q1);
  if(q1==3 && q2==2) return -4;
  if(q1==4 && q2==2) return 3;
  if(q1==4 && q2==3) return -2;
}
int mul(int q1, int q2) {
  int m1=1;
  int m2=1;
  if(q1<0) {
    q1=-q1;
    m1=-1;
  }
  if(q2<0) {
    q2=-q2;
    m2=-1;
  }
  return m1*m2*qm(q1,q2);
}

int sol() {
  int L,X;
  cin>>L>>X;
  string s;
  cin>>s;
  int term=1;
  REP(i,L) term=mul(term, to_quat(s[i]));
  int full=quat_exp(term, X);
  if(full!=-1) {
    return 0;
  }
  int mult=1;
  int state=0;
  REP(k,min(X,12)) {
    REP(i,L) {
      mult=mul(mult,to_quat(s[i]));
      if(state==0) {
        if(mult==2)state=1;

      } else {
        if(mult==4) state=2;
      }
    }
  }
  return state==2;
}
void solve() {
  if(sol()) {
    cout<<"YES"<<endl;
  } else {
    cout<<"NO"<<endl;
  }
}
int main() {
  int T;
  cin>>T;
  REP(i, T) {
    cout<<"Case #"<<(i+1)<<": ";
    solve();
  }
}
