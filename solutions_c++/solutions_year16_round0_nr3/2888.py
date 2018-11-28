/*input
1
6 10
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
 ll t,n,j2=0,done=0;
 cin>>t>>n>>j2;
 ll ek=j2;
 //printf("%lld ",j2);
 printf("Case #1:\n");
 ll i = 1<<(n-1);i++;
 //cout<<calcNum(35,2)<<' ';
 done=0;
 
 for(i;i<(ll)(1<<n) && done<ek;i+=2){
    //printf("%lld %lld fddhf\n",done,j2);
    //cout<<i<<':';
    ll arr[10]={0};
    ll base;
    for(base=2;base<11;base++){
      ll num=PrimeDiv(calcNum(i,base));
      //cout<<base<<'|'<<calcNum(i,base) << '-' << num<<'\n';
      if(num==0)break;
      arr[base]=num;
    }
    if(base!=11)continue;
    done++;
    //printf("hfdsjkf %lld\n",done);
    printf("%s ",i2b(i).c_str());
    for(int i=2;i<11;i++){
      printf("%lld ",arr[i]);
    }
    putchar('\n');
  }



  return 0;
}