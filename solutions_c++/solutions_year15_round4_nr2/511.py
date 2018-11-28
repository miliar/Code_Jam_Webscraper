#include <algorithm>
#include <cstdio>
using namespace std;

typedef long long LL;
const int MAXN = 100;

int N;
LL V, X;
LL R[MAXN], C[MAXN];

void solve()
{
    double answer = 1e100;

    for (int i = 0; i < N; ++i)
        if (C[i] == X)
            answer = min(answer, (V * 1.0) / R[i]);

    for (int i = 0; i < N; ++i)
        for (int j = i + 1; j < N; ++j) {
            if (C[i] == C[j]) {
                if (C[i] == X)
                    answer = min(answer, (V * 1.0) / (R[i] + R[j]));
                continue;
            }

            if (X > C[i] && C[j] < C[i]) continue;
            if (X < C[i] && C[j] > C[i]) continue;
            if (X > C[j] && C[i] < C[j]) continue;
            if (X < C[j] && C[i] > C[j]) continue;

            double T1 = (V * 1.0 * (X - C[j])) / ((C[i] - C[j]) * R[i]);
            double T2 = (V * 1.0 * (X - C[i])) / ((C[j] - C[i]) * R[j]);

            answer = min(answer, max(T1, T2));
        }

    if (answer < 1e99)
        printf("%.10lf\n", answer);
    else
        printf("IMPOSSIBLE\n");
}

int main()
{
    int T; scanf("%d", &T);
    for (int t = 0; t < T; ++t) {
        double Vt, Xt;
        scanf("%d%lf%lf", &N, &Vt, &Xt);
        V = (LL)(Vt * 1e4 + 0.5);
        X = (LL)(Xt * 1e4 + 0.5);

        for (int i = 0; i < N; ++i) {
            double Rt, Ct;
            scanf("%lf%lf", &Rt, &Ct);
            R[i] = (LL)(Rt * 1e4 + 0.5);
            C[i] = (LL)(Ct * 1e4 + 0.5);
        }

        printf("Case #%d: ", t + 1);
        solve();
    }

    return 0;
}
