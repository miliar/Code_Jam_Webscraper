#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
int main()
{
int t,n,m,i,j,f,count=1;

cin>>t;
while(t--)
{
          cin>>n>>m;
          int a[n][m],b[n][m];
     for(i=0;i<n;i++)
     for(j=0;j<m;j++)
     {cin>>a[i][j];
     b[i][j]=2;}
    // cout<<"A";
     for(i=0;i<n;i++)
     {
            f=0;
            if(a[i][0]==1)
            for(j=1;j<m;j++)
            {
                      if(a[i][j]==2)
                      {
                             f=1;
                             break;       
                                    }       
                            }   
            if(f==0 && a[i][0]==1)                
            for(j=0;j<m;j++)
            b[i][j]=1;
                }  
     // cout<<"B";          
      for(i=0;i<m;i++)
     {
            f=0;
            if(a[0][i]==1)
            for(j=1;j<n;j++)
            {
                      if(a[j][i]==2)
                      {
                             f=1;
                             break;       
                                    }       
                            }   
            if(f==0 && a[0][i]==1)                
            for(j=0;j<n;j++)
            b[j][i]=1;
                }  
      //cout<<"C";          
       f=0;
     for(i=0;i<n;i++)
     for(j=0;j<m;j++)
     if(a[i][j]!=b[i][j])
     {
                f=1;
                i=n;
                j=m;         
                         }   
                         
      if(f==1)
     cout<<"Case #"<<count++<<": NO"<<endl;
     else
     cout<<"Case #"<<count++<<": YES"<<endl;

          }
     
                         
    

return 0;
}
