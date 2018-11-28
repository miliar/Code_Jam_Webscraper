#include<iostream>
#include<cstdio>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<cassert>
#define PB push_back
#define MP make_pair
#define sz(v) (in((v).size()))
#define forn(i,n) for(in i=0;i<(n);i++)
#define forv(i,v) forn(i,sz(v))
using namespace std;
typedef long long in;
vector<in> a;
in n;
vector<pair<in,in> > sta;
bool hs(in msk, in a){
  return msk&(1LL<<a);
}
int main(){
  in T;
  cin>>T;
  forn(zz,T){
    cout<<"Case #"<<zz+1<<": ";
    cin>>n;
    a.resize(n);
    sta.clear();
    forn(i,n){
      cin>>a[i];
      sta.PB(MP(a[i],i));
    }
    sort(sta.begin(),sta.end());
    forv(i,sta)
      a[sta[i].second]=i;
    in mx=sta[n-1].second;
    in cst=0;
    in lc;
    for(in i=n-2;i>=0;i--){
      in ss=0;
      lc=sta[i].second;
      for(in j=0;j<lc;j++){
	if(a[j]>i)
	  ss++;
      }
      if(ss>(n-1-i)-ss)
	ss=n-1-i-ss;
      cst+=ss;
    }
    cout<<cst<<endl;
  }
  return 0;
}

