#include<iostream>
using namespace std;
int a[200][200],res[200][200];
int main()
{
    int t,x=1;
    cin>>t;
    while(t--)
    {
        int n,m;
        cin>>n>>m;
        for(int i=0;i<n;i++) for(int j=0;j<m;j++) cin>>a[i][j];
        
        for(int i=0;i<n;i++) for(int j=0;j<m;j++) res[i][j]=0;
        for(int j=0;j<m;j++)
        {
           int maxc=0;     
           for(int i=0;i<n;i++)
           {
               if(res[i][j]==0)    
                  maxc=max(maxc,a[i][j]);    
           }     
           for(int i=0;i<n;i++)
           {
               if(res[i][j]==0 && a[i][j]<maxc)
               {
                   for(int k=0;k<m;k++)
                   {
                       res[i][k]=a[i][j];    
                   }            
               }  
               else if(res[i][j]==0)
                 res[i][j]=a[i][j];  
           }
        }      

        /*for(int i=0;i<n;i++) 
        {
          for(int j=0;j<m;j++)
            cout<<res[i][j]<<" ";
           cout<<"\n";
        }*/
                
        bool flag=1;
        for(int i=0;i<n;i++) 
          for(int j=0;j<m;j++)
            if(res[i][j]!=a[i][j]) flag=0;
        
        if(flag) 
          printf("Case #%d: YES\n",x++);
        else 
          printf("Case #%d: NO\n",x++);
    }
}
