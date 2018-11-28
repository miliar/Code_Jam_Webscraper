#include <cstdio>
int v1[20], t, n, i, j, lin, l1, l2, nr, x;
void curata()
{
    int i;
    for(i=1;i<=16;++i) v1[i]=0;
}
int main()
{
    freopen("small.in", "r", stdin);
    freopen("small.txt", "w", stdout);
    scanf("%d", &t);
    for(i=1;i<=t;++i)
    {
        curata();
        nr=0; n=0;
        scanf("%d", &l1);
        for(lin=1;lin<=4;++lin)
            for(j=1;j<=4;++j)
            {
                scanf("%d", &x);
                if(lin==l1)
                    v1[x]=1;
            }
        scanf("%d", &l2);
        for(lin=1;lin<=4;++lin)
            for(j=1;j<=4;++j)
            {
                scanf("%d", &x);
                if(lin==l2&&v1[x])
                {
                    ++nr;
                    n=x;
                }
            }
        if(nr==0)
            printf("Case #%d: Volunteer cheated!\n", i);
        else
            if(nr==1)
                printf("Case #%d: %d\n", i, n);
            else
                printf("Case #%d: Bad magician!\n",i);
    }
    return 0;
}
