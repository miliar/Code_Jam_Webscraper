#include <stdio.h>
#include <stdlib.h>
#include<math.h>
#define FOR(i,a,b) for(i=a;i<b;i++)
#define si(x) scanf("%d", (x))
#define sl(x) scanf("%lld", (x))
#define pi(x) printf("%d", x) 
int main()
{
int i,T;
si(&T);
long long r,t;
int m,n,x;
FOR(i,0,T)
{
sl(&r);
sl(&t);
double a= t;
m=1;
n=0;
x=0;

do
{
          a -= (2*r+m+n);
          m+=2;
          n+=2;
          x++;
}while(a>0);
if(a<0)
        x--;
printf("Case #%d: %d\n",i+1,x);
}
return 0;
}
