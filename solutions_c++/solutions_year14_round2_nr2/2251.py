#include <bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
        int T;
        cin>>T;
        int t;
         ll i,j;
        for(t=1;t<=T;t++)
        {
        ll ans=0;
        
              ll A,B,K;
              cin>>A>>B>>K;
             
              for(i=0;i<A;i++)
              {
                for(j=0;j<B;j++)
              {
                if((i&j)<K)ans++;
              }
              }
              cout<<"Case #"<<t<<": "<<ans<<endl;
        }
        
        return 0;
}

