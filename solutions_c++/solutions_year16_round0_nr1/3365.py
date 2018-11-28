/*input
5
0
1
2
11
1692
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
  ll t,cases=1,n;
  int arr[10]={0};
  ios::sync_with_stdio(0);cin.tie(0);
  cin>>t;
  for(cases=1;cases<=t;cases++){
    cin>>n;
    if(!n){printf("CASE #%d: INSOMNIA\n",cases);continue;}
    for(int i=0;i<10;i++)  arr[i]=0;
      ll ans;
    for(ll i=1;;i++ ){
      ll temp=i*n;
      while(temp!=0){
        arr[temp%10]++;
        temp/=10;
      }
      bool flag=1;
      for(int j=0;j<10;j++){
        if(arr[j]==0)flag=0;
      }
      if(flag)
        {printf("CASE #%lld: %lld\n",cases,i*n); break;}
    }

  }
  return 0;




  return 0;
}