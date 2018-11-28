#include <iostream>
#include<string.h>
#include<vector>
using namespace std;

 
int main() {
   int t,n,i,j,k,a[101][51],b[50][50];
   
   cin>>t;j=0;
   while(t--)
   {j++;
       cin>>n;
       int  c[2501];
        for(i=0;i<2500;i++)
        c[i]=0;
       
       for(i=0;i<2*n-1;i++)
       for(k=0;k<n;k++)
      { cin>>a[i][k];
        c[a[i][k]]+=1;
      }
      
       cout<<"Case #"<<j<<": ";
      for(i=1;i<=2500;i++)
      {
          if(c[i]%2!=0)
          cout<<i<<" ";
      }
       
       cout<<"\n";
      
   }
}

