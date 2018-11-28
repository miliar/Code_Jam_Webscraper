
#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>
#define MAXN 200

using namespace std;

int N, K;
int p[MAXN];

void solve_naive() {
    double best_prob = 0;
    for (int mask = 0; mask < (1 << N); mask++) {
        if (__builtin_popcount(mask) != K)
            continue;
        vector <int> idx;
        for (int i = 0; i < N; i++)
            if (mask & (1 << i))
                idx.push_back(i);

        double prob = 0;
        for (int mask2 = 0; mask2 < (1 << K); mask2++) {
            if (__builtin_popcount(mask2) != K / 2)
                continue;
            double cur_p = 1.0;
            for (int j = 0; j < K; j++) {
                if (mask2 & (1 << j))
                    cur_p *= 0.01 * p[idx[j]];
                else
                    cur_p *= (1.0 - 0.01 * p[idx[j]]);
            }
            prob += cur_p;
        }
        if (prob > best_prob)
            best_prob = prob;
    }
    printf("%.10f\n", best_prob);
}

void solve() {
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> N >> K;
        for (int i = 0; i < N; i++) {
            double x;
            cin >> x;
            p[i] = (int) (100 * x + 0.5);
        }

        printf("Case #%d: ", t);
        solve_naive();
        //solve();
    }
}
