#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<iostream>
#include<math.h>
#include<limits.h>
#include<algorithm>
#include<vector>
using namespace std;
long long int dp[1000005]={0},a[1000000],b[1000000];
long long int min(long long int x,long long int y)
{
     if(x<y)
     return x;
     else
     return y;
}
long long int reve(long long int n)
{
     long long int a=0,k;
     while(n!=0)
     {
                k=n%10;
                a=a*10;
                a=a+k;
                n=n/10;
     }
     return a;
}
int main()
{
    freopen("A-small-attempt0 (2).in","r",stdin); freopen("gcjafout.txt","w",stdout);
    long long int t,T,flag,i,cnt,n;
    for(i=1;i<=1000000;i++)
    {
                           dp[i]=i;
                           a[i]=0;
    }
    cnt=2;
    a[1]=1;
    while(1)
    {
            flag=0;
            for(i=1;i<=1000000;i++)
            b[i]=0;
            for(i=1;i<=1000000;i++)
            {
                                   if(a[i]==1)
                                   {
                                              dp[i+1]=min(dp[i+1],cnt);
                                              dp[reve(i)]=min(dp[reve(i)],cnt);
                                              if(dp[i+1]==cnt)
                                              {
                                                              flag=1;
                                                              b[i+1]=1;
                                              }
                                              if(dp[reve(i)]==cnt)
                                              {
                                                              flag=1;
                                                              b[reve(i)]=1;
                                              }
                                   }
            }
            for(i=1;i<=1000000;i++)
            {
                                   a[i]=b[i];
            }
            if(flag==0)
            break;
            else
            {
                cnt++;
            }
    }
    scanf("%lld",&T);                                                  
    for(t=1;t<=T;t++)
    {
                     scanf("%lld",&n);
                     printf("Case #%lld: %lld\n",t,dp[n]);                     
    }
    return 0;
}
