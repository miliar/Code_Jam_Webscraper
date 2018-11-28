#include <iostream>
#include<stdio.h>
using namespace std;

int main()
{
  long long t,n,arr[1000];
 cin>>t;
 long long x=0;
 while(t--)
 {x++;
   cin>>n;
  for(int i=0;i<n;i++)
      cin>>arr[i];
 long long sum=0,y=0,z=0,maxd=0,d=0;
  for(long long i=1;i<n;i++)
   {
      if(arr[i]<arr[i-1]){
       y+=arr[i-1]-arr[i];
       if(maxd<arr[i-1]-arr[i])
       maxd=arr[i-1]-arr[i];
       }
   }
   for(long long i=0;i<n-1;i++)
   { 
       if(arr[i]<=maxd )
       sum+=arr[i];
       else{
         sum+=maxd;
       }
   }
  cout<<"Case #"<<x<<": "<<y<<" "<<sum<<endl;
  
 }
}
  