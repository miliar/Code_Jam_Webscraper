#include<cstdio>
#include<cstdlib>
#include<stdint.h>
using namespace std;

int sqrt(long int x)
{
    long int i,s;
    for(i=0;i<x,i*i<=x;i++)
    {
        if((i*i)==x) return i;
    }
    return -1;
}

int palindr(long int x)
{
   long int n=x,d=0,*rev,i; if((x%10)==0) return 0;
    while(n) {d++;n=n/10;}
    rev=(long int *)malloc(d*sizeof(long int));
    n=x;i=0;
    while(n)
    {
        rev[i++]=n%10; n=n/10;
    }

   i=d-1; n=x;
   while(n)
   {
       if((n%10)!=rev[i--]) return 0;
       n=n/10;
   }
   return 1;

}


int main()
{
    long int tc,i,A,B,ctr,j,sqr;
    FILE *in,*out;
    in=fopen("F:\\input.txt","r");
    out=fopen("F:\\output.txt","w");
    fscanf(in,"%ld",&tc);
    for(i=0;i<tc;i++)
    {
        fscanf(in,"%ld %ld",&A,&B); ctr=0;
        for(j=A;j<=B;j++)
        {    sqr=sqrt(j);
             if(sqr!=-1)
            {
                if(palindr(j)==1 && palindr(sqrt(j))==1) ctr++;
            }

        }
        fprintf(out,"Case #%ld: %ld\n",i+1,ctr);
    }
    return 0;
}
