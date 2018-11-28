/*input
2
8 10 8
3 2 3
*/
#include "bits/stdc++.h"
using namespace std;

#define ll      long long
#define vll     vector< long long >
#define vvll    vector< vll >
#define vd      vector< double > 
#define forP(i,x,a) for(ll i=x;i<=a;++i)
#define forM(i,x,a) for(ll i=x;i>=a;--i)
#define all(a) a.begin(), a.end()
#define put(x) printf("%I64d",x);
#define get(x) scanf("%I64d",&x);
#define ENDL printf("\n");
const ll mod = 1e9+7;

#define X first
#define Y second

ll abso( ll a){
  return (a<0)?-a:a;
}
ll PrimeDiv(ll n){
  if(n==2||n==3)return 0;
  if(!(n%2))return 2;
  for(ll j=3;j*j<=n;j+=2){
      if(!(n%j)) return j;
  }
  return 0;
}

ll calcNum(ll a,ll base){
  ll ans=0,p=1;
  for(int i=0;i<16;i++){
    ans += (a&1)*p;
    //cout<<p<<':'<<ans<<' ';
    p*=base;
    a=a>>1;
  }
  return ans;
}
string i2b(ll a){
  string rv,rvr;
  for(int i=0;i<16;i++){
    rvr += '0'+(a&1);
    //cout<<p<<':'<<ans<<' ';
    a=a>>1;
  }
  for(int i=rvr.length()-1;i>=0;i--){
    rv+=rvr[i];
  }
  return rv;
}

int main(int argc, char const *argv[])
{
 ios::sync_with_stdio(0);
 cin.tie(0);
 ll cases,t,k,c,s;
 cin>>t;
 for(cases=1;cases<=t;cases++){
  cin>>k>>c>>s;
  if(s==k){
    printf("Case #%lld: ",cases );
    for(ll i=1;i<=s;i++){
      printf("%lld ",i);
    }
    putchar('\n');
  }
 }



  return 0;
}