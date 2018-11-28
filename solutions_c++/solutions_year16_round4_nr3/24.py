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
in nucd(char c, in cd){
  if(c=='/'){
    if(cd==0)
      return 1;
    if(cd==1)
      return 0;
    if(cd==3)
      return 2;
    if(cd==2)
      return 3;
  }
  else{
    if(cd==0)
      return 3;
    if(cd==3)
      return 0;
    if(cd==1)
      return 2;
    if(cd==2)
      return 1;
  }
  assert(0);
  return -1;
}
vector<string> bd;
VI mof;
in r,c;
VVI d={{0,1},{-1,0},{0,-1},{1,0}};
VI ttr(in st){
  in cx,cy,cd;
  if(st<c){
    cx=0;
    cy=st;
    cd=3;
  }
  if(st>=c && st<c+r){
    cx=st-c;
    cy=c-1;
    cd=2;
  }
  if(st>=c+r && st<c+r+c){
    cx=r-1;
    cy=c-1-(st-c-r);
    cd=1;
  }
  if(st>=c+r+c){
    cx=r-1-(st-c-r-c);
    cy=0;
    cd=0;
  }
  return {cx,cy,cd};
}
bool mrc(in st, in gl){
  in cx,cy,cd;
  VI tp=ttr(st);
  cx=tp[0];
  cy=tp[1];
  cd=tp[2];
  while(cx>=0 && cx<r && cy>=0 && cy<c){
    if(bd[cx][cy]=='.'){
      if(cd==3 || cd==1)
	bd[cx][cy]='\\';
      else
	bd[cx][cy]='/';
    }
    cd=nucd(bd[cx][cy],cd);
    cx+=d[cd][0];
    cy+=d[cd][1];
  }
  cx-=d[cd][0];
  cy-=d[cd][1];
  tp=ttr(gl);
  if(cx!=tp[0] || cy!=tp[1] || (cd+2)%4!=tp[2])
    return 0;
  return 1;
}
void docase(){
  cin>>r>>c;
  bd=vector<string>(r,string(c,'.'));
  VI pm(2*(r+c));
  forv(i,pm){
    cin>>pm[i];
    --pm[i];
  }
  mof.resize(2*(r+c));
  for(in i=0;i<sz(pm);i+=2){
    mof[pm[i]]=pm[i+1];
    mof[pm[i+1]]=pm[i];
  }
  VI cll(2*(r+c));
  forv(i,cll)
    cll[i]=i;
  while(sz(cll)){
    bool fd=0;
    forv(i,cll){
      if(mof[cll[i]]==cll[(i+1)%sz(cll)]){
	fd=1;
	if(!mrc(cll[i],mof[cll[i]])){
	  cout<<"IMPOSSIBLE"<<endl;
	  return;
	}
	if(i==sz(cll)-1){
	  forn(j,sz(cll)-2)
	    cll[j]=cll[j+1];
	  cll.resize(sz(cll)-2);
	}
	else{
	  for(in j=i;j<sz(cll)-2;++j)
	    cll[j]=cll[j+2];
	  cll.resize(sz(cll)-2);
	}
	break;
      }
    }
    if(!fd){
      cout<<"IMPOSSIBLE"<<endl;
      return;
    }
  }
  forv(i,bd){
    forv(j,bd[i]){
      if(bd[i][j]=='.'){
	bd[i][j]='/';
      }
      cout<<bd[i][j];
    }
    cout<<endl;
  }
}
int main(){
  ios::sync_with_stdio(0);
  cin.tie(0);
  in T;
  cin>>T;
  for(in zz=1;zz<=T;zz++){
    cout<<"Case #"<<zz<<":"<<endl;
    docase();
  }
  return 0;
}
