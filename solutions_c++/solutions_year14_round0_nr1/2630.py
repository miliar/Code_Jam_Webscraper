#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;
int N;
int vu[20];

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);

    int T;
    scanf("%d", &T);

    for(int t = 1; t <= T; t++)
    {
        int repA;
        scanf("%d", &repA);

        for(int j = 1; j <= 4; j++)
        {
            for(int i = 0; i < 4; i++)
            {
                int nb;
                scanf("%d", &nb);

                if(repA==j)
                    vu[nb]=1;
                else
                    vu[nb]=0;
            }
        }

        int repB;
        scanf("%d", &repB);

        for(int j = 1; j <= 4; j++)
        {
            for(int i = 0; i < 4; i++)
            {
                int nb;
                scanf("%d", &nb);

                if(repB==j)
                    vu[nb]++;
            }
        }

        int res = -1;
        printf("Case #%d: ", t);

        for(int i = 1; i <= 16; i++)
        {
            if(vu[i] == 2 && res != -1)
            {
                printf("Bad magician!\n");
                goto end;
            }
            if(vu[i]==2)
                res=i;
        }

        if(res==-1)
            printf("Volunteer cheated!\n");
        else
            printf("%d\n", res);

        end:;
    }

    return 0;
}
