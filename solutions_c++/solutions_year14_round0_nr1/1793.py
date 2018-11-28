#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstring>

void readRow(int* mask)
{
    int iRow;
    scanf("%d", &iRow);
    for (int i = 1; i < iRow; ++i)
    {
        int dummy;
        for (int j = 0; j < 4; ++j)
        {
            scanf("%d", &dummy);
        }
    }
    int dummy;
    for (int j = 0; j < 4; ++j)
    {
        scanf("%d", &dummy);
        ++mask[dummy - 1];
    }
    for (int i = iRow + 1; i <= 4; ++i)
    {
        int dummy;
        for (int j = 0; j < 4; ++j)
        {
            scanf("%d", &dummy);
        }
    }
}

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);

    int nTests;
    scanf("%d", &nTests);
    for (int iTest = 0; iTest < nTests; ++iTest)
    {
        int mask[16];
        memset(mask, 0, sizeof(mask));
        
        readRow(mask);
        readRow(mask);

        int count = 0;
        int res = -1;
        for (int i = 0; i < 16; ++i)
        {
            if (2 == mask[i])
            {
                ++count;
                res = i;
            }
        }

        printf("Case #%d: ", iTest + 1);
        if (0 == count)
        {
            printf("Volunteer cheated!");
        }
        else if (count > 1)
        {
            printf("Bad magician!");
        }
        else
        {
            printf("%d", res + 1);
        }
        printf("\n");
    }
    
    return 0;
}