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
VI s;
VI sh,sl;
vector<int> isinh,isinl,isinq;
VVI subs;
VI m;
struct hg{
  in id,s;
  hg(in a=0, in b=0){
    id=a;s=b;
  }
  bool operator<(const hg cp)const{
    if(s!=cp.s)
      return s<cp.s;
    return id<cp.id;
  }
};
struct lw{
  in id,s;
  lw(in a=0, in b=0){
    id=a;s=b;
  }
  bool operator<(const lw cp)const{
    if(s!=cp.s)
      return s<cp.s;
    return id<cp.id;
  }
};
priority_queue<hg> rmh;
priority_queue<lw> adl;
void docase(){
  while(!rmh.empty())
    rmh.pop();
  while(!adl.empty())
    adl.pop();
  in n,d;
  cin>>n>>d;
  in s0,as,cs,rs;
  cin>>s0>>as>>cs>>rs;
  in m0,am,cm,rm;
  cin>>m0>>am>>cm>>rm;
  s.resize(n);
  m.resize(n);
  s[0]=s0;
  m[0]=m0;
  for(in i=1;i<n;i++){
    s[i]=(s[i-1]*as+cs)%rs;
    m[i]=(m[i-1]*am+cm)%rm;
  }
  for(in i=1;i<n;i++)
    m[i]%=i;
  m[0]=0;
  sh=sl=s;
  for(in i=1;i<n;i++){
    sh[i]=max(sh[i],sh[m[i]]);
    sl[i]=min(sl[i],sl[m[i]]);
  }
  subs=VVI(n,VI(0));
  for(in i=1;i<n;i++)
    subs[m[i]].PB(i);
  isinh=vector<int>(n,1);
  isinl=vector<int>(n,0);
  isinq=vector<int>(n,0);
  forn(i,n){
    if(sz(subs[i])==0){
      rmh.push(hg(i,sh[i]));
      isinq[i]=1;
    }
  }
  adl.push(lw(0,sl[0]));
  in bst=0;
  in ttl=0;
  while(!adl.empty()){
    lw tp=adl.top();
    adl.pop();
    forv(i,subs[tp.id])
      adl.push(lw(subs[tp.id][i],sl[subs[tp.id][i]]));
    isinl[tp.id]=1;
    ttl+=isinh[tp.id];
    while(!rmh.empty() && rmh.top().s>tp.s+d){
      hg tt=rmh.top();
      isinh[tt.id]=0;
      ttl-=isinl[tt.id];
      rmh.pop();
      if(tt.id!=0){
	if(!isinq[m[tt.id]]){
	  rmh.push(hg(m[tt.id],sh[m[tt.id]]));
	  isinq[m[tt.id]]=1;
	}
      }
    }
    bst=max(bst,ttl);
  }
  cout<<bst<<endl;
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
