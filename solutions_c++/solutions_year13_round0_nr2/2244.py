#include<iostream>
using namespace std;

int main()
{
       freopen("input.in","r",stdin);
       freopen("output.in","w",stdout);
       int t,i,j,k,l1,k1,l,n,m,fl1,fk1;
       cin>>t;
       for(i=1;i<=t;i++)
       {
              cin>>n>>m;
              int mark[101]={0};
              int arr[n][m];
              int use[n][m],new_arr[n][m];
              for(j=0;j<n;j++)
              {
                     for(k=0;k<m;k++)
                     {
                            cin>>arr[j][k];
                            mark[arr[j][k]]=1;
                            use[j][k]=arr[j][k];
                     }
                     //use_row[j]=1;
              }
              cout<<"Case #"<<i<<": ";
              for(l=100;l>=1;l--)
              {
                     if(mark[l])
                     {
                            for(j=0;j<n;j++)
                            {
                                   for(k=0;k<m;k++)
                                   {
                                          fl1=0;
                                          fk1=0;
                                          if(arr[j][k]==l)
                                          {
                                                 for(l1=0;l1<n;l1++)
                                                 {
                                                        if(arr[l1][k]==-1)
                                                        {
                                                               fl1=1;
                                                               break;
                                                        }
                                                 }
                                                 if(!fl1)
                                                 for(l1=0;l1<n;l1++)
                                                 new_arr[l1][k]=arr[j][k];
                                                 
                                                 
                                                 for(k1=0;k1<m;k1++)
                                                 {
                                                        if(arr[j][k1]==-1)
                                                        {
                                                               fk1=1;
                                                               break;
                                                        }
                                                 }
                                                 if(!fk1)
                                                 for(k1=0;k1<m;k1++)
                                                 new_arr[j][k1]=arr[j][k];
                                                 arr[j][k]=-1;
                                          }
                                   }
                            }
                     }
              }
              int fi_flag=0;
                     for(j=0;j<n;j++)
                     {
                            for(k=0;k<m;k++)
                            {
                                   if(new_arr[j][k]!=use[j][k])
                                   {
                                          fi_flag=1;
                                          break;
                                   }
                            }
                            if(fi_flag)
                            break;
                     }
                     if(fi_flag)
                     cout<<"NO"<<endl;
                     else
                     cout<<"YES"<<endl;         
              
       }
              return 0;
       }   
                                                        
                                                        
              
              
