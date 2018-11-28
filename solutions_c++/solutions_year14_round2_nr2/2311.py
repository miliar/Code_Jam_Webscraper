#include<iostream>
#include<string>
#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<math.h>
#include<set>
#include<map>
using namespace std;

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
   freopen("B-small-attempt0.out","w",stdout);
    int t,ti;
    cin>>ti;
    for(t=1;t<=ti;t++)
    {
     int a,b,k,i,j;
     cin>>a>>b>>k;
     int ans=0;
     for(i=0;i<a;i++)
     {
         for(j=0;j<b;j++)
         {
           //cout<< (i & j);
             if( (i & j) < k)
                ans++;
         }
     }
     printf("\nCase #%d: %d",t,ans);
    }
    return 0;
}
