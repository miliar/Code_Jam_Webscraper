#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
ll N,J;
string str;

ll isPrime(ll x){
  if(x<=1)return -1;

}

ll check(ll S,ll base){
  ll num=0;
  for(int i=0;i<N;i++){
    if(S>>i&1){
      num=num*base+1;
    }else{
      num*=base;
    }
  }
  //cout<<str<<' '<<S<<' '<<base<<' '<<num<<endl;
  if(num<=1)return -1;
  for(ll i=2;i*i<=num;i++)if(num%i==0)return num/i;
  return -1;
}

int main(){
  int T,C=0;
  cin>>T;
  for(int tc=1;tc<=T;tc++){
    cout<<"Case #"<<tc<<":"<<endl;
    cin>>N>>J;
    
    for(ll i=0;i<(1<<N);i++){
      if( (i&1LL)==0)continue;
      if( (i&(1LL<<(N-1))) ==0)continue;
      
      str="";
      for(int j=0;j<N;j++){
        if( i&(1<<j) )str+='1';
        else str+='0';
      }


      vector<ll> v;
      for(ll j=2;j<=10;j++){
        ll k=check(i,j);
        if(k!=-1)v.push_back(k);
        else break;
      }

      if(v.size()==9){
        cout<<str;
        for(int i=0;i<9;i++)cout<<' '<<v[i];
        cout<<endl;
        C++;
      }
      if(C==J)break;
    }
    
  }
                           
  return 0;
}
