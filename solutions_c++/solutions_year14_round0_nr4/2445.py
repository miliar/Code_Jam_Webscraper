#include<stdio.h>
#include<algorithm>
#include<vector>
#include<iostream>
using namespace std;
int main()
{
    freopen("outwarlarge.in","w",stdout);
    freopen("inwarlarge.in","r",stdin);
    int t,t1;
    scanf("%d",&t);
    t1=t;
    while(t--)
    {
              int n,i,j;
              scanf("%d",&n);
              vector<double> a(n);
              vector<double> b(n);
              vector<double> ac(n);
              vector<double> bc(n);
              for(i=0;i<n;i++)
              scanf("%lf",&a[i]);
              
              for(i=0;i<n;i++)
              scanf("%lf",&b[i]);
              
              sort(a.begin(),a.end());
              sort(b.begin(),b.end());
              for(i=0;i<n;i++)
              {
                              ac[i]=a[i];
                              bc[i]=b[i];
              }              
              int war=0;
              for(i=0;i<n;i++)
              {
                              for(j=0;j<n;j++)
                              if(b[j]>a[i])
                              {
                                   b[j]=-1;
                                   break;
                              }
                              if(j==n)
                              war++;        
              }
           //   printf("%d\n",war);
              
              
              int flag=1,start=0,end=n;
              
              while(flag)
              {
                         
                         
                         for(i=0;i<n-start;i++)
                         {
                                          if(ac[start+i]<bc[i])
                                          break;   
                         }
                         if(i==(n-start))
                         {
                                         break;
                         }
                         else
                         {
                             start++;
                         }
              
              }
              printf("Case #%d: %d %d\n",t1-t,n-start,war);
              
    }
    return 0;
}
