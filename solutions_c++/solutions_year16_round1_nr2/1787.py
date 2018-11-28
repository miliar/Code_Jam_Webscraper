#include <iostream>
using namespace std;

int main()
{int t;
int a,b,c,n;
   cin>>t;
   int i;int k;
   int j;int temp;
   for(j=1;j<=t;j++)
   
   {
       int arr[10009];
       for(i=0;i<10009;i++)
       arr[i]=0;
       
       cin>>n;
       for(i=0;i<2*n-1;i++)
       {
           
           for(k=0;k<n;k++)
           {cin>>temp;
           arr[temp]++;
           }
         
       } cout<<"Case #"<<j<<":"<< " ";
       for(i=1;i<10007;i++)
       {
           if(arr[i]%2!=0)
           cout<<i<<" ";
       }
       cout<<"\n";
       
       
   
       
       
   }
   
   
   
   
   
   
   
   
    return 0;
}
