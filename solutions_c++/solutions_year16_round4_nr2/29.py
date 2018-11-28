#include <bits/stdc++.h>
#define sz(x) (int((x).size()))
#define pb push_back
#define eb emplace_back
#define all(x) (x).begin(), (x).end()
template<typename T> bool domax(T &a, T b) { return (b > a ? (a = b, true) : false); }
template<typename T> bool domin(T &a, T b) { return (b < a ? (a = b, true) : false); }
typedef long long ll;

const int maxn = 205;

int n, k, besti;
double ans;
double p[maxn], dp[maxn], dpnew[maxn];

void clear() {
    ans = 0;
}

int main() {
    int testcases; scanf("%d", &testcases);
    for (int testnum = 1; testnum <= testcases; testnum++) {
        printf("Case #%d: ", testnum);
        scanf("%d%d", &n, &k);
        for (int i = 0; i < n; i++) scanf("%lf", p+i);
        std::sort(p, p+n);
        for (int i = 0; i <= k; i++) {
            std::fill(dp, dp+maxn, 0.0);
            dp[0] = 1.0;
            for (int j = 0; j < n; j++) if (j < i || j >= n-(k-i)) {
                std::fill(dpnew, dpnew+maxn, 0.0);
                for (int k = 0; k < maxn; k++) {
                    dpnew[k+1] += dp[k] * p[j];
                    dpnew[k] += dp[k] * (1-p[j]);
                }
                for (int k = 0; k < maxn; k++) dp[k] = dpnew[k];
            }
            if (domax(ans, dp[k/2])) {
                besti = i;
            }
        }
        printf("%.8lf\n", ans);
        clear();
    }
}

