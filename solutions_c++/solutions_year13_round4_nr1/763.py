#include <iostream>
#include <cstdio>
#include <vector>
#include <list>
#include <complex>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <cstring>
#include <stack>
#include <cmath>
#include <iomanip>
#include <sstream>
#include <cassert>
#include <numeric>
using namespace std;
typedef long long ll;
typedef ll li;
typedef pair<int,int> PI;
#define EPS (1e-6)
#define rep(i,n) for(int i=0;i<(int)(n);++i)
#define REP(i, n) rep (i, n)
#define F first
#define S second
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)
#define min3(a,b,c) min((a),min((b),(c)))
#define min4(a,b,c,d) min((a),min3((b),(c),(d)))
#define SZ(a) (int)((a).size())
#define ALL(a) a.begin(),a.end()
#define FLL(a,b) memset((a),b,sizeof(a))
#define CLR(a) memset((a),0,sizeof(a))
#define FOR(it,a) for(__typeof(a.begin())it=a.begin();it!=a.end();++it)
template<typename T,typename U> ostream& operator<< (ostream& out, const pair<T,U>& val){return out << "(" << val.F << ", " << val.S << ")";}
template<class T> ostream& operator<< (ostream& out, const vector<T>& val){out << "{";rep(i,SZ(val)) out << (i?", ":"") << val[i];return out << "}";}
typedef double FP;
typedef complex<FP> pt;
typedef pt P;
typedef pair<pt,pt> line;
FP dot(P a,P b){return real(conj(a)*b);}
FP crs(P a,P b){return imag(conj(a)*b);}
P ortho(P a){return P(imag(a),-real(a));}
P ortho(line a){return ortho(a.S-a.F);}
P crspt(P a,P b,P c,P d){b-=a,d-=c;return a+b*crs(d,c-a)/crs(d,b);}
P crspt(line a,line b){return crspt(a.F,a.S,b.F,b.S);}
bool onl(P a1,P a2,P b){return abs(b-a1)+abs(b-a2)<abs(a1-a2)+EPS;}
bool onl(line a,P b){return onl(a.F,a.S,b);}
bool iscrs(line a,line b){P c=crspt(a,b);return onl(a,c)&&onl(b,c);}
void pkuassert(bool t){t=1/t;};
int dx[]={0,1,0,-1,1,1,-1,-1};
int dy[]={1,0,-1,0,-1,1,1,-1};
enum{TOP,BTM,LFT,RGT,FRT,BCK};
int dxdy2ce[]={RGT,FRT,LFT,BCK};
int s2i(string& a){stringstream ss(a);int r;ss>>r;return r;}
template<class T> T shift(T a,int b,int c,int d,int e){
  __typeof(a[0])t=a[b];
  a[b]=a[c];a[c]=a[d];a[d]=a[e];a[e]=t;return a;}
template<class T> T rgt(T a){return shift(a,TOP,LFT,BTM,RGT);}
template<class T> T lft(T a){return shift(a,TOP,RGT,BTM,LFT);}
template<class T> T frt(T a){return shift(a,TOP,BCK,BTM,FRT);}
template<class T> T bck(T a){return shift(a,TOP,FRT,BTM,BCK);}
line mkl(P a,P v){return line(a,a+v);}
FP lpdist(line a,P b){return abs(b-crspt(a,mkl(b,ortho(a))));}
FP spdist(line a,P b){
  P c(crspt(a,mkl(b,ortho(a))));
  return onl(a,c)?abs(b-c):min(abs(a.F-b),abs(a.S-b));
}
FP ssdist(line a,line b){
  return
    iscrs(a,b)?0.:
    min4(spdist(a,b.F),spdist(a,b.S),
         spdist(b,a.F),spdist(b,a.S));
}

ll MOD=1000002013;
int n,m;
ll e[1000],o[1000],p[1000];

void solve(int ca){
  cin >> n >> m;
  ll ans=0;
  ll rco=0;

  priority_queue<pair<ll,pair<ll,ll> > > q;
  rep(i,m){
    cin >> o[i] >> e[i] >> p[i];
    q.push(mp(-o[i],mp(1,p[i])));
    q.push(mp(-e[i],mp(0,p[i])));
    if(o[i]!=e[i]) {
      ll k=e[i]-o[i];
      ll cc=(n*k%MOD-k*(k+1)/2%MOD);
      rco+=((cc)%MOD+MOD)%MOD*p[i]%MOD;
      rco%=MOD;
      rco+=MOD;
      rco%=MOD;
    }
    //cout << rco << endl;
  }

  map<ll,ll> ik;
  while(!q.empty()){
    ll co=-q.top().F;
    ll ev=q.top().S.F;
    ll pe=q.top().S.S;
    q.pop();
    //cout << co << ' ' << ev << ' ' << pe << endl;
    if(ev){
      ik[co]+=pe;
      continue;
    }
    while(pe){
      ll di= ik.rbegin()->F;
      ll dp=ik.rbegin()->S;
      ll mv=min(dp,pe);      
      if(dp<=pe)ik.erase(di);
      else ik[di]-=mv;
      ll k=co-di;

      //cout << "mv " << mv << ' ' << k << endl;
      pe-=mv;
      if(k){
	ll cc=(n*k%MOD-k*(k+1)/2%MOD);
	ans+=(cc%MOD+MOD)%MOD*mv%MOD;
	ans%=MOD;
	ans+=MOD;
	ans%=MOD;
      }
    }
  }
  
  if(!ik.empty())
    FOR(it,ik) cout << it->F << ' ' << it->S << endl;

  assert(ik.empty());
  //cout << rco << ' ' << ans << endl;
  printf("Case #%d: %lld\n",ca,((rco-ans)%MOD+MOD)%MOD);
}

int main(int argc, char *argv[])
{
  int t;
  cin >> t;
  rep(i,t) solve(i+1);
  return 0;
}
