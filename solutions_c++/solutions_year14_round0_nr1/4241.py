#include<iostream>
#include<fstream>
using namespace std;

main()
{
    int a[4][4],b[4][4],m,n,t,k,i,j,flag,l;
    ifstream fin;
    fin.open("A-small-attempt0.txt"); 
    fin>>t;
    for(i=0;i<t;i++)
    {
     L:flag=0;
     fin>>m;
     for(j=0;j<4;j++)
      for(k=0;k<4;k++)
        fin>>a[j][k]; 
     fin>>n;   
     for(j=0;j<4;j++)
      for(k=0;k<4;k++)
       fin>>b[j][k];
     m--;
     n--;
     cout<<m+1<<"\n";
     for(j=0;j<4;j++)
     {
      for(k=0;k<4;k++)
      {
       cout<<a[j][k]<<" ";
      }
      cout<<"\n";
     }
     cout<<n+1<<"\n";
     for(j=0;j<4;j++)
     {
      for(k=0;k<4;k++)
      {
       cout<<b[j][k]<<" ";
      }
      cout<<"\n";
     }
     for(j=0;j<4;j++)
     {
      for(k=0;k<4;k++)
      {
       if(a[m][j]==b[n][k])
       { 
        if(flag==1)
        {
         cout<<"\nBad Magician!\n";
         i++;
         goto L;
        }     
        l=a[m][j];       
        flag=1;
       }
      }
     }
     if(flag==0)
     {
      cout<<"\nVolunteer Cheated!\n";
     }
     else
      cout<<"\nAnswer is: "<<l<<"\n";
    }
}
