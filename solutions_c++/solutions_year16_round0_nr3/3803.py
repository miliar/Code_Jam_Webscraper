#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <iostream>
using namespace std;

long long isprime(long long num) {

    if (num <= 1) return 0;

    long long i;

    if (num == 2) return -1;

    if (num%2==0) return 2;

    for (i=3; i*i<=num; i+=2)
    {
        if (num%i==0) return i;
    }

    return -1;
}

int main()
{
    FILE* fin=fopen("c.in","r");
    FILE* fout=fopen("c.out","w");
    int n=0,jj=0,t=0,tt=1;

    long long now =0;
    long long div[10];
    int seq[35];
    fscanf(fin,"%d",&t);

    while (t--)
    {
        fscanf(fin,"%d %d",&n,&jj);

        int i=0,j=0,k=0;
        bool f=true;

        fprintf(fout,"Case #%d:\n",tt++);

        for (i=0;i<(1<<(n-2));i++)
        {
             now = (1<<(n-2));
             now |= i;
             now <<= 1;
             now |= 1;

            div[1]=isprime(now);

            if (div[1]<0) continue;

            for (j=0;j<n;j++)
            {
                seq[n-j-1]=(now&1);
                now>>=1;
            }

            //for (j=0;j<n;j++)
            //    printf("%d",seq[j]);
           // printf("\n");

            f=true;

            for (j=3;j<=10;j++)
            {
                now = 0;
                for (k=0;k<n;k++)
                {
                    now*=j;
                    now+=seq[k];
                }

                div[j-1]=isprime(now);

                if (div[j-1]<0)
                {
                    f=false;
                    break;
                }

            }

            if (f==false) continue;

            jj--;

            for (j=0;j<n;j++)
                fprintf(fout,"%d",seq[j]);

            for (j=1;j<10;j++)
                fprintf(fout," %I64d",div[j]);

            fprintf(fout,"\n");

            if (jj==0) break;
        }

    }


    return 0;
}
