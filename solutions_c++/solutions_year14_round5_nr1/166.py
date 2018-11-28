#include <cstdio>
#include <algorithm>
using namespace std;


long long int es[1000003];

inline
long long int f(int l, int r)
{
    return es[r] - es[l - 1];
}

int main()
{
    int T;
    scanf("%d", &T);
    for(int ttt = 1; ttt <= T; ttt++)
    {
        printf("Case #%d:", ttt);

        int N, p, q, r, s;
        scanf("%d%d%d%d%d", &N, &p, &q, &r, &s);

        if(N == 1)
        {
            printf(" 0.0\n");
            continue;
        }
        for(int i = 1; i <= N; i++)
            es[i] = ((i - 1)* 1ll * p + q) % r + s + es[i - 1];
        if(N == 2)
        {
            printf(" %.10f\n", min(es[1], es[2] - es[1]) / (es[2] + 0.0));
            continue;
        }


        long long ans = 0;
        for(int i = 2; i <= N - 1; i++)
        {
            int l = i, r = N;
            while(l + 1 < r)
            {
                int m = (l + r) >> 1;
                if(f(i, m) <= f(m + 1, N))
                    l = m;
                else
                    r = m;
            }

            long long int tmp = 0;
//            printf("%d!\n", l);
            tmp = max(f(l + 1, N), max(f(1, i - 1), f(i, l)));
            if(l < N - 1)
                tmp = min(tmp, max(f(1, i - 1), max(f(i, l + 1), f(l + 2, N))));
            ans = max(ans, es[N] - tmp);
        }
        printf(" %.10f\n", ans * 1.0 / es[N]);
    }
    return 0;
}
