#include <stdio.h>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;


int main()
{
    //freopen("A-small-attempt0.in", "r", stdin);
    //freopen("A-small-attempt0.out", "w", stdout);

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T, N, m[10010];
    int cas = 1;
    long long ans_1 = 0, ans_2;
    scanf("%d", &T);

    while (T --)
    {
        scanf("%d", &N);
        for (int i = 0; i < N; i ++)
            scanf("%d", &m[i]);

        ans_1 = 0, ans_2 = 0;
        int max_gap = 0;

        for (int i = 0; i < N - 1; i ++)
        {
            int gap = m[i] - m[i + 1];
            if (gap <= 0)
                continue;
            ans_1 += gap;
            max_gap = gap > max_gap ? gap : max_gap;
        }

        for (int i = 0; i < N - 1; i ++)
            ans_2 += (m[i] >= max_gap ? max_gap : m[i]);

        printf("Case #%d: %lld %lld\n", cas ++, ans_1, ans_2);
    }

    return 0;
}
