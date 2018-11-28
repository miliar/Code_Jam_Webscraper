#include<iostream>
using namespace std;
int main()
{   freopen("B-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,cnt=0;
    cin>>t;
    while(t--)
    {       
              cnt++;
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
                                            int p=1;
                                            for(int k=0;k<m;k++)
                                            {
                                                    if(a[i][k]!=a[i][j])
                                                    {
                                                                        p=0;
                                                                        break;
                                                    }
                                            }
                                            if(p==0)
                                            {
                                                    p=1;
                                                    for(int k=0;k<n;k++)
                                                    {
                                                    if(a[k][j]!=a[i][j])
                                                    {
                                                                        p=0;
                                                                        break;
                                                    }
                                                    }
                                            }
                                            if(p==0)
                                            {
                                                    ans=0;
                                                    break;
                                            }
                              }
                      }
                      if(ans==0)
                      break;
              }
              cout<<"Case #"<<cnt<<": ";
              if(ans==0)
              cout<<"NO"<<endl;
              else
              cout<<"YES"<<endl;
    }
    //system("pause");
    return 0;
}
 
