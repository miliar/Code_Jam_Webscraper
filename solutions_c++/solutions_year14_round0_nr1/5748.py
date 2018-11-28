#include <iostream>

using namespace std;

int main()
{
   int n,i,j,k,l,a[4][4],b[4][4],ans[2],coun=0,count=0,m,p,q;
   cin>>n;
   if(n<=100&&n>=1)
  { for(i=0;i<n;i++)
   {   count=0;coun=0;
       for(j=0;j<2;j++)    
       {   
          cin>>ans[j];
          if(ans[j]<=1&&ans[j]>=4)
            return 0;
          if(j==0)
         {for(k=0;k<4;k++)
          {
              for(l=0;l<4;l++)
              {
                  cin>>a[k][l];
                  if(a[k][l]>16||a[k][l]<0)
                  return 0;
              }
          }  
         }
          else
          {for(k=0;k<4;k++)
          {
              for(l=0;l<4;l++)
              {
                  cin>>b[k][l];
                  if(b[k][l]>16||b[k][l]<0)
                  return 0;
              }
          }
              
          }
       
       }
     for(j=1;j<=16;j++)  
      {coun=0;
      for(k=0;k<4;k++)
          {
              for(l=0;l<4;l++)
              {
                 if(j==a[k][l])
                 coun++;
              }
          }
        if(coun>1)
        return 0;
     } 
      
    m=ans[0]-1;p=ans[1]-1;
    for(j=0;j<4;j++)
      {
         
         for(k=0;k<4;k++)
          {
              if(a[m][j]==b[p][k])
              {count++;
               q=a[m][j];
              }
          
          }
          
      }
   
   if(count==0)
   {
       cout<<"Case #"<<i+1<<": Volunteer cheated!\n";

   }
    if(count>1)
   {
       cout<<"Case #"<<i+1<<": Bad magician!\n";

   }
    if(count==1)
    {cout<<"Case #"<<i+1<<": "<<q<<"\n";}  
   }
  }
   return 0;
}
