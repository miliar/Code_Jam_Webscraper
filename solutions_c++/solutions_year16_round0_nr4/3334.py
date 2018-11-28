#include<iostream>
#include<stdio.h>
using namespace std;

 int main()
 {
     int T,j=1;
     cin>>T;
     while(j<=T)
     {
         int K,C,S,i=1;
         cin>>K>>C>>S;

        cout<<"Case #"<<j<<":";
         while(i<=K)
         {
            cout<<" "<<i;

            i++;
         }
         cout<<"\n";
         j++;
     }

     return 0;

 }
