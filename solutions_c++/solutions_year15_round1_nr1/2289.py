#include<iostream>
#include<stdio.h>
using namespace std;
#define lli long long int
lli a[100000];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("outa.txt","w",stdout);
    lli t,i,n,y,z,temp,max,j=1;
    cin>>t;
    
    while(t--)
    {
              cin>>n;
              
              for(i=0;i<n;i++)
              cin>>a[i];
              
              y=0;temp=0;
              z=0;max=0;
              
              for(i=0;i<n-1;i++)
              {
                              temp=a[i]-a[i+1];
                              if(temp>0)
                              y+=temp;
                              
                              if(temp>max)
                              max=temp;
              }
             // cout<<max<<"max"<<endl;
              for(i=0;i<n-1;i++)
              {
                              temp=a[i];
                              if(temp>max)
                              z+=max;
                              else
                              z+=a[i];
                             // cout<<"z"<<z<<endl;
              }
              
              cout<<"Case #"<<j<<": "<<y<<" "<<z<<endl;
              j++;
    }
    
    return 0;
}

