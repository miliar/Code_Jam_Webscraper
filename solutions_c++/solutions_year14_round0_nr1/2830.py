#include <iostream>
#include <stdio.h>

using namespace std;
int v1[20], v2[20], l;

void cit()
{
    int x;
    scanf("%d", &l);
    for (int i=1; i<=4; i++)
        for (int j=1; j<=4; j++)
        {
            scanf("%d", &x);
            if (i==l)
                v1[x]++;
        }
    scanf("%d", &l);
    for (int i=1; i<=4; i++)
        for (int j=1; j<=4; j++)
        {
            scanf("%d", &x);
            if (i==l)
                v2[x]++;
        }
}

void sol()
{
    int nr=0;
    for (int i=1; i<=16; i++)
        if (v1[i]!=0 && v1[i]==v2[i])
            nr++;
    if (nr==0)
        printf("Volunteer cheated!\n");
    else if (nr>=2)
        printf("Bad magician!\n");
    else
    {
        for (int i=1; i<=16; i++)
            if (v1[i]!=0 && v1[i]==v2[i])
            {
                printf("%d\n", i);
                return;
            }
    }
}

void reset()
{
    for (int i=0; i<29; i++)
        v1[i]=v2[i]=0;
}

int main()
{
    freopen("magic.in", "r", stdin);
    freopen("magic.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int r=1; r<=T; r++) {
        cit();
        printf("Case #%d: ", r);
        sol();
        reset();
    }
    return 0;
}
