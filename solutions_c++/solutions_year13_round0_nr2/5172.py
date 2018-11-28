#include<stdio.h>
#include<map>
#include<vector>
#include<iostream>
#include<algorithm>

using namespace std;

#define mod 1000000007

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int t,ct=1;
    cin>>t;
    while(t--)
    {
    int n,i,j,m,val;
    int row[200],col[200];
    int a[200][200];
 cin>>n>>m;

 for(i=0;i<n;i++)
 for(j=0;j<m;j++)
 cin>>a[i][j];


 int mx=0;

 for(i=0;i<n;i++)
   { mx=a[i][0];
       for(j=0;j<m;j++)
         {
           if(a[i][j]>mx)
           {mx=a[i][j];}  
             
         }
         row[i]=mx;
   }    
 
 for(i=0;i<m;i++)
   { mx=a[0][i];
       for(j=0;j<n;j++)
         {
           if(a[j][i]>mx)
           {mx=a[j][i];}  
             
         }
         col[i]=mx;
   }    
 
int flag=0;
 for(i=0;i<n;i++)
   {
       for(j=0;j<m;j++)
         {
             if(a[i][j]<row[i] && a[i][j]<col[j])
               {flag=1; break;}
         }
         if(flag==1)
         break;
   } 
if(flag==1)
{cout<<"Case #"<<ct<<": "<<"NO"<<"\n"; ct++;}
else
{cout<<"Case #"<<ct<<": "<<"YES"<<"\n"; ct++;}


}
//cin>>i;
return 0;    
}
