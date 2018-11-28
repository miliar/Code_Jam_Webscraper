#include<iostream>
#include<cstdio>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<cassert>
#include<sstream>
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
struct eg{
  in dest,c,f,rev;
};
struct flow{
  vector<bool> vtd;
  vector<vector<eg> > egs;
  vector<vector<in> > ept;
  vector<in> dtt;
  in n,s,t,tot,inf;
  void ini(in pn, in ps, in pt){
    n=pn;s=ps;t=pt;
    egs.resize(0);
    ept.resize(0);
    ept.resize(n,vector<in>(0));
    egs.resize(n,vector<eg>(0));
    dtt.resize(0);
    dtt.resize(n);
    tot=0;
    inf=1000000000000000LL;
    vtd.resize(n);
  }
  void add(in a, in b, in c1, in c2=0){
    eg ta,tb;
    ta.dest=b;
    tb.dest=a;
    ta.f=tb.f=0;
    ta.c=c1;
    tb.c=c2;
    ta.rev=egs[b].size();
    tb.rev=egs[a].size();
    egs[a].push_back(ta);
    egs[b].push_back(tb);
  }
  in doit(in u, in lim){
    if(u==t)
      return lim;
    in cfl=0;
    in dlm;
    in pl;
    while(cfl<lim && ept[u].size()>0){
      eg& tp=egs[u][ept[u].back()];
      dlm=lim-cfl;
      if(dlm>tp.c-tp.f)
	dlm=tp.c-tp.f;
      pl=doit(tp.dest,dlm);
      tp.f+=pl;
      egs[tp.dest][tp.rev].f-=pl;
      if(pl<dlm || dlm==0)
	ept[u].pop_back();
      cfl+=pl;
    }
    return cfl;
  }
  in dinic(){
    while(true){
      for(in i=0;i<n;i++){
	ept[i].resize(0);
	dtt[i]=inf;
      }
      queue<in> q;
      dtt[t]=0;
      q.push(t);
      while(!q.empty()){
	in u=q.front();
	q.pop();
	for(in i=0;i<egs[u].size();i++){
	  eg& tp=egs[u][i];
	  if(dtt[tp.dest]<inf)
	    continue;
	  if(egs[tp.dest][tp.rev].c==egs[tp.dest][tp.rev].f)
	    continue;
	  dtt[tp.dest]=dtt[u]+1;
	  q.push(tp.dest);
	}
      }
      for(in i=0;i<n;i++)
	vtd[i]=0;
      vtd[s]=1;
      q.push(s);
      while(!q.empty()){
	in u=q.front();
	q.pop();
	for(in i=0;i<egs[u].size();i++){
	  eg& tp=egs[u][i];
	  if(dtt[tp.dest]+1>dtt[u])
	    continue;
	  if(tp.f==tp.c)
	    continue;
	  ept[u].push_back(i);
	  if(!vtd[tp.dest])
	    q.push(tp.dest);
	  vtd[tp.dest]=1;
	}
      }
      in pl=doit(s,inf);
      if(pl==0)
	break;
      tot+=pl;
    }
    return tot;
  }
};
flow tfl;
set<string> hastobeeng,hastobefr;
map<pair<string,in>,in> idofword;
in s,t;
map<pair<in,in>,in> idofsent;
vector<vector<string> > inp;
map<string,in> apinlat;
set<string> apineng;
void docase(){
  in n;
  cin>>n>>ws;
  apineng.clear();
  apinlat.clear();
  hastobeeng.clear();
  hastobefr.clear();
  idofword.clear();
  idofsent.clear();
  inp.clear();
  inp.resize(n);
  string prp;
  in wid=0;
  forn(i,n){
    getline(cin,prp);
    stringstream is(prp);
    while(is>>prp){
      inp[i].PB(prp);
      if(i>=2)
	apinlat[prp]++;
      if(i==0)
	apineng.insert(prp);
    }
  }
  in totpen=0;
  s=wid++;
  t=wid++;
  forv(j,inp[1]){
    if(apineng.count(inp[1][j]) && !apinlat[inp[1][j]])
      totpen++;
  }
  forn(i,n){
    forn(j,2)
      idofsent[MP(i,j)]=wid++;
    forv(j,inp[i]){
      if(apinlat[inp[i][j]]>=1 && !idofword.count(MP(inp[i][j],0))){
	forn(k,2)
	  idofword[MP(inp[i][j],k)]=wid++;
      }
    }
  }
  tfl.ini(wid,s,t);
  const in inf=10000000LL;
  tfl.add(s,idofsent[MP(1,1)],inf);
  tfl.add(idofsent[MP(0,0)],t,inf);
  in pnl=0;
  fors(it,idofword){
    if(it->first.second==0)
      tfl.add(s,it->second,1);
    else
      tfl.add(it->second,t,1);
    pnl--;
  }
  forn(i,n){
    tfl.add(idofsent[MP(i,0)],idofsent[MP(i,1)],inf);
    forv(j,inp[i]){
      if(idofword.count(MP(inp[i][j],0))){
	tfl.add(idofword[MP(inp[i][j],0)],idofsent[MP(i,0)],inf);
	tfl.add(idofsent[MP(i,1)],idofword[MP(inp[i][j],1)],inf);
      }
    }
  }
  cout<<tfl.dinic()+pnl/2+totpen<<endl;
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
