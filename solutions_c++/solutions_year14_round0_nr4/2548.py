#include<stdio.h>
#include<iostream>
#include<map>
#include<set>
#include<vector>
#include<queue>
#include<stack>
#include<algorithm>
#include<cstring>

#define MOD 1000000007
#define INF 2000000000

using namespace std;

int war(double a[],double b[],int n)
{
    int i,j=n-1;
    int ret=0;
    
    for(i=n-1;i>=0;i--)
    {
                       if(a[i]>b[j])
                       {
                                    ret++;
                       }
                       else
                       {
                           j--;
                       }
    }
    
    return ret;
}


int d_war(double a[],double b[],int n)
{
    int i,j=0;
    int ret=0;
    
    for(i=0;i<n;i++)
    {
                    if(a[i]>b[j])
                    {
                                 ret++;
                                 j++;
                    }
    }
    
    return ret;
}                    

int main()
{
    int n,i,t;
    
    double a[2000],b[2000];
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    scanf("%d",&t);
    int save=t;
    
    while(t--)
    {
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
              int ans1=d_war(a,b,n),ans2=war(a,b,n);
              
              printf("Case #%d: %d %d\n",save-t,ans1,ans2);
    }
    
    return 0;
}
