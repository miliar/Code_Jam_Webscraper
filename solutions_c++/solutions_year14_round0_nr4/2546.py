#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <cmath>
#include <stdio.h>
#include <list>
#include <vector>
#include <map>
#include <set>
#include <limits.h>
#define ll long long int
#define mod 1000000009
using namespace std;

double a[1010];
double b[1010];
bool t[1010];
bool t2[1010];

int main()
{

 //freopen("C:\\Users\\jack\\Desktop\\in.txt","r",stdin);
 //freopen("C:\\Users\\jack\\Desktop\\out.txt","w",stdout);

    int test,ca;
    scanf("%d",&ca);
    test=1;
    while(test<=ca)
    {
     
     int n;
      scanf("%d",&n);
      
     for(int i=0;i<n;i++)
     { scanf("%lf",&a[i]);
        t[i]=false;t2[i]=false;
     }
      
       for(int i=0;i<n;i++)
         scanf("%lf",&b[i]);
      
             
     sort(a,a+n);
     sort(b,b+n);
     int prev=n-1;
     
     for(int i=n-1;i>=0;i--)
     {
             
     for(int j=prev;j>=0;j--)
        {
          if(a[i]>=b[j])
            {t[j]=true;prev=j-1;break;}   
             
          }        
             
     }
     
     prev=n-1;
     
     for(int i=n-1;i>=0;i--)
     {
             
     for(int j=prev;j>=0;j--)
        {
          if(b[i]>=a[j])
            {t2[j]=true;prev=j-1;break;}   
             
          }        
             
     }
     
    int ans=0;
    int cnt=0;
    
   for(int i=0;i<n;i++)
   { if(t[i]==true)cnt++;
      if(t2[i]==true)ans++;
   }

  printf("Case #%d: %d %d\n",test,cnt,n-ans);
       test++;
                 }

    }
