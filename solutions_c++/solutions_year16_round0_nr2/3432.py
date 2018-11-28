/*input
5
-
-+
+-
+++
--+-
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

int main(int argc, char const *argv[])
{
 ios::sync_with_stdio(0);
 cin.tie(0);
 ll t,cases;
 string s;
 cin>>t;
 for(cases=1;cases<=t;cases++){
    cin>>s;
    char curr=s[0];
    ll changes=0;
    for(int i=1;i<s.length();i++){
      if(s[i]!=curr){
        changes++;curr=s[i];
      }
    }
    if(s[s.length()-1]=='-')changes++;
    printf("Case #%lld: %lld\n",cases,changes );
  }
  
  return 0;
}