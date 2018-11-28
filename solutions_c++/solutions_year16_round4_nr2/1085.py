#include <bits/stdc++.h>

using namespace std;

#define all(x) (x).begin(), (x).end()
#define allr(x) (x).rbegin(), (x).rend()

typedef pair<int, int> PII;
typedef pair<int, char> PIC;
typedef long long LL;
typedef long double LD;

LD P[205], dp[205][205][102];

bool on(int mask, int bit) {
    return ((mask >> bit) & 1);
}

int main() {
    int T, N, K, H;
    dp[0][0][0] = 1.0;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        printf("Case #%d: ", t);
        cin >> N >> K;
        H = K / 2;
        LD sol = 0.0;
        for (int i = 0; i < N; ++i) {
            cin >> P[i];
        }
        for (int i = 0; i < (1 << N); ++i) {
            if (__builtin_popcount(i) != K) continue;
            LD tmp = 0.0;
            for (int j = i; j > 0; j = i & (j - 1)) {
                if (__builtin_popcount(j) != H) continue;
                LD cur = 1;
                for (int k = 0; k < N; ++k) {
                    if (on(j, k)) cur *= (1 - P[k]);
                    else if (on(i, k)) cur *= (P[k]);
                }
                tmp += cur;
            }
            sol = max(sol, tmp);
        }
        cout << fixed << setprecision(10) << sol << "\n";
    }
    return 0;
}