#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<cstdio>

using namespace std;
#define REP(i,n) for(int i=0;i<(int)n;++i)
typedef long long int ll;
void solve() {
  int n;
  cin>>n;
  if(n==0)  {
    cout<<"INSOMNIA"<<endl;
    return;
  }
  int c[10];
  int tot=0;
  REP(i,10) c[i]=0;
  REP(i,1000) {
    char p[100];
    sprintf(p,"%d",n*(i+1));
    for(int j=0;p[j];++j) {
      int x=p[j]-'0';
      if (!c[x]) ++tot;
      c[x]=1;

    }
    if(tot==10) {
      cout<<n*(i+1)<<endl;
      return;
    }
  }
}
int main() {
  int t;cin>>t;REP(i,t) {
    cout<<"Case #"<<(i+1)<<": ";
    solve();
  }

}
