#include<stdio.h>
#include<stdlib.h>

int main(void)
{
    int T,x[100],r[100],c[100];
    FILE *in=fopen("D-small-attempt0.in","r"),*out=fopen("D-small-attempt0.txt","w");
    fscanf(in,"%d",&T);
    for(int t=0;t<T;t++)
    {
        fscanf(in,"%d%d%d",&x[t],&r[t],&c[t]);
    }
    for(int t=0;t<T;t++)
    {
        if((r[t]*c[t])%x[t]==0)
        {
            if(x[t]==1||x[t]==2)
            {
                fprintf(out,"Case #%d: GABRIEL\n",t+1);
                continue;
            }
            if(x[t]==3&&r[t]>=2&&c[t]>=2)
            {
                fprintf(out,"Case #%d: GABRIEL\n",t+1);
                continue;
            }
            if(x[t]==4&&r[t]>=3&&c[t]>=3)
            {
                fprintf(out,"Case #%d: GABRIEL\n",t+1);
                continue;
            }
            if(x[t]==5&&r[t]>=4&&c[t]>=4)
            {
                fprintf(out,"Case #%d: GABRIEL\n",t+1);
                continue;
            }
            if(x[t]==6&&r[t]>=4&&c[t]>=4)
            {
                fprintf(out,"Case #%d: GABRIEL\n",t+1);
                continue;
            }
        }
        fprintf(out,"Case #%d: RICHARD\n",t+1);
    }
}
