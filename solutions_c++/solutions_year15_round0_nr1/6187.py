#include<iostream>
#include<stdio.h>
using namespace std;
string a;
int main()
{
   long long int t,k,n,i,diff,sum;
   scanf("%lld",&t);
   k=1;
   while(t--)
   {
       scanf("%lld",&n);
       cin>>a;          
       sum=0;
       diff=0;
       for(i=1;i<=n;i++)
       {
          sum+=(a[i-1]-48);                 
          if(sum<i && (a[i]-48))
          {
              diff+=(i-sum);
              sum=i;         
          }  
       }
       printf("Case #%lld: %lld\n",k,diff);
       k++;
   }
   return 0;
}
