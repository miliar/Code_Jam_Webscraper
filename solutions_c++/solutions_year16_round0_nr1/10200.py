#include<cstdio>
#include<cstring>

using namespace std;

int main()
{
    int n;
    freopen("A-large.in", "r", stdin);
    freopen("output.out", "w", stdout);
    scanf("%d", &n);
    for (int lp = 1; lp <= n; lp++)
    {
        int x;
        scanf("%d", &x);
        if (x == 0)
        {
            printf("Case #%d: INSOMNIA\n", lp);
            continue;
        }
        int v[10];
        memset(v, 0, sizeof(v));
        int x1 = x;
        while (true)
        {
            int t = x1;
            while (t > 0)
            {
                v[t % 10] = 1;
                t /= 10;
            }
            int sum = 0;
            for (int i = 0; i < 10; i++) sum += v[i];
            if (sum == 10)
            {
                printf("Case #%d: %d\n", lp, x1);
                break;
            }
            x1 += x;
        }
    }
    return 0;
}

