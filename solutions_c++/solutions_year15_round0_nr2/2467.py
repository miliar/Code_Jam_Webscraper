#include<stdio.h>
#include<stdlib.h>

int main(void)
{
    int T;
    FILE *in=fopen("B-large.in","r"),*out=fopen("B-large.txt","w");
    fscanf(in,"%d",&T);
    for(int t=0;t<T;t++)
    {
        int D,pan[1001]={0};
        fscanf(in,"%d",&D);
        for(int i=0;i<D;i++)
        {
            int p;
            fscanf(in,"%d",&p);
            pan[p]++;
        }
        int time;
        for(time=1000;time>0;time--)
        {
            if(pan[time]!=0)
            {
                break;
            }
        }
        int max=time;
        for(int i=1;i<=max;i++)
        {
            int temp=0;
            for(int p=i+1;p<=max;p++)
            {
                if(pan[p]==0)
                {
                    continue;
                }
                int seb=pan[p]*(p/i);
                if(p%i==0)
                {
                    seb-=pan[p];
                }
                temp+=seb;
            }
            temp+=i;
            if(time>temp)
            {
                time=temp;
            }
        }
        fprintf(out,"Case #%d: %d\n",t+1,time);
    }
}
