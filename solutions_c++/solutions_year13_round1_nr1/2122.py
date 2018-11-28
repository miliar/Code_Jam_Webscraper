#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<limits.h>

int readint()
{
    int t=0;
    char c;
    c=getchar();
    while(c<'0' || c>'9')
        c=getchar();
    while(c>='0' && c<='9')
    {
        t=(t<<3)+(t<<1)+c-'0';
        c=getchar();
    }
    return t;
}
int main()
{
    int t,s,r,k;
    FILE *fp,*fp2;
    fp=fopen("A-small-attempt0.in","r");
    fscanf(fp,"%d",&t);
    fp2=fopen("Output1.txt","w");
    int a,b,cnt;
    int sum;
    for(s=1; s<=t; s++)
    {
        fscanf(fp,"%d%d",&r,&k);
        sum=k;
        a=2*r+1;
        cnt=0;
        while(1)
        {
           if(sum<a)
           {
              break;
           }
           else
           {
               cnt++;
               sum=sum-a;
           }
            a=a+4;
        }
        fprintf(fp2,"Case #%d: ",s);
        fprintf(fp2,"%d\n",cnt);
    }
    return 0;
}
