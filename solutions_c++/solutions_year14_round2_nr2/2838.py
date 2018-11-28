#include <iostream>
#include <string>
#include <cmath>
#include <cstdio>
using namespace std;

int main()
{
     freopen("B-small-attempt0.in","r",stdin);
freopen("b1a.out","w",stdout);
  int t;
   cin>>t;
   for(int l=1;l<=t;l++)
   {
       long int a,b,k;
       cin>>a>>b>>k;
       long int ans=0;
       for(int i=0;i<a;i++)
        for(int j=0;j<b;j++)
          if((i & j)<k)
            ans++;

       cout<<"Case #"<<l<<": "<<ans<<endl;

   }

   return 0;
}
