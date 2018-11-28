#include <bits/stdc++.h>

using namespace std;

#define ll long long
const ll N=1000001;

ll yes[N+1];

int main()
{
  ll t;
  cin>>t;
  for(ll i=1;i<=N;i++)
    {
      ll num=i;
      bool present[10];
      int total=0;
      memset(present,false,sizeof(present));
      for(ll j=1;;j++)
      {

        ll error=i*j;
        while(error>0)
        {
          ll d=error%10;
          error/=10;
          if(!present[d])
            present[d]=1,total++;
          if(total==10)
            { yes[i]=i*j;goto hello;}
        
        }
      }
      hello: ;
    }
  for(ll cases=1;cases<=t;cases++)
  {
    ll n;
    cin>>n;
    printf("Case #%lld: ",cases);
    if(n==0)
      cout<<"INSOMNIA\n";
    else cout<<yes[n]<<endl;


  }  
}