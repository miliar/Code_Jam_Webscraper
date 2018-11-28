#include <algorithm>
#include <cstdio>
#include <vector>

double cal_prob(const std::vector<double>& p)
{
    int n = p.size();
    std::vector<double> prob(n + 1);
    prob[0] = 1.;
    for (int i = 0; i < n; ++ i) {
        for (int j = i + 1; j >= 1; -- j) {
            prob[j] = prob[j] * (1 - p[i]) + prob[j - 1] * p[i];
        }
        prob[0] *= (1 - p[i]);
    }
    return prob[n / 2];
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++ t) {
        int n, m;
        scanf("%d%d", &n, &m);
        std::vector<double> p(n);
        for (int i = 0; i < n; ++ i) {
            scanf("%lf", &p[i]);
        }
        std::sort(p.begin(), p.end());
        double result = 0.;
        for (int i = 0; i <= m; ++ i) {
            std::vector<double> np;
            for (int j = 0; j < i; ++ j) {
                np.push_back(p[j]);
            }
            for (int j = n - (m - i); j < n; ++ j) {
                np.push_back(p[j]);
            }
            result = std::max(result, cal_prob(np));
        }
        printf("Case #%d: %.10f\n", t, result);
    }
}
