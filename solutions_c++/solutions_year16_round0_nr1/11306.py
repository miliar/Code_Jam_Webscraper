#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

int main()
{
   freopen("jam.txt","w",stdout);
   int t;cin>>t;
   for(int i=1;i<=t;i++){
      ll n;cin>>n;
      if(n==0) cout<<"Case #"<<i<<": INSOMNIA"<<endl;
      else {
            ll p=0,u=0;
         map<ll,bool>m;
         while(1){
               if(m.size()==10){
                  cout<<"Case #"<<i<<": "<<u<<endl;
                  break;
               }
            p=p+1;
            u=n*p;
            ll temp=u;
            //cout<<u<<endl;
            while(temp>0){
               ll x=temp%10;
               temp=temp/10;
               m[x]=true;
               //cout<<temp<<endl;
            }
         }

      }
   }
}
