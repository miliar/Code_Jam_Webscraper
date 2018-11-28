#include <bits/stdc++.h>

using namespace std;

const int N = 205;

long double prob[N][N][N];
int n, K;
long double p[N];

long double solve(int sr) {
    vector<long double> nowi;
    for (int i = 1; i <= sr; i++) {
        nowi.push_back(p[i]);
    }
    for (int i = n - (K - sr) + 1; i <= n; i++) {
        nowi.push_back(p[i]);
    }
    prob[0][0][0] = 1.0L;

    for (int i = 1; i <= K; i++) {
        for (int j = 0; j <= K; j++) {
            if (j == 0) {
                prob[i][j][0] = 1.0L;
                continue;
            }
            for (int k = 0; k <= K; k++) {
                if (k == 0) {
                    prob[i][j][k] = prob[i - 1][j - 1][k] * (1.0L - nowi[i - 1]);
                    continue;
                }
                prob[i][j][k] = prob[i - 1][j - 1][k - 1] * nowi[i - 1] + prob[i - 1][j - 1][k] * (1.0L - nowi[i - 1]);
            }
        }
    }
    return prob[K][K][K / 2];
}

void testCase() {
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= n; j++) {
            for (int k = 0; k <= n; k++) {
                prob[i][j][k] = 0.0L;
            }
        }
    }

    scanf("%d %d", &n, &K);
//     K /= 2;
    for (int i = 1; i <= n; i++) {
        scanf("%Lf", &p[i]);
    }
    long double ans = 0;
    int poc = 1;
    int kon = K;
    sort(p + 1, p + 1 + n);
    ans = max(ans, solve(0));
    while (poc <= kon) {
        int sr = (poc + kon) / 2;
        long double r = solve(sr);
        cerr << r << endl;
        ans = max(r, ans);
        if (r > solve(sr - 1)) {
            poc = sr + 1;
        } else {
            kon = sr - 1;
        }

    }
//     cerr << ans << endl;
    printf("%.10Lf\n", ans);
}

int main() {
    srand(513315);
    int tests;
    scanf("%d", &tests);

    for (int t = 1; t <= tests; t++) {
        cerr << t << endl;
        printf("Case #%d: ", t);
        testCase();
    }

    return 0;
}