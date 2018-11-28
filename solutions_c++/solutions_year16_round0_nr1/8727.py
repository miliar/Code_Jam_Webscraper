#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int main()
    {

int t;
cin>>t;
    int j=1;
while(t--)
    {
   long long  int n;
    cin>>n;
    if(n==0)
         cout<<"Case #"<<j<<":"<<" INSOMNIA"<<endl;
    else
        {
    int arr[10];
        for(int i=0;i<10;i++)
            arr[i]=0;
    int count=0;
    int i=1;
        long long int N=n;
   while(count<10)
       {
   //    cout<<n<<endl;

      long long  int temp=n;
       while(temp>0)
           {
           int b=temp%10;
               if(arr[b]==0)
               {
               arr[b]=1;
               count++;
               }
                   if(count==10)
                       {
                       cout<<"Case #"<<j<<":"<<" "<<n<<endl;
                       break;
                   }
             temp=temp/10;
           }
        
       
        i++;
       n=N*i;
             
   }
       
    }
    j++;
}
       
         return 0;
        
}
  


