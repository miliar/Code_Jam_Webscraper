#include<iostream>
#include<cstring>
#include<stdio.h>
using namespace std;
int main()
{
       freopen("B-large.in","r",stdin);
       freopen("Output2.txt","w",stdout);
       long long int t,j=0;
       cin>>t;
       while(t--)
       {
              long long int l,i,count=0;
              string str;
              j++;
              cin>>str;
              l=str.length();
              for(i=1;i<l;i++)
              {
                     if(str[i-1]!=str[i])
                     count++;
              }

              if(str[l-1]=='-')
              count++;
              cout<<"Case #"<<j<<": "<<count<<endl;
       }
}
