#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
 ll t;
 cin>>t;
 for(ll j=1;j<=t;j++)
 {
     ll max;
     cin>>max;
     string s;
     cin>>s;
     ll len=s.size(),ctr=0,sum=0;

     sum=sum+s[0]-'0';

     for(ll i=1;i<len;i++)
     {
        if(s[i]!='0')
        {
         if(sum>=i)
         {
             sum=sum+s[i]-'0';
         }
         else
         {
             ctr=ctr+i-sum;
             sum=sum+s[i]-'0'+ctr;
         }
        }
     }
     cout<<"Case #"<<j<<": "<<ctr<<"\n";
 }
}
