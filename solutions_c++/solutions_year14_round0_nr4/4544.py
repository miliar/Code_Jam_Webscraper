#include<iostream>
#include<stdio.h>
#include<string>
#include<math.h>
#include<vector>
#include<queue>
#include<string.h>
#include<algorithm>
using namespace std;
#define N 1000000
#define mod 1000000007
#define ll long long
#define ex 2.7182818284590452354
#define pi 3.141592653589793239
#define INFF 999999999
#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;
double a[1005],b[1005];
int c[1005],d[1005];
int main()
{
    int t;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
   scanf("%d",&t);
   for(int Case=1;Case<=t;Case++)
   {
       int n,i,j,k;
       memset(c,0,sizeof(c));
       memset(d,0,sizeof(d));
       int add=0,sum=0;
       scanf("%d",&n);
       for(i=0;i<n;i++)
       {
           scanf("%lf",&a[i]);
       }
       for(i=0;i<n;i++)
       {
           scanf("%lf",&b[i]);
       }
       sort(a,a+n);
       sort(b,b+n);
       printf("Case #%d: ",Case);
       for(i=0;i<n;i++)
       {
           for(j=0;j<n;j++)
           {
               if(a[i]>b[j]&&!c[j])
               {
                   add++;
                   c[j]=1;
                   break;
               }
           }
           for(k=0;k<n;k++)
           {
               if(b[i]>a[k]&&!d[k])
               {
                   sum++;
                   d[k]=1;
                   break;
               }
           }
       }
       printf("%d %d\n",add,n-sum);
   }
   return 0;
}
