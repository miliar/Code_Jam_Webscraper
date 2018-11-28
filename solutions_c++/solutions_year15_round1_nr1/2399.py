#include<stdio.h>
#include<stdlib.h>

int main(void)
{
    FILE *in=fopen("A-large.in","r"),*out=fopen("A-large.txt","w");
    int T;
    fscanf(in,"%d",&T);
    for(int t=0;t<T;t++)
    {
        int n;
        fscanf(in,"%d",&n);
        int m[n];
        for(int i=0;i<n;i++)
        {
            fscanf(in,"%d",&m[i]);
        }
        int m1=0,m2=0,r=0;
        for(int k=1;k<n;k++)
        {
            if(m[k]<m[k-1])
            {
                m1+=(m[k-1]-m[k]);
            }
        }
        for(int k=1;k<n;k++)
        {
            if(m[k-1]-m[k]>=r)
            {
                r=(m[k-1]-m[k]);
            }
        }
        for(int k=0;k<n-1;k++)
        {
            if(m[k]<r)
            {
                m2+=m[k];
            }
            else
            {
                m2+=r;
            }
        }
        fprintf(out,"Case #%d: %d %d\n",t+1,m1,m2);
    }
}
