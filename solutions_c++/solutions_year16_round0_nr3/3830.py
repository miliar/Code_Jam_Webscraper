#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <iostream>
using namespace std;

long long isPrime(long long num) {
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
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int n=0,jj=0,t=0,tt=1;

    long long now =0;
    long long div[10];
    int seq[35];
    scanf("%d",&t);

    while (t--)
    {
        scanf("%d %d",&n,&jj);
        int i=0,j=0,k=0;
        bool f=true;
        printf("Case #%d:\n",tt++);
        for (i=0;i<(1<<(n-2));i++)
        {
             now = (1<<(n-2));
             now |= i;
             now <<= 1;
             now |= 1;

            div[1]=isPrime(now);

            if (div[1]<0) continue;

            for (j=0;j<n;j++)
            {
                seq[n-j-1]=(now&1);
                now>>=1;
            }        
            f=true;

            for (j=3;j<=10;j++)
            {
                now = 0;
                for (k=0;k<n;k++)
                {
                    now*=j;
                    now+=seq[k];
                }

                div[j-1]=isPrime(now);

                if (div[j-1]<0)
                {
                    f=false;
                    break;
                }
            }
            if (f==false) continue;
            jj--;
            for (j=0;j<n;j++)
                printf("%d",seq[j]);
            for (j=1;j<10;j++)
                printf(" %I64d",div[j]);
            printf("\n");
            if (jj==0) break;
        }
    }
}