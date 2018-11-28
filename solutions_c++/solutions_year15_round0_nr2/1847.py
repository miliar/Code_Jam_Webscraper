#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<stack>
#define oo 1000
#define MAXN 1005
using namespace std;  
int p[MAXN],dp[MAXN][MAXN]; 
int main()
{
      int cases,T,n,x,i,j,k,ans,temp;
      freopen("B-large.in","r",stdin);
      freopen("output.txt","w",stdout);
      memset(dp,0x7f,sizeof(dp));
      for (i=1;i<=oo;i++)
         for (j=1;j<=oo;j++)
         { 
               if (i<=j) dp[i][j]=0;
               for (k=1;k<i;k++)
                  dp[i][j]=min(dp[i-k][j]+dp[k][j]+1,dp[i][j]); 
         }
         
      scanf("%d",&T); 
      for (cases=1;cases<=T;cases++)
      { 
             scanf("%d",&n);
             for (i=1;i<=n;i++) scanf("%d",&p[i]);
             ans=MAXN;
             for (j=1;j<=oo;j++)
             {
                   temp=j;
                   for (i=1;i<=n;i++) temp+=dp[p[i]][j];
                   ans=min(ans,temp);
             }
             printf("Case #%d: %d\n",cases,ans);   
      }
      return 0;
}
