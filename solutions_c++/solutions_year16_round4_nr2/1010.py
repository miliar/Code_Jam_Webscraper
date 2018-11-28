#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

int T, K, N;
double maxi;
double DP[205][105];
double A[205];
vector<double> V;

double calc(int pos, int taken) {
    if (pos == K - 1) {
        if (taken == K / 2) return (1 - V[pos]);
        return V[pos];
    }
    if (DP[pos][taken] >= 0) return DP[pos][taken];
    double ret = 0;
    if (taken < K / 2) // Can Take
        ret += V[pos] * calc(pos + 1, taken + 1);
    if (K / 2 - taken < K - pos) // Can Don't Take
        ret += (1 - V[pos]) * calc(pos + 1, taken);
    return DP[pos][taken] = ret;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> T;
    for (int TC = 1; TC <= T; ++TC) {
        cin >> N >> K;
        maxi = 0;
        for (int a = 0; a < N; ++a) {
            cin >> A[a];
        }
        for (int a = 1; a < (1 << N); ++a) {
            if (__builtin_popcount(a) != K) continue;
            V.clear();
            for (int b = 0; b < N; ++b)
                if (a & (1 << b)) V.push_back(A[b]);
            for (int b = 0; b < 205; ++b) for (int c = 0; c < 105; ++c)
                DP[b][c] = -1e9;
            maxi = max(maxi, calc(0, 0));
        }
        cout << fixed << setprecision(9);
        cout << "Case #" << TC << ": " << maxi << "\n";
    }
    return 0;
}
