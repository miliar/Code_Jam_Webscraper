#include<iostream>
#include<cstdio>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<iomanip>
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
struct pip{
  double r,c;
  bool operator<(const pip cp)const{
    return c<cp.c;
  }
};
void ad(pip cpip, double& cvl, double& ctemp, double mt, double gv){
  double mad=mt*cpip.r;
  if(mad+cvl>gv)
    mad=gv-cvl;
  ctemp=(cvl*ctemp+mad*cpip.c)/(cvl+mad);
  cvl+=mad;x
}
in n;
double gv,gx;
const double eps=0.000000001;
vector<pip> pips;
bool ispo(double mt){
  double ctemp=0;
  double cvl=0;
  forv(i,pips){
    ad(pips[i],cvl,ctemp,mt,gv);
  }
  if(ctemp>gx || cvl<gv*(1-eps))
    return 0;
  ctemp=0;
  cvl=0;
  for(in i=sz(pips)-1;i>=0;i--)
    ad(pips[i],cvl,ctemp,mt,gv);
  if(ctemp<gx || cvl<gv-eps)
    return 0;
  return 1;
}
void docase(){
  cin>>n>>gv>>gx;
  pips.resize(n);
  forn(i,n)
    cin>>pips[i].r>>pips[i].c;
  sort(all(pips));
  const double inf=1000000000000000.0;
  double mn=0;
  double mx=inf;
  double md;
  if(!ispo(mx)){
    cout<<"IMPOSSIBLE"<<endl;
    return;
  }
  while(mx>mn+eps && mx>mn*(1+eps)){
    md=(mx+mn)/2.0;
    if(ispo(md))
      mx=md;
    else
      mn=md;
  }
  cout<<setprecision(15)<<mn<<endl;
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
