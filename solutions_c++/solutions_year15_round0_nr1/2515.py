#include<stdio.h>
#include<stdlib.h>

int main(void)
{
    int T;
    FILE *in=fopen("A-large.in","r"),*out=fopen("A-large.txt","w");
    fscanf(in,"%d",&T);
    int max[T];
    char str[T][1001];
    for(int t=0;t<T;t++)
    {
        fscanf(in," %d",&max[t]);
        for(int i=0;i<=max[t];i++)
        {
            fscanf(in," %c",&str[t][i]);
        }
    }
    for(int t=0;t<T;t++)
    {
        int n=0,add=0;
        for(int i=0;i<max[t];i++)
        {
            n+=(str[t][i]-48);
            if(n<i+1)
            {
                add++;
                n++;
            }
        }
        if(n<0)
        {
            n=0;
        }
        fprintf(out,"Case #%d: %d\n",t+1,add);
    }
}
