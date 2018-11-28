//Palindrome GCJ
#include<iostream>
#include<stdio.h>
using namespace std;
inline int palindrome(int n)
{
    int a,b=0,num;
 num=n;
 while(n!=0)
 {
  a=n%10;
  b=a+(b*10);
  n=n/10;
 }
 if(num==b)
    return 1;
 else
    return 0;
}
int main()
{
int t,i,n,a,b,j;
int count=0;
scanf("%d",&t);
for(int k=1;k<=t;k++)
{
    count=0;
    cin>>a>>b;
    for(i=1;i<=b;i++)
    {
        if((palindrome(i)!=0))
        {
                   n=i*i;
                   if(((n)<=b)&&((n)>=a))
                   {
                   if((palindrome(n)!=0))
                   count++;
                   }
        }
    }
    cout<<"Case #"<<k<<": "<<count<<endl;
}
system("PAUSE");
return 0;
}
    
