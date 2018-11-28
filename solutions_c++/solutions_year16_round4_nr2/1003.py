#include <bits/stdc++.h>

using namespace std;

constexpr int maxk = 200;

double d[maxk + 1][maxk + 1];

double get_answer(const std::vector<double> &vc) {
    int k = (int)vc.size();
    assert(k % 2 == 0);
    d[0][0] = 1;
    for (int i = 0; i < k; ++i) {
        d[i + 1][0] = d[i][0] * (1 - vc[i]);
        d[i + 1][i + 1] = d[i][i] * vc[i];
        for (int j = 1; j <= i; ++j) {
            d[i + 1][j] = d[i][j - 1] * vc[i] + d[i][j] * (1 - vc[i]);
        }
    }
    return d[k][k / 2];
}

double rec(const std::vector<double> &v, int k, int pos, std::vector<double> &acc) {
    if (k == 0) {
        return get_answer(acc);
    }
    if ((int)v.size() - pos < k) {
        return 0.;
    } else {
        double res = 0.0;
        acc.push_back(v[pos]);
        res = max(res, rec(v, k - 1, pos + 1, acc));
        acc.pop_back();
        res = max(res, rec(v, k, pos + 1, acc));
        return res;
    }
}

double solve_dummy(const std::vector<double> &vc, int k) {
    std::vector<double> acc;
    return rec(vc, k, 0, acc);
}

double solve(std::vector<double> vc, int k) {
    std::sort(vc.begin(), vc.end());
    int fpos = 0;
    int lpos = (int)vc.size() - 1;
    std::vector<double> result;
    while (k > 0 && vc[fpos] < .5 && vc[lpos] > .5) {
        result.push_back(vc[fpos++]);
        result.push_back(vc[lpos--]);
        k -=2;
    }
    while (k > 0 && vc[fpos] >= .5) {
        result.push_back(vc[fpos++]);
        --k;
    }
    while (k > 0 && vc[fpos] <= .5) {
        result.push_back(vc[lpos--]);
        --k;
    }
    return get_answer(result);
}


int main() {
    FILE *in = fopen("b.in", "r");
    FILE *out = fopen("b.out", "w");
    int t;
    fscanf(in, "%d", &t);
    for (int i = 0; i < t; ++i) {
        int n, k;
        fscanf(in, "%d%d", &n, &k);
        std::vector<double> p(n);
        for (int j = 0; j < n; ++j) {
            fscanf(in, "%lf", &p[j]);
        }
        double res1 = solve_dummy(p, k);
        double res2 = solve(p, k);
        if (std::abs(res1 - res2) > 1e-6) {
            fprintf(stderr, "different answers for test #%d: %f and %f\n", i + 1, res2, res1);
        }
        fprintf(out, "Case #%d: %.10f\n", i + 1, res1);
    }
    fclose(in);
    fclose(out);
}
