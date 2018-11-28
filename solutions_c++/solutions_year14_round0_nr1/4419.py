#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

bool use[20];

int a[10][10];

int main()
{
    freopen("A-small-attempt3.in","r",stdin);
    freopen("1.out","w",stdout);
    int i,j,k,t,T,A,B,ans,n;
    scanf("%d",&T);
    for (t=1;t<=T;t++)
    {
        scanf("%d",&A);
        for (i=1;i<=4;i++)
            for (j=1;j<=4;j++)
                scanf("%d",&a[i][j]);
        memset(use,0,sizeof(use));
        for (j=1;j<=4;j++)
            use[a[A][j]] = true;

        scanf("%d",&B);
        for (i=1;i<=4;i++)
            for (j=1;j<=4;j++)
                scanf("%d",&a[i][j]);
        n=0;
        for (j=1;j<=4;j++)
        if (use[a[B][j]])
        {
            ans=a[B][j];
            n++;
        }

        if (n==1)
            printf("Case #%d: %d\n",t,ans);
        else if (n>1)
            printf("Case #%d: Bad magician!\n",t);
        else
            printf("Case #%d: Volunteer cheated!\n",t);

    }


    return 0;
}
