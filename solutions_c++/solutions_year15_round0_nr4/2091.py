#include<stdio.h>
#include<iostream>
#include<math.h>
#include<string.h>
#include<algorithm>
typedef long long int ll;
using namespace std;
int main()
{
   FILE *op=fopen("output.in","w");
   FILE *ip=fopen("D-small-attempt0.in","rt");
ll t,t1,x,r,c;
fscanf(ip,"%lld",&t);
for(t1=1;t1<=t;t1++)
{
    fscanf(ip,"%lld %lld %lld",&x,&r,&c);
    if(x==1)
        fprintf(op,"Case #%d: GABRIEL\n",t1);
    if(x==2)
    {
      if((r%2==0)||(c%2==0))
           fprintf(op,"Case #%d: GABRIEL\n",t1);
      else
        fprintf(op,"Case #%d: RICHARD\n",t1);
    }
   if(x==3)
    {
        //fprintf(op,"hello");

              if((r*c)%3==0&&r>=2&&c>=2)
                  fprintf(op,"Case #%d: GABRIEL\n",t1);
       else
       {
            fprintf(op,"Case #%d: RICHARD\n",t1);
           // fprintf(op,"hello");
       }
    }
    if(x==4)
    {
         if((r*c)%4==0&&r>=3&&c>=3)
                   fprintf(op,"Case #%d: GABRIEL\n",t1);
       else
            fprintf(op,"Case #%d: RICHARD\n",t1);
    }
}
return 0;
}
