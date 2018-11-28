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
typedef int in;
typedef vector<in> VI;
typedef vector<VI> VVI;
in n;
VI pr;
VVI cd;
VI sst;
VI blg,lb,dcd;
in fnd(in u){
  in a=u;
  while(dcd[u]!=u)
    u=dcd[u];
  in ta;
  while(a!=u){
    ta=a;
    a=dcd[a];
    dcd[ta]=u;
  }
  return u;
}
void fsamp(VI& res){
  forn(i,n)
    dcd[i]=i;
  in nxt=0;
  forn(i,n){
    if(pr[i]==-1){
      lb[i]=nxt;
      forn(j,sst[i]){
	blg[nxt++]=i;
      }
    }
  }
  in u,p,t;
  in tn=n;
  while(sz(res)!=n){
    if((n-sz(res))*5<tn){
      nxt=0;
      forn(i,tn){
	if(blg[i]!=-1){
	  blg[nxt]=blg[i];
	  if(nxt==0 || blg[nxt]!=blg[nxt-1])
	    lb[fnd(blg[nxt])]=nxt;
	  ++nxt;
	}
      }
      tn=nxt;
      assert(tn!=0);
    }
    u=rand()%tn;
    while(blg[u]==-1)
      u=rand()%tn;
    p=fnd(blg[u]);
    res.PB(p);
    nxt=lb[p];
    assert(nxt==0 || blg[nxt-1]!=blg[nxt]);
    assert(blg[nxt]==blg[u]);
    forv(i,cd[p]){
      t=cd[p][i];
      lb[t]=nxt;
      if(sst[t]*2<sst[p]){
	forn(j,sst[t]){
	  blg[nxt++]=t;
	}
      }
      else{
	dcd[p]=t;
	nxt+=sst[t];
      }
    }
    blg[nxt]=-1;
  }
  /*
  forn(i,n)
    cout<<res[i]<<" ";
  cout<<endl;
  */
}
in dfs(in u){
  in c=1;
  forv(i,cd[u]){
    c+=dfs(cd[u][i]);
  }
  sst[u]=c;
  return c;
}
VI trp;
bool issb(string& a, string& b){
  in n=sz(a);
  in m=sz(b);
  trp.resize(n);
  trp[0]=-1;
  for(in i=1;i<n;++i){
    trp[i]=trp[i-1];
    while(trp[i]!=-1 && a[trp[i]]!=a[i-1])
      trp[i]=trp[trp[i]];
    ++trp[i];
  }
  in msf=0;
  forn(i,m){
    while(msf!=-1 && a[msf]!=b[i])
      msf=trp[msf];
    ++msf;
    if(msf==n)
      return 1;
  }
  return 0;
}
void docase(){
  cin>>n;
  pr=VI(n);
  cd=VVI(n,VI(0));
  forn(i,n){
    cin>>pr[i];
    --pr[i];
    if(pr[i]!=-1)
      cd[pr[i]].PB(i);
  }
  dcd=lb=blg=VI(n,0);
  sst=VI(n,0);
  forn(i,n){
    if(pr[i]==-1)
      dfs(i);
  }
  string ltr;
  cin>>ltr;
  vector<string> cwd;
  in m;
  cin>>m;
  cwd.resize(m);
  forn(i,m)
    cin>>cwd[i];
  VI gsp(m,0);
  in nsamp=50000;
  VI tp;
  string ts;
  forn(i,nsamp){
    tp.clear();
    fsamp(tp);
    ts.clear();
    forv(j,tp)
      ts.PB(ltr[tp[j]]);
    forn(j,m){
      if(issb(cwd[j],ts))
	++gsp[j];
    }
  }
  cout<<setprecision(6);
  forn(j,m)
    cout<<double(gsp[j])/double(nsamp)<<" ";
  cout<<endl;
}
int main(){
  ios::sync_with_stdio(0);
  cin.tie(0);
  in T;
  cin>>T;
  for(in zz=1;zz<=T;zz++){
    cerr<<zz<<endl;
    cout<<"Case #"<<zz<<": ";
    docase();
  }
  return 0;
}
