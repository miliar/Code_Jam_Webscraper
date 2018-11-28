// vim:set sw=4 et smarttab:
// Qualification Round 2014

#include <cstdio>
#include <cstdint>
#include <cassert>

uint16_t input_row()
{
    uint16_t ret = 0;
    int row;
    scanf("%d", &row);
    --row;
    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j)
        {
            int t;
            scanf("%d", &t);
            if (i == row)
                ret |= (1 << --t);
        }
    return ret;
}

int main()
{
    int ntc;
    scanf("%d", &ntc);
    for (int tc = 1; tc <= ntc; ++tc)
    {
        uint16_t a = (input_row() & input_row());
        printf("Case #%d: ", tc);
        if (a == 0)
            printf("Volunteer cheated!\n");
        else
        {
            int answer;
            for (int i = 0; i < 16; ++i)
                if ((a & (1 << i)) != 0)
                {
                    answer = i;
                    break;
                }
            if (a == (1 << answer))
                printf("%d\n", answer + 1);
            else
                printf("Bad magician!\n");
        }
    }
}
