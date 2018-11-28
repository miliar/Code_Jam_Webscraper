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
struct eg{
  in dest,c,f,rev;
};
struct flow{
  vector<vector<eg> > egs;
  vector<vector<in> > ept;
  vector<bool> opt;
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
    opt.resize(n);
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
      cfl+=pl;
      if(pl<dlm || tp.f==tp.c)
	ept[u].pop_back();
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
      forn(i,n)
	opt[i]=0;
      opt[s]=1;
      q.push(s);
      while(!q.empty()){
	in u=q.front();
	q.pop();
	for(in i=0;i<egs[u].size();i++){
	  eg& tp=egs[u][i];
	  assert(tp.f<=tp.c);
	  if(tp.f==tp.c)
	    continue;
	  assert(dtt[tp.dest]+1>=dtt[u]);
	  if(dtt[tp.dest]+1>dtt[u])
	    continue;
	  ept[u].push_back(i);
	  if(!opt[tp.dest])
	    q.push(tp.dest);
	  opt[tp.dest]=1;
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
in w,h,b;
vector<vector<bool> > fr;
in dd[4][2]={{0,1},{1,0},{0,-1},{-1,0}};
int main(){
  in T;
  cin>>T;
  forn(zz,T){
    cout<<"Case #"<<zz+1<<": ";
    cin>>w>>h>>b;
    fr.clear();
    fr.resize(w,vector<bool>(h,1));
    forn(i,b){
      in x0,y0,x1,y1;
      cin>>x0>>y0>>x1>>y1;
      for(in j=x0;j<=x1;j++){
	for(in k=y0;k<=y1;k++){
	  fr[j][k]=0;
	}
      }
    }
    flow tt;
    in s=w*h*2;
    in t=w*h*2+1;
    tt.ini(w*h*2+2,s,t);
    forn(i,w){
      forn(j,h){
	if(!fr[i][j])
	  continue;
	tt.add(i*h+j,i*h+j+w*h,1);
	forn(k,4){
	  in ni=i+dd[k][0];
	  in nj=j+dd[k][1];
	  if(ni>=0 && ni<w && nj>=0 && nj<h && fr[ni][nj]){
	    tt.add(i*h+j+w*h,ni*h+nj,1);
	  }
	}
	if(j==0)
	  tt.add(s,i*h+j,1);
	if(j==h-1)
	  tt.add(i*h+j+w*h,t,1);
      }
    }
    cout<<tt.dinic()<<endl;
  }
  return 0;
}

