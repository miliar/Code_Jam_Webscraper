#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

const int MaxN = 20;

int t,n,m,tot,a[MaxN];

void Check()
{
    int i,pt[11]; long long j,d;
    for (i=2; i<=10; i++)
    {
        for (j=1,d=0; j<=n; j++)
            d = d*i+a[j];
        for (j=2; j*j<=d; j++)
            if(d%j==0)
            {
                pt[i] = j;
                break;
            }
        if(j*j>d) return;
    }
    for (i=1; i<=n; i++) printf("%d",a[i]);
    tot++;
    for (i=2; i<=10; i++)
        printf(" %d",pt[i]);
    printf("\n");
}

int main()
{
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    scanf("%d",&t);
    scanf("%d%d",&n,&m);
    printf("Case #1:\n");
    a[1] = a[n] = 1; tot=0;
    int i,j;
    while(tot<m)
    {
        for (i=2; i<n; i++)
            if(a[i] == 0) break;
        if(i==n) break;
        for (j=2; j<i; j++) a[j] = 0;
        a[i] = 1;
        Check();
    }
    return 0;
}
