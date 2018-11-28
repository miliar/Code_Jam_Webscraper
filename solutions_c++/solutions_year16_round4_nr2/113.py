#include<iostream>
#include<cmath>
#include<string.h>
#include<stdio.h>
#include<algorithm>
using namespace std;

int n,k;
int t;

double p[211];

double q[211];
double ans;
double dp[211][211];

int main()
{
    int i,j,times;
    int z;
    int xx;
    freopen("B-large.in","r",stdin);
    freopen("ans.out","w",stdout);
    
    cin>>t;
    
    for(times=1;times<=t;times++)
    {
         cin>>n>>k;
         
         for(i=1;i<=n;i++)
         {
             cin>>p[i];
         }
         
         sort(p+1,p+n+1);
         
         ans=0.0;
         
         for(z=0;z<=k;z++)
         {
             for(j=1;j<=i;j++)
             {
                 q[j]=p[j];
             }
             xx=z+1;
             for(j=n-(k-z)+1;j<=n;j++)
             {
                 q[xx]=p[j];
                 xx++;
             }
             
             for(i=0;i<=k;i++)
             {
                 for(j=0;j<=k;j++)
                 {
                     dp[i][j]=0.0;
                 }
             }
             dp[0][0]=1.0;
             
             for(i=1;i<=k;i++)
             {
                 for(j=0;j<=i;j++)
                 {
                     if(j>0)
                     {
                        dp[i][j]=dp[i-1][j]*(1.0-q[i])+dp[i-1][j-1]*(q[i]);
                     }
                     else
                     {
                         dp[i][j]=dp[i-1][j]*(1.0-q[i]);
                     }
                 }
             }
             /*
             for(i=1;i<=k;i++)
             {
                 cout<<q[i]<<' ';
             }
             cout<<endl;
             cout<<"(*&^%$#@"<<endl;
             
             for(i=0;i<=k;i++)
             {
                 for(j=0;j<=k;j++)
                 {
                      cout<<dp[i][j]<<' ';
                 }
                 cout<<endl;
             }
             */
             ans=max(ans,dp[k][k/2]);
         }
         
         cout.precision(8);
         cout.setf(ios::fixed);
         cout<<"Case #"<<times<<": "<<ans<<endl;
    }
    
    
    
    return 0;
}
