#include<iostream>
#include<cstdio>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<cassert>
#define PB push_back
#define sz(v) (in((v).size()))
#define forn(i,n) for(in i=0;i<(n);i++)
#define forv(i,v) forn(i,sz(v))
using namespace std;
typedef long long in;
vector<in> hpt;
vector<in> gd;
vector<in> twhits;
vector<in> hits;
vector<in> best[2];
in inf=100000000000000000LL;
in p,q,n;
int main(){
  in T;
  cin>>T;
  forn(zz,T){
    cout<<"Case #"<<zz+1<<": ";
    cin>>p>>q>>n;
    hpt.resize(n);
    gd.resize(n);
    forn(i,n){
      cin>>hpt[i]>>gd[i];
    }
    twhits.resize(n);
    hits.resize(n);
    forn(i,n){
      twhits[i]=(hpt[i]-1)/q;
      hits[i]=((hpt[i]-1)%q+1)/p+1;
      if(((hpt[i]-1)%q+1)%p==0)
	hits[i]--;
    }
    in sw,nw;
    forn(i,2){
      best[i].clear();
      best[i].resize(15*(n+3),-inf);
    }
    sw=nw=0;
    best[0][1]=0;
    forn(i,n){
      sw=i%2;
      nw=!sw;
      in nuj;
      forn(j,15*(i+3)){
	best[nw][j]=-inf;
      }
      forn(j,15*(i+2)){
	nuj=j+twhits[i]+1;
	if(best[nw][nuj]<best[sw][j])
	  best[nw][nuj]=best[sw][j];
	if(j+twhits[i]>=hits[i]){
	  nuj=j+twhits[i]-hits[i];
	  if(best[nw][nuj]<best[sw][j]+gd[i]){
	    best[nw][nuj]=best[sw][j]+gd[i];
	  }
	}
      }
    }
    in besttot=-inf;
    forv(j,best[nw])
      if(best[nw][j]>besttot)
	besttot=best[nw][j];
    cout<<besttot<<endl;
  }
  return 0;
}

