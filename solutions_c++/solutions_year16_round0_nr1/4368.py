#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);

    int cnt_cases;
    scanf("%d", &cnt_cases);
    for (int current_case = 1; current_case <= cnt_cases; current_case++)
    {
        int seed;
        scanf("%d", &seed);

        if (seed == 0)
        {
            printf("Case #%d: INSOMNIA\n", current_case);
            continue;
        }

        int digit_cnt = 0;
        int digits[10] = { 0 };
        int repeat_times = 0;

        do
        {
            repeat_times++;
            int dummy = seed * repeat_times;
            while (dummy)
            {
                if (digits[ dummy % 10 ] == 0)
                    digit_cnt++;
                digits[ dummy % 10 ] = 1;
                dummy /= 10;
            }
        } while (digit_cnt != 10);

        printf("Case #%d: %d\n", current_case, seed * repeat_times);
    }
    return 0;
}
