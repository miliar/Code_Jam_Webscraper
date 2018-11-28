#include <algorithm>
#include <iostream>
#include <cstdio>

using namespace std;

long double P[400];

long double pre[400][400], suf[400][400];

int main()
{
    freopen("B_large.in", "r", stdin);
    freopen("B_large_out.txt", "w", stdout);

    int T;
    scanf("%d", &T);

    for(int Ti = 1; Ti <= T; Ti++)
    {
        int N, K;
        scanf("%d %d", &N, &K);

        for(int Ni = 1; Ni <= N; Ni++)
            scanf("%Lf", &P[Ni]);

        sort(P+1, P+N+1);

        for(int Ni = 0; Ni <= N; Ni++)
            pre[0][Ni] = 0, suf[N+1][Ni] = 0;
        pre[0][0] = suf[N+1][0] = 1;

        for(int Ni = 1; Ni <= N; Ni++)
            for(int Nj = 0; Nj <= N; Nj++)
            {
                pre[Ni][Nj] = 0;
                pre[Ni][Nj] += (1-P[Ni])*pre[Ni-1][Nj];
                if( Nj ) pre[Ni][Nj] += P[Ni]*pre[Ni-1][Nj-1];
            }

        for(int Ni = N; Ni >= 1; Ni--)
            for(int Nj = 0; Nj <= N; Nj++)
            {
                suf[Ni][Nj] = 0;
                suf[Ni][Nj] += (1-P[Ni])*suf[Ni+1][Nj];
                if( Nj ) suf[Ni][Nj] += P[Ni]*suf[Ni+1][Nj-1];
            }

        long double ans = 0;

        for(int Ni = 0; Ni+(N-K)+1 <= N+1; Ni++)
        {
            long double val = 0;

            for(int Ki = 0; Ki*2 <= K; Ki++)
                val += pre[Ni][Ki]*suf[Ni+(N-K)+1][K/2-Ki];

            ans = max(ans, val);
        }

        printf("Case #%d: %.9Lf\n", Ti, ans);
    }
}
