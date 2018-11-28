#include<iostream>
#include<cmath>
#include<cstdio>

using namespace std;
int main()
{
 
 int arr[100][100];
 int t,n,m,i,j,k,l,cases,max,min;
 cin>>t;
 for(cases=1;cases<=t;cases++)
 {
   cin>>n>>m;
   max=0,min=100;
   for(i=0;i<n;i++)
   { 
     for(j=0;j<m;j++)
     {
        cin>>arr[i][j];
     }
   }
   bool rowflag=true;
   for(i=0;i<n && rowflag;i++)
   { 
     for(j=0;j<m &&rowflag;j++)
     {
        for(k=0;k<m;k++)
        {//chk row
           if(arr[i][k]> arr[i][j])
              break;
        }
        if(k==m)
         continue;
        for(k=0;k<n;k++)
        {//chk col
           if(arr[k][j]> arr[i][j])
              break;
        }
        if(k==n)
         continue;
        else
         rowflag=false;
     }  
   }
   if(rowflag)
     cout<<"Case #"<<cases<<": YES\n";
   else
     cout<<"Case #"<<cases<<": NO\n";
}
return 0;
}