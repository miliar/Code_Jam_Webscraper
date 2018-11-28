#include<iostream>
#include<stdio.h>
using namespace std;

 int main()
 {
     int t,x=1;
     cin>>t;
     while(x<=t)
     {
         int k,c,s,i=1;
         cin>>k>>c>>s;

        cout<<"Case #"<<x<<": ";
         while(i<=k)
         {
            cout<<i<<" ";
            i++;
         }
         cout<<"\n";
         x++;
     }

     return 0;

 }

