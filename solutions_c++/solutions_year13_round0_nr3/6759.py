#include<stdio.h>
#include<iostream>
#include<cmath>
using namespace std;
 
int pal(int);
 
int main()
{
    int t,a,b,c,count=0;
    scanf("%d",&t);
    c=t;
    while(t--)
    {
        scanf("%d",&a);
        scanf("%d",&b);   
        int m=ceil(sqrt(a)), n=floor(sqrt(b));
        //cout<<m;
        for(int i=m;i<=n;i++){
        if(pal(i))
        {
            int j=i*i;
            if(pal(j))
            count++;
        }
        
        }
        printf("Case #%d: %d\n",c-t,count);
        count=0;
    }
 return 0;   
}
 
int pal(int n)
{
    int temp,p,sum=0;
    p=n;
    while(temp=p%10)
    {
        p/=10;
        sum=sum*10+temp;        
    }
   if(n==sum)
   return 1;
   else
   return 0;
    
}