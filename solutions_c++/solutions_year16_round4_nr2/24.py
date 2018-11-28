#include<iostream>
#include<iomanip>
#include<cstdio>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<cassert>
#define PB push_back
#define MP make_pair
#define sz(v) (in((v).size()))
#define forn(i,n) for(in i=0;i<(n);++i)
#define forv(i,v) forn(i,sz(v))
#define fors(i,s) for(auto i=(s).begin();i!=(s).end();++i)
#define all(v) (v).begin(),(v).end()
using namespace std;
typedef long long in;
typedef vector<in> VI;
typedef vector<VI> VVI;
vector<double> tmn;
vector<vector<double> > pof;
double mk(){
  in n=sz(tmn);
  forv(i,pof){
    forv(j,pof[i])
      pof[i][j]=0;
  }
  pof[0][0]=1;
  double cpr;
  forn(i,n){
    cpr=tmn[i];
    forn(j,n){
      pof[i+1][j+1]+=pof[i][j]*cpr;
      pof[i+1][j]+=pof[i][j]*(1-cpr);
    }
  }
  return pof[n][n/2];
}
in p2(in a){
  return 1LL<<a;
}
vector<double> mpr;
void docase(){
  in n,k;
  cin>>n>>k;
  pof=vector<vector<double> >(k+1,vector<double>(k+1));
  mpr.resize(n);
  forn(i,n)
    cin>>mpr[i];
  sort(all(mpr));
  double bst=0;
  forn(pfx,k+1){
    in sfx=k-pfx;
    tmn.clear();
    forn(i,pfx)
      tmn.PB(mpr[i]);
    forn(i,sfx)
      tmn.PB(mpr[n-1-i]);
    bst=max(bst,mk());
  }
  cout<<setprecision(15)<<bst<<endl;
}
int main(){
  ios::sync_with_stdio(0);
  cin.tie(0);
  in T;
  cin>>T;
  for(in zz=1;zz<=T;zz++){
    cout<<"Case #"<<zz<<": ";
    docase();
  }
  return 0;
}
