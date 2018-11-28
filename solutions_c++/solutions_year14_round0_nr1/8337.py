#include <cstdlib>
#include <cstdio>
#include <memory.h>

#define NUM 16

int main()
{
    int t;
    scanf("%d", &t);
    for (int idx = 0; idx < t; ++idx)
    {
        int map[NUM + 1];
        memset(map, 0, sizeof(int) * (NUM + 1));
        for (int count = 0; count < 2; ++count)
        {
            int row;
            scanf("%d", &row);
            for (int i = 0; i < NUM; ++i)
            {
                int tmp;
                scanf("%d", &tmp);
                if (i / 4 == row - 1)
                {
                    map[tmp]++;
                }
            }
        }
        int result = -1;
        for (int i = 1; i < NUM + 1; ++i)
        {
            if (map[i] == 2 && result == -1)
            {
                result = i;
            }
            else if (map[i] == 2 && result > 0)
            {
                result = 0;
            }
        }
        if (result > 0)
        {
            printf("Case #%d: %d\n", idx + 1, result);
        }
        else if (result == 0)
        {
            printf("Case #%d: Bad magician!\n", idx + 1);
        }
        else
        {
            printf("Case #%d: Volunteer cheated!\n", idx + 1);
        }
    }
    return 0;
}
