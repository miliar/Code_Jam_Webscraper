#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{   freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
   ll k,t;
   cin>>t;

   for(k=1;k<=t;k++)
   {
     ll ans,i,num,q,n;
     cin>>n;
     if(n==0)
     {

         cout<<"Case #"<<k<<": "<<"INSOMNIA"<<endl;
         continue;
     }
     set<ll>s;
     s.clear();
     int flag=0;
     for(i=1;i*n<INT_MAX;i++)
      { num=i*n;
        q=num;
        while(q>0)
        {
            s.insert(q%10);
            q=q/10;
            if(s.size()==10)
            {   ans=num;
                flag=1;
                break;
            }
        }
        if(flag==1)break;

      }
       cout<<"Case #"<<k<<": "<<ans<<endl;
   }
    return 0;
}
