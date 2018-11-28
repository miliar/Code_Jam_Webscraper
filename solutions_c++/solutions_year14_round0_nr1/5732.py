#include<iostream>
using namespace std;
int main()
{
int i,j,k,n,count,ans,c,t,a[20],b[7][7];
cin>>t;
for(k=1;k<=t;k++)
{
    count=0;
    for(i=0;i<20;i++)
    {
       a[i]=0;
    }
     cin>>ans;
     for(i=1;i<=4;i++)
     {
     for(j=1;j<=4;j++)
     {
        cin>>b[i][j];
     }
     }
     for(j=1;j<=4;j++)
     {
        a[b[ans][j]]++;
     }
     cin>>ans;
     for(i=1;i<=4;i++)
     {
       for(j=1;j<=4;j++)
       {
           cin>>b[i][j];
       }
     }
     for(j=1;j<=4;j++)
     {
        if(a[b[ans][j]]==1)
        {
          count++;
          c=b[ans][j];
        }
     }
     if(count==0)
     {
     cout<<"Case #"<<k<<": "<<"Volunteer cheated!\n";
     }
     else if(count==1)
     {
          cout<<"Case #"<<k<<": "<<c<<"\n";
     }
     else if(count>1)
     {
       cout<<"Case #"<<k<<": "<<"Bad magician!\n";
     }
}
return 0;
}
