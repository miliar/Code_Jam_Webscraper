#include <iostream>
#include <bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
   ll t,n,temp,c=0;
   cin>>t;
   ll a[3000]={0};
   while(t--){c++;
       cin>>n;
        for(ll i=0;i<3000;i++)a[i]=0;
       for(ll i=0;i<2*n-1;i++){
           for(ll j=0;j<n;j++){
               cin>>temp;
               a[temp]++;
           }
       }
   cout<<"Case #"<<c<<": ";
   for(ll i=0;i<3000;i++){
       if(a[i]>0&&a[i]%2==1)cout<<i<<' ';
   }
   cout<<endl;
}

return 0;
}
