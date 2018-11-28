#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(ll n){
  if(n==0){
    cout<<"INSOMNIA"<<endl;
    return;
  }
  set<ll> a;
  for(ll i=1;;i++){
    ll k=n*i;
    while(k){
      a.insert(k%10LL);
      k/=10LL;
    }
    if(a.size()==10){
      cout<< n*i <<endl;
      return;
    }
  }
  cout<<"ISONOMIA"<<endl;
}

int main(){
  int Tc;
  ll n;
  cin>>Tc;
  for(int tc=1;tc<=Tc;tc++){
    cout<<"Case #"<<tc<<": ";
    cin>>n;
    solve(n);
  }
  return 0;
}
