#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
     int t,i,j;
   int s,x,y;
   int ans[1000];
   char a[1000];
   cin>>t;
   for(i=0;i<t;i++)
   {
       ans[i]=0;
       cin>>s;
       cin>>a;
       x=a[0]-48;
       y=a[1]-48;
       for(j=0;j<s;j++)
       {
           if(((j+1)>x)&&(y!=0))
           {
               ans[i]+=(j+1-x);
               x=j+1+y;
               y=a[j+2]-48;
           }
           else
           {
               x=x+y;
               y=a[j+2]-48;
           }
       }
   }
   for(i=0;i<t;i++)
   cout<<"Case #"<<i+1<<": "<<ans[i]<<endl;
  return 0;
}
