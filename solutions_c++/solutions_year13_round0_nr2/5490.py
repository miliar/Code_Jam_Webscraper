#include<iostream>
#include<cstdio>
using namespace std;
 
int main()
{
    int t,x,m,i,j,k,maxno,n,flag;
    int no[110][110],dp[110][110];
    cin>>t;
    x=t;
    while(t--)
    {
              
              cin>>n>>m;
              cout<<"Case #"<<x-t<<": ";
              for(i=0;i<n;i++)
              for(j=0;j<m;j++)
              scanf("%d",&no[i][j]);
              
              for(i=0;i<n;i++)
              for(j=0;j<m;j++)
              dp[i][j]=-1;
              
              flag=1;
              
              for(i=0;i<n;i++)
              {
                              maxno=0;
                              
                              for(j=0;j<m;j++)
                              maxno=max(no[i][j],maxno);
                              
                              
                              for(j=0;j<m;j++)
                              {
                                       if(dp[i][j]==-1)
                                       {
                                                 if(maxno!=no[i][j])
                                                 {
                                                              for(k=0;k<n;k++)
                                                              {
                                                                              if(dp[k][j]==-1)
                                                                              {
                                                                                              dp[k][j]=no[i][j];
                                                                              }
                                                                              else if(dp[k][j]!=no[i][j])
                                                                              flag=0;
                                                              }
                                                 }
                                                 
                                                 else
                                                 dp[i][j]=no[i][j];   
                                       }
                                       else
                                       if(dp[i][j]!=no[i][j])
                                       flag=0;                             
                              }
              }
                              if(flag)
                              cout<<"YES";
                              else
                              cout<<"NO";
                              cout<<"\n";
    }
          return 0;
}
