#include <stdio.h>
#include <string.h>

int main(void)
{
    int TC, T,j,n, tmp, tmp1;

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);


    scanf("%d", &TC);

    for (T = 1; T <= TC; T++)
    {
        int nTps = 0;
        int nTF = 0;

        printf("Case #%d: ", T);
        scanf("%d", &n);
        scanf("%1d", &tmp);

        nTps += tmp;
        for(j=1; j <= n; j++)
        {
            tmp = 0;
            scanf("%1d", &tmp);

            if(nTps < j)
            {
                tmp1 = (j - nTps);
                tmp += tmp1;
                nTF += tmp1 ;
            }

            nTps += tmp;
        }
        printf("%d\n", nTF);

    }
    return 0;
}

