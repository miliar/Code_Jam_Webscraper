#include<iostream>
#include<stdio.h>
using namespace std;
long long unsigned int a[10000001],n=10000000,b[10000001];
long long unsigned int ispalin(long long unsigned int x)
{
     long long unsigned int y=0,temp=x;
     while(temp){y=(y*10)+(temp%10);temp/=10;}
     if(y==x) return 1;
     return 0;
     }
int main()
{
    for(int i=1;i<=n;i++)
    a[i]=i*i;
    for(int i=1;i<=n;i++)
    {
            if(ispalin(i)==1 && ispalin (a[i])==1  )
            b[i]=1;
            else b[i]=0;
            }
    long long unsigned int test,number1,number2;
    cin>>test;int cases = 1;
    while(test--)
    {
               scanf("%llu %llu",&number1,&number2);//cin>>number1>>number2;
               int ans=0;
               int i=1;
               for(;i<=1000;i++)
               if(a[i]>=number1) break;
               for(;a[i]<=number2;i++)
             {
                       ans+=b[i];
                       }    
                       printf("Case #%d: %d\n",cases,ans);
                 cases++;
                 }
    return 0;
}
 
