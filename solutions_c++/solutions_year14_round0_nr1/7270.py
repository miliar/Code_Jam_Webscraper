#include <cstdio>
#include <cstring>
#include <set>

bool flag[17];

using namespace std;

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);

    int nca;
    scanf("%d", &nca);

    for(int ii = 1; ii <= nca; ii++)
    {
        int row1;
        int row2;
        int index;
        memset(flag, 0, sizeof(flag));
        scanf("%d", &row1);

        for(int i = 1; i <= 4; i++)
        {
            for(int j = 1; j <= 4; j++)
            {
                scanf("%d", &index);

                if(i == row1)
                {
                    flag[index] = true;
                }
            }
        }

        scanf("%d", &row2);

        int ans = -1;

        for(int i = 1; i <= 4; i++)
        {
            for(int j = 1; j <= 4; j++)
            {
                scanf("%d", &index);

                if(i == row2 && flag[index])
                {
                    if(ans == -1)ans = index;
                    else ans = -2;
                }
            }
        }

        printf("Case #%d: ", ii);

        if(ans == -1)
        {
            puts("Volunteer cheated!");
        }

        else if(ans == -2)
        {
            puts("Bad magician!");
        }

        else
        {
            printf("%d\n", ans);
        }
    }

    return 0;
}