#include <algorithm>
#include <cstdio>
#include <string>
using namespace std;

const int MAXN = 300;

double p[MAXN];
double q[MAXN], d[MAXN];

double calc(int K)
{
    fill(d, d + MAXN, 0.0);
    d[0] = 1;
    for (int t = 1; t <= K; ++t) {
        for (int i = t; i >= 0; --i) {
            d[i] = d[i] * (1 - q[t - 1]);
            if (i > 0)
                d[i] += d[i - 1] * q[t - 1];
        }
    }
    return d[K / 2];
}

int main()
{
    int T; scanf("%d", &T);
    for (int t = 0; t < T; ++t) {
        int N, K; scanf("%d%d", &N, &K);
        for (int i = 0; i < N; ++i)
            scanf("%lf", &p[i]);

        sort(p, p + N);

        double res = -1.0;
        for (int L = 0; L <= K; ++L) {
            for (int i = 0; i < L; ++i)
                q[i] = p[i];
            for (int i = 0; i < K - L; ++i)
                q[K - i - 1] = p[N - i - 1];
            res = max(res, calc(K));
        }

        printf("Case #%d: ", t + 1);
        printf("%.10lf\n", res);
    }

    return 0;
}
