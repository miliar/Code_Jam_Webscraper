#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <tuple>
#include <map>
#include <set>

#include <gmpxx.h>
#include <QtGlobal>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;
typedef unsigned long ul;

#define MAXINT 0x7FFFFFFF

int main() {
    int T, N, K;
    cin >> T;
    vector<double> P;
    double v;
    double left[201][201], right[201][201];
    left[0][0] = 1;
    right[0][0] = 1;
    for (int i = 0; i < T;) {
        cin >> N >> K;
        P.clear();
        P.reserve(N);
        for (int j = 0; j < N; ++j) {
            cin >> v;
            P.push_back(v);
        }
        sort(P.begin(), P.end());
        for (int j = 1; j <= K; ++j) {
            left[0][j] = (1 - P[j - 1]) * left[0][j - 1];
            right[0][j] = (1 - P[N - j]) * right[0][j - 1];
            for (int k = 1; k <= j; ++k) {
                left[k][j] = P[j - 1] * left[k - 1][j - 1] + (1 - P[j - 1]) * left[k][j - 1];
                right[k][j] = P[N - j] * right[k - 1][j - 1] + (1 - P[N - j]) * right[k][j - 1];
            }
        }
        double best = 0;
        int goal = K >> 1;
        for (int j = 0; j <= K; ++j) {
            double c = 0;
            for (int k = 0; k <= j; ++k) {
                if (k > goal) break;
                c += left[k][j] * right[goal - k][K - j];
            }
            if (c > best) best = c;
        }
        cout << "Case #" << (++i) << ": " << best << endl;
    }
    return 0;
}
