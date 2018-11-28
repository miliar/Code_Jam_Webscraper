#include <stdio.h>
#include <iostream>
using namespace std;

int T, k;
int f[20];

int main()
{

    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int a;

    scanf("%d", &T);

    for (int q = 1;q <= T;++q)
    {
        for (int i = 1;i <= 16;++i)
            f[i] = 0;
        scanf("%d", &k);
        for (int i = 1;i <= (k-1)*4;++i) scanf("%*d");
        for (int i = 1;i <= 4;++i)
        {
            scanf("%d", &a);
            f[a]++;
        }
        for (int i = 1;i <= (4-k)*4;++i) scanf("%*d");

        scanf("%d", &k);
        for (int i = 1;i <= (k-1)*4;++i) scanf("%*d");
        for (int i = 1;i <= 4;++i)
        {
            scanf("%d", &a);
            f[a]++;
        }
        for (int i = 1;i <= (4-k)*4;++i) scanf("%*d");

        a = 0;
        for (int i = 1;i <= 16;++i)
            if (f[i] == 2)
            {
                k = i;
                a++;
            }
        printf("Case #%d: ", q);
        if (a == 1)
        {
            printf("%d\n", k);
        }
        else if (a > 1) printf("Bad magician!\n");
            else printf("Volunteer cheated!\n");
    }
}
