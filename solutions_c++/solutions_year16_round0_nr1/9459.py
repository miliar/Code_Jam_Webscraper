#include <iostream>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#define lli long long int
#define pb push_back
#define mod 1000000007
#define pii pair<int,int>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
   int t,j,c,flag=0,l;
   int a[10]={0};
   lli n,k,g,i=1;
   cin>>t;
   for(j=1;j<=t;j++)
   {
      cin>>n;
      k=n;g=n;
      i=1;
      flag=0;
      for(l=0;l<10;l++)a[l]=0;
      if(n==0)
        cout<<"Case #"<<j<<": "<<"INSOMNIA"<<endl;
      else
         {
           while(flag==0)
              { k=i*g;
                 n=k;
                 while(n>0)
                   {
                     c=n%10;
                     a[c]=1;
                     n=n/10;
                   }
                if(a[0]==1 && a[1]==1 && a[2]==1 && a[3]==1 && a[4]==1 && a[5]==1 && a[6]==1 && a[7]==1 && a[8]==1 && a[9]==1)
                   flag=1;
                 i++;
                }
         cout<<"Case #"<<j<<": "<<k<<endl;
         }
       }
       return 0;
       }





