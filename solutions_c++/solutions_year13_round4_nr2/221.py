#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <map>
#include <queue>
#include <vector>
#include <set>

using namespace std;

long long N, P;
int b[60]; // 0 - W

bool verifyWorst(long long val) {
    long long better = val;
    for (int i = 0; i < N; ++i) {
        if (b[i] == 0)
            return better == 0;
        else {
            better = (better - 1) / 2;
        }
    }
    return true;
}

bool verifyBest(long long val) {
    long long better = val, worse = (1LL << N) - val - 1;
    //cout << "Val = " << val << endl;
    for (int i = 0; i < N; ++i) {
        // cout << "B: " << better << " W: " << worse << " i: " << i << " b[i]=" << b[i] << endl;
        assert(better + worse + 1 == (1LL << (N - i)));
        if (better == 0)
            return true;
        if (b[i] == 0) {
            if (worse == 0)
                return false;
            worse -= 1;
            // W
            if (better & 1) {
                better = (better / 2) + 1;
                worse = worse / 2;
            } else {
                better /= 2;
                worse /= 2;
            }
        } else {
            better -= 1;
            // L
            long long cp = min(better, worse);
            better = (better - cp) / 2;
            worse = cp + (worse - cp) / 2;
        }
    }
    return true;
}

void convert() {
    long long P0 = P - 1, N0 = N - 1;
    while (N0 >= 0) {
        b[N0] = P0 & 1;
        P0 /= 2;
        N0 -= 1;
    }
}

void minimizeNumWins() {
    int cnt = 0;
    for (int i = N - 1; i >= 0; --i) {
        if (b[i] == 0)
            ++cnt;
        else {
            if (cnt >= 1) {
                cnt = 1;
                b[i] = 0;
                for (int j = i + 1; j < N; ++j)
                    b[j] = 1;
            }
        }
    }
}

void solve() {
    convert();
    long long worstP = 0, bestP = 0, left = 0, right = (1LL << N) - 1;
    while (left <= right) {
        long long mid = (left + right) >> 1;
        if (verifyWorst(mid)) {
            worstP = max(worstP, mid);
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    minimizeNumWins();
    left = 0; right = (1LL << N) - 1;
    while (left <= right) {
        long long mid = (left + right) >> 1;
        if (verifyBest(mid)) {
            bestP = max(bestP, mid);
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    cout << worstP << " " << bestP;
}

int main() {
    int numCases;
    cin >> numCases;
    for (int caseNo = 1; caseNo <= numCases; ++caseNo) {
        cin >> N >> P;
        cout << "Case #" << caseNo << ": ";
        solve();
        cout << endl;
    }
    return 0;
}
