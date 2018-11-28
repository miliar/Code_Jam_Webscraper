#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

int N, K;
int S[1000];
int L[1000];
int H[1000];

int solve() {
    memset(L, 0, sizeof(L));
    memset(H, 0, sizeof(H));
    for (int i = 0; i < K; i++) {
        int v = 0;
        for (int j = i; j < N - K; j += K) {
            v += S[j + 1] - S[j];
            L[i] = min(L[i], v);
            H[i] = max(H[i], v);
        }
    }

//for (int i = 0; i < K; i++) {
//    cout << L[i] << ' ' << H[i] << endl;
//}
    int offset = 0;
    for (int i = 0; i < K; i++) {
        H[i] -= L[i];
        offset -= L[i];
    }
    int rest = S[0] - offset;
    rest = (rest % K + K) % K;
//cout << rest << endl;
    int max_h = 0;
    for (int i = 0; i < K; i++) {
        if (max_h < H[i]) {
            max_h = H[i];
        }
    }
    int gap = 0;
    for (int i = 0; i < K; i++) {
        gap += max_h - H[i];
    }
    
    if (gap >= rest) {
        return max_h;
    } else {
        return max_h + 1;
    }
}

int main() {
    int T;
    cin >> T;
    for (int testcase = 1; testcase <= T; testcase++) {
        int ans = 0;
        cin >> N >> K;
        for (int i = 0; i < N - K + 1; i++) {
            cin >> S[i];
        }
        ans = solve();

        cout << "Case #" << testcase << ": ";
        cout << ans;
        cout << endl;
    }
    return 0;
}
