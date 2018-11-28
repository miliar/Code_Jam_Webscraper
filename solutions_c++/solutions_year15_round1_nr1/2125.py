#include <cstdio>
#include <algorithm>

int main ()
{
    int T;
    int m [1000];
    scanf ("%d", &T);
    for (int j = 1; j <= T; ++ j)
    {
        int N;
        scanf ("%d", &N);
        for (int i = 0; i < N; ++ i)
        {
            scanf ("%d", &m [i]);
        }
        int ANS1 = 0;
        int ANS2 = 0;
        int rate = 0;
        for (int i = 1; i < N; ++ i)
        {
            if (m [i-1] > m [i])
            {
                ANS1 += m [i-1] - m [i];
                rate = std::max (rate, m [i-1] - m [i]);
            }
        }
        for (int i = 0; i < N-1; ++ i)
        {
            ANS2 += std::min (rate, m [i]);
        }
        printf ("Case #%d: %d %d\n", j, ANS1, ANS2);
    }
    return 0;
}

