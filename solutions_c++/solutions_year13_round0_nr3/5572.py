#include<iostream>
#include<stdio.h>
#include<math.h>
using namespace std;

int pal(int a)
{
int m,n=0;
m=a;
while(a)
{
n=(n*10)+(a%10);
a/=10;
}
if(m==n) return 1;
return 0;
}

int main()
{
int j,t,a,b,i,c;
scanf("%d",&t);
for(i=1;i<=t;i++)
{
scanf("%d%d",&a,&b);
c=0;
for(j=a;j<=b;j++)
{
if(float(sqrt(j))-sqrt(j)==0) if(pal(j)) if(pal(sqrt(j))) c++;
}
printf("Case #%d: %d\n",i,c);
}
return 0;
}
