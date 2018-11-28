
#include <iostream>
#include <string>
#include <cmath>
#include <cstdio>
using namespace std;

int main()
{


   int t;
   cin>>t;
    for(int l=1;l<=t;l++)
   {
       unsigned long long int a,b,k;
       cin>>a>>b>>k;
       unsigned long long int ans=0;
       if(k>=a || k>=b)
       {
       ans+=a*b;
       }
       else
       {
       ans+=k*b;
       long long int m=a-k;
       for(long long int i=k;i<a;i++)
       {
       for(long long int j=0;j<b;j++)
          if((i & j)<k)
          {
            ans++;}
       }
       }

       cout<<"Case #"<<l<<": "<<ans<<endl;

   }
}
 










