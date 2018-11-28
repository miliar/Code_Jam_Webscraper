#include<iostream>
#include<stdio.h>
#define MAX 1000000
using namespace std;
long long int reverse(long long int n)
{
   long long int rev=0,rem;
   while(n!=0)
  {
     rem=n%10;
     rev=rev*10+rem;
     n/=10;
  }     
   return rev;  
}
long long int dp[MAX];
/*long long int cntWays(long long int n)
{
    if(n==1)
    {
      dp[1]=1;
      return 1;
    }
    else if(n<MAX && dp[n])     
     return dp[n];
    else if(dp[n]==0)
    {
        if(dp[n-1] && dp[reverse(n)])
        {
            dp[n]=min(dp[n-1],dp[reverse(n)])+1;
            return dp[n];           
        }
        else
        return min(cntWays(n-1),cntWays(reverse(n)))+1 ;    
    }
    else
      return min(cntWays(n-1),cntWays(reverse(n)))+1 ;    
}*/
void cntWays(long long int n)
{
    dp[1]=1;
    long long int i,c;    
    for(i=2;i<=n;i++)
    {
       c=reverse(i);
      if(c<i && dp[reverse(i)] && i%10)
         dp[i]=min(dp[i-1],dp[reverse(i)])+1;
      else 
        dp[i]=dp[i-1]+1;
    }
}
int main()
{
    int t,k=1;
    long long int n,i,cnt,x;
    scanf("%d",&t); 
    dp[0]=0;
    for(i=1;i<MAX;i++)
       dp[i]=0;
    cntWays(MAX);
    while(t--)
    {
      scanf("%lld",&n);          
      printf("Case #%d: %lld\n",k,dp[n]);
      k++;
    }
   return 0;
}
