#include <functional>/*{{{*/
#include <algorithm>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <numeric>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <cmath>
#include <stack>
#include <list>
#include <map>
#include <set>
using namespace std;typedef long long ll;typedef long double real;void run();int main(){ios::sync_with_stdio(0);run();}/*}}}*/

ll const inf=1ll<<60ll;
ll const lots=1000002013ll;
ll n,m;

unsigned long long get(unsigned long long k){
  return k*(n*2+1-k)/2;
}

struct tick_t{
  ll s,t,weight;

  tick_t(ll s=0,ll t=0,ll weight=1):s(s),t(t),weight(weight){
    return;
  }

  bool operator<(tick_t const &a)const{
    return s!=a.s? a<a.s: t<a.t;
  }

  ll cost() const{
    return get(t-s)%lots;
  }
};

tick_t plan[1000];

static ll muner[8192];
pair<ll,ll> seg[8192];
ll pdn[8192];

void push(ll x,ll l,ll r){
  if (l+1<r){
    pdn[x*2+1]+=pdn[x];
    pdn[x*2+2]+=pdn[x];
  }
  seg[x].first+=pdn[x];
  pdn[x]=0;
}

pair<ll,int> findmin(int a,int b,int x=0,int l=0,int r=4096){
  push(x,l,r);

  if (b<=l || r<=a) return {inf,1<<30};
  if (a<=l && r<=b) return seg[x];

  ll m=(l+r)/2;
  pair<ll,int> res=min(findmin(a,b,x*2+1,l,m),findmin(a,b,x*2+2,m,r));
  seg[x]=min(seg[x*2+1],seg[x*2+2]);
  return res;
}

void add(ll a,ll b,ll delt,int x=0,int l=0,int r=4096){
  push(x,l,r);

  if (b<=l || r<=a) return;
  if (a<=l && r<=b) {pdn[x]+=delt;push(x,l,r);return;}

  ll m=(l+r)/2;
  add(a,b,delt,x*2+1,l,m);
  add(a,b,delt,x*2+2,m,r);

  seg[x]=min(seg[x*2+1],seg[x*2+2]);
}

ll go(ll l,ll r){
  if (l>=r) return 0;
  ll res=0;

  auto m=findmin(l,r);

  if (m.first>0){
    ll will=get(muner[r]-muner[l]);
    res+=(will%lots)*(m.first%lots);
    add(l,r,-m.first);
  }

  if (m.second<l or m.second>=r){
    cerr<<"ERROR! "<<l<<" - ("<<m.first<<", "<<m.second<<") - "<<r<<endl;
    exit(1);
  }

  res+=go(l,m.second);
  res+=go(m.second+1,r);

  return res%lots;
}

void run(){
  int tsts; cin>>tsts;
  for (int tst=1; tst<=tsts; ++tst){

    cin>>n>>m;
    for (int i=0; i<m; i++) cin>>plan[i].s>>plan[i].t>>plan[i].weight;
    ll nick=0; for (int i=0; i<m; i++){ll u=plan[i].cost()%lots; (nick+=(u*(plan[i].weight%lots)%lots))%=lots;}
    sort(plan,plan+m);

    map<ll,int> renum;
    for (int i=0; i<m; i++) renum[plan[i].s]=renum[plan[i].t]=0;
    int unq=0; for (auto &i: renum) i.second=unq, muner[unq]=i.first, ++unq;

    for (int i=8192; i--;) pdn[i]=0;
    for (int i=0; i<4096; i++) seg[i+4095]={0,i};
    for (int i=4095; i--;) seg[i]=seg[i*2+1];

    for (int i=0; i<m; i++){
      add(renum[plan[i].s],renum[plan[i].t],plan[i].weight);
    }

    ll toast=go(0,unq)%lots;
    cout<<"Case #"<<tst<<": "<<(nick-toast+lots)%lots<<endl;
  }
}

