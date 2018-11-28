#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define FOR(i,n) for(int i=0;i<n;i++)
#define FORN(i,n) for(int i=1;i<n;i++)
#define FORM(i,a,b,n)for(int i=a;i<=b;i+=n)
#define all(v) v.begin(),v.end()
typedef vector<ll> vll;
int main(){
  freopen("A-large.in", "r", stdin);
  freopen("output2.out", "w", stdout);
  int t,c;
  ll n,ans,aux,p,v[10],x;
  cin>>t;
  for(int i=1;i<=t;i++){
    memset(v,0,sizeof(v));
    c=0;
    p=1;
    cin>>n;
    cout<<"Case #"<<i<<": ";
    if(n==0)puts("INSOMNIA");
    else{
      for(int p=1;c<10;p++){
        aux=n*p;
        ans=aux;
        while(aux){
          x=aux%10;
          if(v[x]==0) c++;
          v[x]++;
          aux/=10;
        }
      }
      cout<<ans<<endl;
    }
  }
  return 0;
}