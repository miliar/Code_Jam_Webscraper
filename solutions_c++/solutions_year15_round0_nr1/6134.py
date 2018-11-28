#include<iostream>
#include<cstdio>
#include<algorithm>
#include<string.h>
using namespace std;
int t,ar,s,i,c,pt;
string vd;
int main()
{
     //freopen("A-large.in","r",stdin);
     //freopen("AL.txt","w",stdout);
     cin>>t;
     c=t;
     while(t--)
     {
         cin>>s;
         cin>>vd;
         ar=0;pt=0;
         for(i=1;i<vd.length();i++)
         {
             ar+=(int)(vd[i-1]-'0');
             if(ar<i) {pt+=i-ar; ar+=i-ar;}
         }
         cout<<"Case #"<<c-t<<": "<<pt<<"\n";
     }
     return 0;
}
