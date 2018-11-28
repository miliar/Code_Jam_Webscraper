#include<iostream>
#include<algorithm>
using namespace std;
typedef long long ll;
struct nd{
  ll val;
  ll ind,ind2;
  bool operator<(const nd cp)const{
    return val<cp.val;
  }
};
int t;
ll ar[10009][2];
nd nds[20009];
ll totv[10009][2];
ll dgs[109];
ll even(ll a){
  //cout<<"even"<<" "<<a;
  ll r=a;
  int i=0;
  while(r>0){
    dgs[i++]=r%10;
    r/=10;
    a*=10;
  }
  for(int j=0;j<i;j++){
    a+=dgs[j]*(1LL<<(i-1-j));
  }
  //cout<<" "<<a<<endl;
  return a;
}
ll odd(ll a){
  //cout<<"odd"<<" "<<a;
  ll r=a;
  int i=0;
  while(r>0){
    dgs[i++]=r%10;
    r/=10;
    a*=10;
  }
  a/=10;
  for(int j=1;j<i;j++){
    a+=dgs[j]*(1LL<<(i-1-j));
  }
  //cout<<" "<<a<<endl;
  return a;
}
bool ispal(ll a){
  ll r=a;
  int i=0;
  while(r>0){
    dgs[i++]=r%10;
    r/=10;
  }
  //cout<<"ispal"<<" "<<a<<endl;
  for(int j=0;j<i;j++){
    if(dgs[j]!=dgs[i-1-j])
      return false;
  }
  //cout<<1<<endl;
  return true;
}
void runs(){
  ll csm=0;
  int cind=0;
  ll cnmb=0;
  for(ll cst=1;cind<2*t;cst++){
    cnmb=odd(cst);
    cnmb*=cnmb;
    while(cind<2*t && cnmb>nds[cind].val){
      totv[nds[cind].ind][nds[cind].ind2]+=csm;
      cind++;
    }
    if(ispal(cnmb))
      csm++;
  }
  csm=0;
  cind=0;
  cnmb=0;
  for(ll cst=1;cind<2*t;cst++){
    cnmb=even(cst);
    cnmb*=cnmb;
    while(cind<2*t && cnmb>nds[cind].val){
      totv[nds[cind].ind][nds[cind].ind2]+=csm;
      cind++;
    }
    if(ispal(cnmb))
      csm++;
  }
}
int main(){
  cin>>t;
  for(int i=0;i<t;i++){
    cin>>ar[i][0]>>ar[i][1];
    nds[2*i].val=ar[i][0]-1;
    nds[2*i].ind=i;
    nds[2*i].ind2=0;
    nds[2*i+1].val=ar[i][1];
    nds[2*i+1].ind=i;
    nds[2*i+1].ind2=1;
    totv[i][0]=0;
    totv[i][1]=0;
  }
  sort(nds,nds+2*t);
  runs();
  for(int z=1;z<=t;z++){
    cout<<"Case #"<<z<<": ";
    cout<<totv[z-1][1]-totv[z-1][0]<<endl;
  }
  return 0;
}
