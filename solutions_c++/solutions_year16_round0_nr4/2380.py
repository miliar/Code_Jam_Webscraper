#include <cstdio>

using namespace std;

int main(int argc, char *argv[])
{
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++)
    {
        unsigned long long k, c, s;
        scanf("%llu %llu %llu", &k, &c, &s);
        printf("Case #%d:", i + 1);

        if (k == 1)
        {
            printf(" 1\n");
            continue;
        }

        unsigned long long ch[100] = {0};
        int chl = 0;
        unsigned long long cur = 1;
        while (cur <= k)
        {
            ch[chl] = cur;
            for (int d = 1; d < c; d++)
            {
                cur++;
                ch[chl] = (ch[chl] - 1)*k + (cur <= k ? cur : 1);
            }
            cur++;
            chl++;
        }

        if (chl > s)
            printf(" IMPOSSIBLE\n");
        else
        {
            for (int i = 0; i < chl; i++)
                printf(" %llu", ch[i]);
            printf("\n");
        }
    }
    return 0;
}
