#include <iostream>
using namespace std;
int main()
{ 
 freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);    
int t,n,m;
cin>>t;
for(int cas=1;cas<=t;cas++)
{
        cin>>n>>m;
        int a[n][m];
        for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
        cin>>a[i][j];
        int valid1=0;
        for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
        {  
         if(a[i][j]==1) //check if it valid 1 or not
          { int norow=0,nocol=0; 
          for(int col=0;col<m;col++)
           {   if(a[i][col]!=1)
            {  norow=1;
                  break;
                  } 
           }       
            for(int row=0;row<n;row++)
            {  if(a[row][j]!=1)
                { nocol=1;
                 break;
                 }
           }      
                 if(norow==1 && nocol==1)
                 valid1=1;
          }
          if(valid1==1)
          break;
        }
        if(valid1==1)
        cout<<"Case #"<<cas<<": NO\n";
        else
        cout<<"Case #"<<cas<<": YES\n";
        
}
//getchar();
return(0);
}
