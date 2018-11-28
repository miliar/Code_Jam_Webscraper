#include<iostream>
#include<math.h>
using namespace std;
int palin(int);
int main()
{
    int t,a,b,i,k,count=0;
    double j;
    cin>>t;
    for(k=1;k<=t;k++)
    {
    
             cin>>a>>b;
             count = 0;
             for(i=a;i<=b;i++)
             {
              
              j=sqrt(i);
              if(j*j==i && palin(i) && (palin((int)j)) )
              {
                      count++;  
              }
                   
                             
             }
              cout<<"Case #"<<k<<": "<<count<<endl; 
    }
}
int palin(int a)
{
    int n=a;
    int sum=0,rem;
 while(n>0)
 {
           rem=n%10;
           sum=sum*10+rem;
           n=n/10;
 }
 if(sum==a)
 return 1;
 else
 return 0;
}
