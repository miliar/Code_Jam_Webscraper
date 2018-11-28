#include<cstdio>
#include<cstring>
#include<vector>
#include<string>
#include<iostream>
#include<algorithm>
#include<queue>
#include<set>
#include<map>
#include<cmath>
using namespace std;
typedef long long ll;
int T;
bool check( ll a ){
  int keta=0;
  ll tmp = a;
  while( a>0 ){
    a/=10;
    keta++;
  }
  a=tmp;
  ll k2 = 1;
  ll k1 = 1;
  for(int i=1;i<keta;i++,k2*=10);
  bool f=true;
  for(;k2>k1;k2/=10,k1*=10){
    //cout << (a%(k2*10))/k2 <<" " <<(a%(k1*10))/k1<<endl;
    if( (a%(k2*10))/k2 != (a%(k1*10))/k1 ){
      f=false; break;
    }
  }
  if(!f) return false;
  return true;
}
bool solve( ll a ){
  if( !check(a) ) return false;
  if( !check(a*a) ) return false;
  return true;
}
int main()
{
  cin >> T;
  for(int loop=1;loop<=T;loop++){
    ll a,b;
    cin >> a >> b;
    ll tar = (ll)sqrt(b);
    ll tmp = a;
    a = (ll)(sqrt(a));
    if( a*a < tmp ) a = a+1; 
    int res = 0;
    for(ll i=a;i<=tar;i++){
      //      cout << i << "\n";
      if(solve(i)) res++;
    }
    cout << "Case #" << loop << ": "<< res <<"\n";
  }
}
