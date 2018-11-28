#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>
#include<cstdio>
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
int pal(int x)
{
    int p=0,r,s=x;
    while(x>0)
    {
        r=x%10;
        p=p*10+r;
        x=x/10;
    }
    //return p;
    if (p==s) return 1;
    else return 0;
}
int main()
{
   int i,j,k,t,l=0,a,b,p;
   FILE *fp;
   freopen("C-small-attempt0.in","r",stdin);
   FILE *fp2;
   freopen("Output.txt","w",stdout);
   t=readint();
   fori(t)
   {
       a=readint();
       b=readint();
       int count=0;
       fork(a,b+1)
       {
           p=sqrt(k);
           if (p*p==k)
           {
               //printf("Here %d pal=%d\n",k,pal(k));
               if (pal(k)==1&&pal(p)==1) count++;
           }
       }
       printf("Case #%d: %d\n",i+1,count);
   }

   return 0;
}
