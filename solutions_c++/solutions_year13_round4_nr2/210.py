#include<iostream>
using namespace std;
typedef long long ll;
ll bcd(ll n, ll p){
  ll mn, mx, md, nb, brk;
  mn=0;
  mx=1LL<<n;
  while(mx-mn>1){
    md=(mx+mn)/2;
    brk=0;
    nb=((1LL<<n)-1)-md;
    for(ll i=n;i>0;i--){
      if(nb==0)
	break;
      brk+=(1LL<<(i-1));
      nb=(nb-1)/2;
    }
    if(brk+p>=(1LL<<n))
      mn=md;
    else
      mx=md;
  }
  return mn;
}
int main(){
  ll t,n,p;
  cin>>t;
  for(int z=1;z<=t;z++){
    cin>>n>>p;
    cout<<"Case #"<<z<<": ";
    if(p==(1LL<<n))
      cout<<(p-1)<<" "<<(p-1)<<endl;
    else
      cout<<((1LL<<n)-2-bcd(n,(1LL<<n)-p))<<" "<<bcd(n,p)<<endl;
  }
  return 0;
}
