#include<iostream>
#include<cmath>
using namespace std;
int main()
{
   int tt,i;
   long long int r,t,k;
   cin>>tt;
   for(i=1;i<=tt;i++)
   {
      cin>>r>>t;
      k=(1+sqrt(4*r*(r-1)+8*t+1)-2*r)/4;
      cout<<"Case #"<<i<<": "<<k<<endl;
   }
}
