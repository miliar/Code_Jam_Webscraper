#include <iostream>
#include <stdio.h>

using namespace std;

int t,t1,a[5][5],ans,p,i,j,m[20],x;

main()
{
      
      freopen ("mt.in","r",stdin);
      freopen ("mt.out","w",stdout);
      
      
  cin>>t;
   t1=t;
   
     while (t--)
      {
           
          ans=0;
          for (i=1;i<=16;i++) 
          m[i]=0;
                 
           
        cin>>x;
         
          for (i=1;i<=4;i++)
           for (j=1;j<=4;j++)
            cin>>a[i][j];
          
          
         for (i=1;i<=4;i++)
          m[a[x][i]]=1;
       
       
         cin>>x;
         
          for (i=1;i<=4;i++)
           for (j=1;j<=4;j++)
            cin>>a[i][j];
        
          for (i=1;i<=4;i++)
           if (m[a[x][i]]==1)
            {
              ans++;
              p=a[x][i];      
            }
            
            cout<<"Case #"<<t1-t<<": ";
            
           if (ans==0) cout<<"Volunteer cheated!"<<endl; else
           if (ans==1) cout<<p<<endl; else
            cout<<"Bad magician!"<<endl;
         
            
            
            
      }


}
