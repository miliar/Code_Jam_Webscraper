#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

const int MOD = 1000002013;

int N, M;
int o[1 << 10], e[1 << 10], p[1 << 10];

vector<int> x;
long f[1 << 11][1 << 11];

int calc2() {
    int s = x.size();
    int re = 0;
    for (int i = 0; i < s; ++i) {
        for (int j = i + 1; j < s; ++j) {
            long d = x[j] - x[i];
            d = d * N - d * (d - 1) / 2;
            d %= MOD;
            d *= f[i][j];
            d %= MOD;
            re += d;
            re %= MOD;
        }
    }
    return re;
}

void go() {
    int s = x.size();
    for (int i = s - 2; i >= 0; --i) {
        for (int j = s - 1; j > i; --j) {
            for (int k = 0; k < i; ++k) {
                for (int l = i; l < j; ++l) {
                    long g = min(f[i][j], f[k][l]);
                    f[i][j] -= g;
                    f[k][l] -= g;
                    f[i][l] += g;
                    f[k][j] += g;
                }
            }
        }
    }
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        x.clear();
        scanf("%d%d", &N, &M);
        for (int m = 0; m < M; ++m) {
            scanf("%d%d%d", o + m, e + m, p + m);
            x.push_back(o[m]);
            x.push_back(e[m]);
        }
        sort(x.begin(), x.end());
        x.erase(unique(x.begin(), x.end()), x.end());

        memset(f, 0, sizeof f);
        for (int m = 0; m < M; ++m) {
            f[lower_bound(x.begin(), x.end(), o[m]) - x.begin()]
             [lower_bound(x.begin(), x.end(), e[m]) - x.begin()] += p[m];
        }

        int a = calc2();
        go();
        int b = calc2();

        printf("Case #%d: %d\n", t, (a - b + MOD) % MOD);
    }

    return 0;
}
