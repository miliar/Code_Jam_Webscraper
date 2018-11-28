#include <iostream>
#include <cstdio>
#define f cin
#define g cout
#define NM 20

using namespace std;

int T;
int N, D, H, M;

int K;
int d[NM], m[NM];

int solve2 ()
{
    if (d[2] < d[1])
    {
        swap(d[1], d[2]);
        swap(m[1], m[2]);
    }

    if (d[1] == d[2])
    {
        if (m[2] < m[1])
            swap(m[1], m[2]);
        // 1 is faster
        if (1LL*(360-d[2])*m[2] < 1LL*(720-d[1])*m[1])
            return 0;
        return 1;
    }

    if (m[1] == m[2])
        return 0;

    if (m[1] > m[2]) // 1 slower
    {
        long long t1 = 1LL*(360-d[1])*m[1];
        long long t2 = 1LL*(720-d[2])*m[2];

        if (t1 < t2)
            return 0;
        else
            return 1;
    }

    // m[1] < m[2], so 1 faster
    if (1LL*(360-d[1])*m[1] >= 1LL*(360-d[2])*m[2]) // no overtake
        return 0;

    long long t1 = 1LL*(720-d[1])*m[1];
    long long t2 = 1LL*(360-d[2])*m[2];

    if (t2 < t1)
        return 0;
    return 1;
}

int main ()
{
    #ifndef ONLINE_JUDGE
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    #endif

    f >> T;
    for (int t=1; t<=T; t++)
    {
        g << "Case #" << t << ": ";

        K=0;
        f >> N;
        for (int i=1; i<=N; i++)
        {
            f >> D >> H >> M;

            for (int j=M; j<=M+H-1; j++)
            {
                ++K;
                d[K] = D;
                m[K] = j;
            }
        }

        if (K<=1)
            g << 0 << '\n';
        else
            g << solve2() << '\n';
    }

    return 0;
}


