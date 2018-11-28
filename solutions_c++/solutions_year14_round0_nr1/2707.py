#include<iostream>
#include<stdio.h>
using namespace std;
int a[5][5],b[5][5];
int c[20];
int main()
{
    int t,k,m,n,cnt,m1,i,j;
    cin>>t;
    k=1;
    while(k<=t)
    {
         scanf("%d",&m);
         cnt=0;
         for(i=0;i<4;i++)
         {
           for(j=0;j<4;j++)
             cin>>a[i][j];                
         }
         scanf("%d",&n);
         for(i=0;i<4;i++)
         {
           for(j=0;j<4;j++)
             cin>>b[i][j];                
         }
         for(i=0;i<20;i++)
           c[i]=0;
         for(j=0;j<4;j++)
           c[a[m-1][j]]++;
         for(j=0;j<4;j++)
           c[b[n-1][j]]++; 
         for(i=0;i<20;i++)
         {
            if(c[i]==2)
            {   
                m1=i;
                cnt++;
            }              
         }
         if(cnt==0)
           cout<<"Case #"<<k<<": "<<"Volunteer cheated!"<<"\n";
         else if(cnt==1)
          cout<<"Case #"<<k<<": "<<m1<<"\n";
         else
           cout<<"Case #"<<k<<": "<<"Bad magician!"<<"\n";
         k++;        
    }
   return 0;   
}
