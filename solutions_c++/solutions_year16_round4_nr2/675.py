#include <bits/stdc++.h>
using namespace std;

const int MAXN = 18;
int N, K;
double P[MAXN];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout << setprecision(12) << fixed;
    int kases; cin >> kases;
    for (int kase=1; kase<=kases; kase++) {
        cout << "Case #" << kase << ": ";
        cin >> N >> K;
        for (int i=0; i<N; i++) {
            cin >> P[i];
        }
        double ans = 0;
        for (int i=0; i<(1 << N); i++) {
            if (__builtin_popcount(i) == K) {
                double cur = 0;
                for (int j=i; j>0; j=(j-1)&i) {
                    if (__builtin_popcount(j) == K/2) {
                        double ccur = 1;
                        for (int k=0; k<N; k++) {
                            if (j&(1 << k)) {
                                ccur *= P[k];
                            } else if (i&(1 << k)) {
                                ccur *= (1-P[k]);
                            }
                        }
                        cur += ccur;
                    }
                }
                ans = max(ans, cur);
            }
        }
        cout << ans << '\n';
    }
    return 0;
}
