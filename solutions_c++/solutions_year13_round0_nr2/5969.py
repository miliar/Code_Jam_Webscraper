#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    int test,cases=0;
    cin>>test;
    while(test--)
    {
              cases++;
              int n,m,ans=1;
              cin>>n>>m;
              int a[n][m];
              for(int i=0;i<n;i++)
              {
                      for(int j=0;j<m;j++)
                      {
                              cin>>a[i][j];
                      }
              }
              for(int i=0;i<n;i++)
              {
                      for(int j=0;j<m;j++)
                      {
                              if(a[i][j]==1)
                              {
                                            int flag=1;
                                            for(int k=0;k<m;k++)
                                            {
                                                    if(a[i][k]!=a[i][j])
                                                    {
                                                                        flag=0;
                                                                        break;
                                                    }
                                            }
                                            if(flag==0)
                                            {
                                                    flag=1;
                                                    for(int k=0;k<n;k++)
                                                    {
                                                    if(a[k][j]!=a[i][j])
                                                    {
                                                                        flag=0;
                                                                        break;
                                                    }
                                                    }
                                            }
                                            if(flag==0)
                                            {
                                                    ans=0;
                                                    break;
                                            }
                              }
                      }
                      if(ans==0)
                      break;
              }
              cout<<"Case #"<<cases<<": ";
              if(ans==0)
              cout<<"NO"<<endl;
              else
              cout<<"YES"<<endl;
    }
  
    return 0;
}
