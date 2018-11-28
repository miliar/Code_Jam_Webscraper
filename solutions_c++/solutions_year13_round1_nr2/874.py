#include <stdio.h>

int min(int a, int b)
{
    if (a < b)
        return a;
    else
        return b;
}

void run(int e, int r, int n, int *v)
{
    int ori_e = e;
    bool disallow[10000];
    
    unsigned long long gain = 0;

    if (e <= r)
    {
        for(int i = 0; i < n; ++i)
            gain += v[i] * e;

        printf("%llu\n", gain);
        return;
    }

    for (int i = 0; i < n; ++i)
        disallow[i] = false;

    for (int i = 0; i < n; ++i)
    {
        bool flag = false;
        int tmpe = e;

        for (int j = i + 1; j < n; ++j)
        {
            if (tmpe >= ori_e)
                break;
            else if (v[i] <= v[j])
            {
                disallow[i] = true;
                break;
            }

            tmpe += r;
        }

        if (disallow[i] == false)
        {
            gain += v[i] * r;
            e -= r;

            for (int j = i + 1; j < n && e != 0; ++j)
                if (v[i] <= v[j])
                {
                    flag = true;
                    break;
                }
                else
                {
                    int tmp = min(e, r);
                    gain += v[i] * tmp;
                    e -= tmp;

//                    disallow[j] = true;
                }

            if (flag == false && e != 0)
            {
                gain += v[i] * e;
                e = 0;
            }

        }

//        printf("Act: %d, gain: %d, energy: %d\n", i, gain, e);

        // Next activity
        e += r;
    }

    printf("%llu\n", gain);
}

int main()
{
    int num_case;
    int e, r, n;
    int v[10000];

    scanf("%d", &num_case);

    for (int i = 1; i <= num_case; ++i)
    {
        scanf("%d %d %d", &e, &r, &n);

        for (int j = 0; j < n; ++j)
            scanf("%d", &v[j]);

        printf("Case #%d: ", i);
        run(e, r, n, v);
    }

    return 0;
}
