#include<iostream>

using namespace std;

int main()
{
    int t;
    cin>>t;
    int i=1;
    while(i<=t)
    {  int c, b;
      cin>>c;
      int a[5][5]={0};
      int r[6]={0,0,0,0,0,0};
      int valr[6]={0,0,0,0,0,0};
      
      for(int i=1;i<=4;i++)
      {  for(int j=1;j<=4;j++)
         cin>>a[i][j];
       }
       
       for(int j=1;j<=4;j++)
         { r[j]=a[c][j];
          
         }
         
         cin>>b;
          for(int i=1;i<=4;i++)
      {  for(int j=1;j<=4;j++)
         cin>>a[i][j];
       }
       
     
     
     
     for(int k=1;k<=4;k++) 
     {  
       for(int j=1;j<=4;j++)
        { if(r[k]==a[b][j])
         valr[k]++;
         }
     }
     
     
         
         int flag=-1;
         int val=0;
         for(int j=1;j<=4;j++)
        { if(valr[j]==1)
           { flag++;
             val=r[j];
             }
         }
         
         if(flag==0)
         cout<<"Case #"<<i++<<": "<<val<<endl;
         else if(flag==-1)
         cout<<"Case #"<<i++<<": Volunteer cheated!"<<endl;
         else
         cout<<"Case #"<<i++<<": Bad magician!"<<endl;
         
         }
         
         return 0;
         }
         
         
         
       
       
       
      
      
          
