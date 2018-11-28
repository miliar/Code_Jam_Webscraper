#include<iostream>
#include<algorithm>
#include<map>
using namespace std;
typedef long long ll;
ll MD=1000002013LL;
struct ev{
  int type;//0 going in, 1 going out
  ll loc;
  ll nmb;
  bool operator<(const ev cp)const{
    if(loc!=cp.loc)
      return loc<cp.loc;
    return type<cp.type;
  }
};
struct tick{
  ll stp;
  bool operator<(const tick cp)const{
    return stp>cp.stp;
  }
};
ev evs[10009];
int nmevs;
ll vl(ll a){
  return a*(a-1)/2;
}
int main(){
  ev tpv;
  ll t,n,m;
  cin>>t;
  ll basew;
  ll gdw;
  ll tpa,tpb;
  map<tick,ll> mp;
  for(int z=1;z<=t;z++){
    cin>>n>>m;
    nmevs=0;
    basew=0;
    gdw=0;
    for(int i=0;i<m;i++){
      cin>>tpa>>tpb>>tpv.nmb;
      basew+=(vl(tpb-tpa)%MD)*tpv.nmb;
      basew%=MD;
      tpv.type=0;
      tpv.loc=tpa;
      evs[nmevs++]=tpv;
      tpv.type=1;
      tpv.loc=tpb;
      evs[nmevs++]=tpv;
    }
    mp.clear();
    tick tpck;
    sort(evs,evs+nmevs);
    for(int i=0;i<nmevs;i++){
      if(evs[i].type==0){
	tpck.stp=evs[i].loc;
	mp[tpck]+=evs[i].nmb;
	continue;
      }
      while(evs[i].nmb>0){
	map<tick,ll>::iterator it=mp.begin();
	ll trm=it->second;
	if(evs[i].nmb<trm)
	  trm=evs[i].nmb;
	evs[i].nmb-=trm;
	gdw+=(vl(evs[i].loc-it->first.stp)%MD)*(trm%MD);
	gdw%=MD;
	mp[it->first]-=trm;
	if(mp[it->first]==0)
	  mp.erase(it->first);
      }
    }
    cout<<"Case #"<<z<<": "<<(MD+gdw-basew)%MD<<endl;
  }
  return 0;
}
