#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>
#define fori(a) for(i=0;i<a;i++)
#define forj(a) for(j=0;j<a;j++)
#define fork(a,b) for(k=a;k<b;k++)
int readint(){
int t=0; char c;
c=getchar();
while(c<'0' || c>'9')
c=getchar();
while(c>='0' && c<='9')
{t=(t<<3)+(t<<1)+c-'0'; c=getchar();}
return t;
}
int main()
{
   int i,j,k,q,t,r,x,p,sum,count;
   freopen("A-small-attempt0.in","r",stdin);
   freopen("Outputone.txt","w",stdout);
   q=readint();
   fori(q)
   {
       r=readint();
       t=readint();
       x=1;
       sum=0;
       count=0;
       p=2*r;
       while(1)
       {
           sum+=(p+((x*x-(x-1)*(x-1))));
           if (sum<=t) {count++;x+=2;}
           else break;
       }
       printf("Case #%d: %d\n",i+1,count);
   }

   return 0;
}
