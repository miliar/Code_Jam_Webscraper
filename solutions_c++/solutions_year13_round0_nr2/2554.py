#include<iostream>
using namespace std;
int a[110][110];
int main()
{    freopen("C:\\Users\\Dell\\Desktop\\input.txt","r",stdin);
    freopen("C:\\Users\\Dell\\Desktop\\output.txt","w",stdout);
    int t,t1;
    cin>>t1;
    for(t=1;t<=t1;t++)
    {
                      int n,m,p=1,c=0,d=0,i1;
                      cin>>n>>m;
                      //int a[n][m];
                      int i,j;
                      for(i=0;i<n;i++)
                      {for(j=0;j<m;j++)
                      {
                                       cin>>a[i][j];
                      }
                      }
                                       for(i=0;i<n;i++)
                                       {
                                                       for(j=0;j<m;j++)
                                                       {c=0;d=0;
                                                                       
                                                                                     for(i1=0;i1<n;i1++)
                                                                                     {
                                                                                                        if(a[i1][j]>a[i][j])
                                                                                                        {c=1;break;}
                                                                                     }
                                                                                     for(i1=0;i1<m;i1++)
                                                                                     {
                                                                                                        if(a[i][i1]>a[i][j])
                                                                                                         {d=1;break;}
                                                                                     }
                                                                                     if(d==1 && c==1)
                                                                                     {p=0;break;}
                                                                       
                                                       }if(p==0)
                                                       break;
                                       }
                                        if(p==1)
                                        cout<<"Case #"<<t<<": YES"<<endl;
                                        if(p==0)
                                        cout<<"Case #"<<t<<": NO"<<endl; 
    }
    return 0;
}
                                                                                                                      
                                      