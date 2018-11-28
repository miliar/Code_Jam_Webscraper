#include <bits/stdc++.h>

using namespace std;

bool psort(const pair<double,double> &s1, const pair<double,double> &s2) {
    if(s1.second > s2.second) return true;
    return false;
}

int main() {
    int T, t, N;
    double V, X, ans;
    pair<double,double> src[100];
    scanf("%d", &T);
    for(t = 0; t < T; ++t) {
        ans = 999999999;
        scanf("%d %lf %lf", &N, &V, &X);
        for(int i = 0; i < N; ++i) {
            scanf("%lf %lf", &src[i].first, &src[i].second);
        }
        sort(src,src+N,psort);
        // small
        if(X > src[0].second || X < src[N-1].second) {
            printf("Case #%d: IMPOSSIBLE\n", t+1);
        } else {
            if(X == src[0].second) {
                ans = min(ans, V/src[0].first);
            }
            if(X == src[N-1].second) {
                ans = min(ans, V/src[N-1].first);
            }
            if(N > 1) {
                if(src[0].second == src[N-1].second) {
                    ans = min(ans, V/(src[0].first+src[N-1].first));
                } else {
                    double p = (X-src[N-1].second)/(src[0].second - src[N-1].second);
                    ans = min(ans, max(p*V/src[0].first,(1-p)*V/src[N-1].first));
                }
            }
            printf("Case #%d: %0.8lf\n", t+1, ans);
        }
    }
}
