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
#define forn(i,n) for(in i=0;i<(n);++i)
#define forv(i,v) forn(i,sz(v))
#define fors(i,s) for(auto i=(s).begin();i!=(s).end();++i)
#define all(v) (v).begin(),(v).end()
using namespace std;
typedef long long in;
typedef vector<in> VI;
typedef vector<VI> VVI;
void trm(map<in,in>& tt, in df){
  map<in,in>::iterator it;
  it=tt.begin();
  in tdf=df;
  if(tdf<0)
    tdf*=-1;
  if(df!=0){
    while(it!=tt.end()){
      tt[it->first+tdf]-=it->second;
      if(tt[it->first+tdf]==0)
	tt.erase(it->first+tdf);
      ++it;
    }
  }
  if(df<0){
    it=tt.end();
    while(it!=tt.begin()){
      --it;
      tt[it->first+tdf]+=it->second;
      tt[it->first]=0;
    }
    map<in,in>::iterator it2;
    it=tt.begin();
    while(it!=tt.end()){
      it2=it;
      ++it2;
      if(it->second==0)
	tt.erase(it->first);
      it=it2;
    }
  }
  if(df==0){
    while(it!=tt.end()){
      it->second/=2;
      ++it;
    }
  }
}
map<in,in> tt,orig;
void docase(){
  in p;
  cin>>p;
  in n=0;
  tt.clear();
  in cc;
  forn(i,p){
    cin>>cc;
    tt[cc]=0;
  }
  fors(i,tt){
    cin>>i->second;
    n+=i->second;
  }
  orig=tt;
  for(in i=0;i<62;i++){
    if((1LL<<i)==n){
      n=i;
      break;
    }
  }
  VI mnb(0);
  forn(i,n){
    map<in,in>::iterator it;
    it=tt.begin();
    in c1=it->first;
    in c2;
    if(it->second>1)
      c2=it->first;
    else{
      ++it;
      c2=it->first;
    }
    in df=c2-c1;
    mnb.PB(df);
    trm(tt,df);/*
    cout<<"added "<<df<<endl;
    fors(j,tt){
      cout<<j->first<<" "<<j->second<<endl;
    }
    cout<<"done"<<endl;*/
  }
  sort(all(mnb));
  VI sol=mnb;
  /*
  sol.clear();
  in gl=-(orig.begin()->first);
  for(in i=sz(mnb)-1;i>=0;i--){
    in cc=mnb[i];
    mnb.pop_back();
    if(hasol(mnb,gl-cc)){
      sol.PB(-cc);
      gl-=cc;
    }
    else
      sol.PB(cc);
  }*/
  sort(all(sol));
  forv(i,sol)
    cout<<sol[i]<<" ";
  cout<<endl;
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
