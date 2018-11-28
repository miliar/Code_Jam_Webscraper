#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
//#include<cctype>
#include<climits>
#include<iostream>
#include<string>
#include<vector>
#include<map>
//#include<list>
#include<queue>
#include<deque>
#include<algorithm>
//#include<numeric>
#include<utility>
//#include<memory>
#include<functional>
#include<cassert>
#include<set>
#include<stack>
#include<random>

const int dx[] = {1, 0, -1, 0};
const int dy[] = {0, -1, 0, 1};
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int, int> pii;

namespace Small {
    void solve() {
        int N, K;
        cin >> N >> K;
        vector<double> P(N);
        for (int i = 0; i < N; i++)
            cin >> P[i];
        double ans = 0;
        for (int s = 0; s < 1<<N; s++) {
            if (__builtin_popcount(s) != K) continue;
            int sub = s;
            double tmp = 0;
            do {
                if (__builtin_popcount(sub) == K/2) {
                    double plus = 1;
                    for (int i = 0; i < N; i++) if ((s>>i)&1) {
                        if ((sub>>i)&1) plus *= P[i];
                        else plus *= 1-P[i];
                    }
                    tmp += plus;
                }
                sub = (sub-1) & s;
            } while (sub != s);
            ans = max(ans, tmp);
        }
        printf("%.10lf\n", ans);
    }
}

namespace Large {
    int N, K;
    double dp[222][222][222];
    double dpr[222][222][222];
    void solve() {
        cin >> N >> K;
        vector<double> P(N);
        vector<int> Pint(N);
        for (int i = 0; i < N; i++) {
            cin >> P[i];
        }
        sort(P.begin(), P.end());
        for (int i = 0; i <= K; i++) for (int j = 0; j <= K; j++) for (int k = 0; k <= K; k++) {
            dp[i][j][k] = 0;
            dpr[i][j][k] = 0;
        }
        dp[0][0][0] = 1;
        for (int i = 0; i < N; i++) {
            for (int ok = 0; ok <= i; ok++) for (int ng = 0; ng <= i-ok; ng++) {
                if (dp[i][ok][ng] > 0) {
                    dp[i+1][ok+1][ng] += P[i]*dp[i][ok][ng];
                    dp[i+1][ok][ng+1] += (1-P[i])*dp[i][ok][ng];
                }
            }
        }
        dpr[0][0][0] = 1;
        for (int i = 0; i < N; i++) {
            for (int ok = 0; ok <= i; ok++) for (int ng = 0; ng <= i-ok; ng++) {
                if (dpr[i][ok][ng] > 0) {
                    dpr[i+1][ok+1][ng] += P[N-1-i]*dpr[i][ok][ng];
                    dpr[i+1][ok][ng+1] += (1-P[N-1-i])*dpr[i][ok][ng];
                }
            }
        }
        double ans = 0;
        for (int k = 0; k <= K; k++) {
            double tmp = 0;
            for (int i = 0; i <= K/2; i++) {
                tmp += dp[k][i][k-i] * dpr[K-k][K/2-i][K/2-k+i];
            }
            ans = max(ans, tmp);
        }
        printf("%.10lf\n", ans);
    }
} // Large
int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";
        Large::solve();        
    }
    return 0;
}
