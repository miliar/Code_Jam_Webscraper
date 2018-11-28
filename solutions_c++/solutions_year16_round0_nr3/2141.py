#include <iostream>
#include<stdio.h>
#include <stdlib.h>
using namespace std;
int t,n,j;
int m;
void afisare(int x)
{
    int k=0;
    int n=x;
    int a[11];
    int b[11];
    for(int i=1;i<=10;i++)
       {
            a[i]=0;
            b[i]=0;
       }
    while (n) {
        if (n & 1)
            {
                printf("1");
                for(int u=2;u<=10;u++)
                    b[u]=b[u]*u+1;
            }
        else
            {
                printf("0");
                for(int u=2;u<=10;u++)
                    b[u]=b[u]*u;
            }

        n >>= 1;
        k++;
    }
    for(int i=1;i<=m-k-k;i++)
        printf("0");

       n=x;
    while (n) {
        if (n & 1)
            printf("1");
        else
            printf("0");
        n >>= 1;
        k++;
    }

    for(int u=2;u<=10;u++)
        printf(" %d",b[u]);
    printf("\n");
}
int main()
{
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        scanf("%d %d",&n,&j);
        m=n;
        printf("Case #%d:\n",i);
        for(int u=3;u<=j*2+1;u+=2)
            afisare(u);
    }
    return 0;
}
