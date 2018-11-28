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
in trsz(vector<string> st){
  set<string> cs;
  forv(i,st){
    forn(j,st[i].length()+1){
      cs.insert(st[i].substr(0,j));
    }
  }
  return sz(cs);
}
vector<string> s;
in hg;
in ct;
vector<in> blg;
in lun;
in mdl=1000000007LL;
in m,n;
void dtb(in l){
  if(l==m){
    in cc=0;
    forn(i,n){
      vector<string> cr;
      forn(j,m)
	if(blg[j]==i)
	  cr.PB(s[j]);
      if(sz(cr)==0){
	cc=-2;
	break;
      }
      cc+=trsz(cr);
    }
    if(cc>hg){
      hg=cc;
      ct=0;
    }
    if(cc==hg)
      ct++;
    return;
  }
  in lunag=lun;
  for(in i=0;i<=lun && i<n;i++){
    blg[l]=i;
    if(i==lun)
      lun++;
    dtb(l+1);
    lun=lunag;
  }
}
int main(){
  in T;
  cin>>T;
  forn(zz,T){
    cout<<"Case #"<<zz+1<<": ";
    cin>>m>>n;
    s.resize(m);
    blg.resize(m);
    forn(i,m)
      cin>>s[i];
    hg=-1;
    ct=0;
    lun=0;
    dtb(0);
    for(in i=1;i<=n;i++)
      ct*=i;
    cout<<hg<<" "<<ct%mdl<<endl;
  }
  return 0;
}

