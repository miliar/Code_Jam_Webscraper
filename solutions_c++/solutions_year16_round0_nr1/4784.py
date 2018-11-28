#include <iostream>
#include <stdio.h>
#include<string>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;
typedef long long int ll;
map<ll,ll>m;
void getDigits(ll a){
  while(a){
  m[a%10]=1;
  a/=10;
  }
}
int main()
{
    freopen("in", "r",stdin );
    freopen("out.txt", "w",stdout );

    ll t;cin>>t;
    for(ll i=1;i<=t;i++){
       cout<<"Case #"<<i<<": ";
       int n;cin>>n;
       if(n==0){cout<<"INSOMNIA\n";continue;}
       m.clear();
       ll j=1;
       while(m.size()!=10){
          getDigits(j*n);j++;
       }
       cout<<(j-1)*n;
       cout<<"\n";
    }
    return 0;
}
