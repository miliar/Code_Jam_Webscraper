#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iomanip>

using namespace std;

unsigned power(int b, int e) {
    if(e == 0) return 1;
    return b * power(b, e - 1);
}

double rec(const vector<double> &ps, vector<vector<double> > &DP, int n, int k) {
    if(k > n) return 0.0;
    if(n == 1 && k == 1) return ps[n];
    if(n == 1 && k == 0) return 1.0 - ps[n];
    if(DP[n][k] >= 0) return DP[n][k];
    DP[n][k] = rec(ps, DP, n - 1, k) * (1 - ps[n]) + rec(ps, DP, n - 1, k - 1) * ps[n];
    return DP[n][k];
}

bool eq(unsigned s, int K) {
    while(s > 0) {
        K -= s & 1;
        s >>= 1;
    }
    return K == 0;
}

void bin(int s, int N) {
    for(int i = 0; i < N; i++) {
        s & 1 ? cout << '1' : cout << '0';
        s >>= 1;
    }
}

int main()
{
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";
        int N, K;
        cin >> N >> K;
        vector<double> ps(N);
        for(int i = 0; i < N; i++) {
            cin >> ps[i];
        }
        double best = 0.0, check = 0.0;
        int best_s = 0;
        sort(ps.begin(), ps.end());
        for(int k = 0; k <= K; k++) {
            vector<double> sps(1, -1);
            for(int i = 0; i < k; i++) sps.push_back(ps[i]);
            for(int i = N - (K - k); i < N; i++) sps.push_back(ps[i]);
            vector<vector<double> > DP(K + 1, vector<double>(K / 2 + 1, -1));
            double v = rec(sps, DP, K, K / 2);
            check = max(check, v);
        }
        cout << fixed << setprecision(10) << check << endl;
    }
    return 0;
}
