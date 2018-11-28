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
string cp(in p, in r, in s){
  if(r+p+s==1){
    if(r)
      return "R";
    if(p)
      return "P";
    return "S";
  }
  in pr=(p+r-s)/2;
  in ps=(p-pr);
  in rs=(r-pr);
  assert(s==ps+rs);
  if(pr<0 || ps<0 || rs<0)
    return "";
  //pr<ps<rs
  string cc=cp(pr,ps,rs);
  string rt;
  forv(i,cc){
    if(cc[i]=='P')
      rt+="PR";
    if(cc[i]=='R')
      rt+="PS";
    if(cc[i]=='S')
      rt+="RS";
  }
  return rt;
}
void docase(){
  in n,r,p,s;
  cin>>n>>r>>p>>s;
  string cc=cp(p,r,s);
  if(cc==""){
    cout<<"IMPOSSIBLE"<<endl;
    return;
  }
  cout<<cc<<endl;
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
