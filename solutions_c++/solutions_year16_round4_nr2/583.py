#include<iostream>
#include<algorithm>
#include<vector>
#include<string>

using namespace std;
#define REP(i,n) for(int i=0;i<(int)n;++i)
typedef long long int ll;
long double halfprob(vector<long double> x) {
  sort(x.begin(), x.end());
  int n=x.size();
  vector<long double> c(n+1);
  c[0]=1.0;
//  REP(i,n) cout<<x[i]<<" ";
  REP(i,n) {
    for(int j=n;j>=0;--j) c[j]= (j? x[i]*c[j-1]:0)+(1.0-x[i])*c[j];
  }
  //cout<<c[n/2]<<endl;
  return c[n/2];
}
void solve() {
  int n,K;
  long double result=0.0;
  cin>>n>>K;
  vector<long double> x(n);
  REP(i,n) cin>>x[i];
  sort(x.begin(), x.end());
  
  REP(pref, K+1) {
    vector<long double> k;
    REP(i,pref) k.push_back(x[i]);
    REP(i,K-pref) k.push_back(x[n-1-i]);
    long double z=halfprob(k);
    if(z>result)result=z;
  }
  cout.precision(13);
  cout<<result<<endl;
}
int main() {
  int t;cin>>t;REP(i,t) {
    cout<<"Case #"<<(i+1)<<": ";
    solve();
  }

}
