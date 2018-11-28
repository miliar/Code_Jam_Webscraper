#include <stdio.h>

int main()
{
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t)
    {
        int N;
        bool digits[10];
        for (int i = 0; i < 10; ++i)
        {
            digits[i] = false;
        }

        scanf("%d", &N);

        if (N == 0)
        {
            printf("Case #%d: INSOMNIA\n", t);
            continue;
        }

        bool stop = false;
        for (int i = 1; !stop; i++)
        {
            int n = i*N;
            while (n > 0)
            {
                digits[n%10] = true;
                n /= 10;
            }

            stop = true;
            for (int j = 0; j < 10; ++j)
            {
                if (!digits[j])
                    stop = false;
            }

            if (stop)
            {
                printf("Case #%d: %d\n", t, i*N);
            }
        }
    }
    return 0;
}
