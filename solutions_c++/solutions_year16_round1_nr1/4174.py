#include<iostream>
#include<cstring>
#include<stdio.h>
using namespace std;
int main()
{
       freopen("A-large (1).in","r",stdin);
       freopen("Output1.txt","w",stdout);
       long long int t,j=0,b=0;
       cin>>t;
       while(t--)
       {
              b++;
              string s;
              long long int k,n;
              cin>>s;
              n=s.size();
              char a[n];
              a[0]=s[0];
              for(int i=1;i<n;i++)
              {
                     if(s[i]<a[0])
                     a[i]=(char)s[i];
                     else
                     {
                            for(j=i;j>0;j--)
                            a[j]=a[j-1];
                            a[0]=(char)s[i];
                     }
              }
              cout<<"Case #"<<b<<": ";
              for(int i=0;i<n;i++)
              cout<<a[i];
              cout<<endl;
       }
}
