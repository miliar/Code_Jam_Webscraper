#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <cstdio>

using namespace std;


int N;
int A[1000];
int L[1000], R[1000];

void solve() {
    cin >> N;
    for (int i = 0; i < N; i++)
        cin >> A[i];
    memset(L, 0, sizeof(L));
    memset(R, 0, sizeof(R));

    for (int i = 0; i < N; i++)
        for (int j = i + 1; j < N; j++)
            if (A[i] < A[j]) {
                R[i]++;
            } else {
                L[j]++;
            }

    int ans = 0;
    for (int i = 0; i < N; i++) {
        ans += min(L[i], R[i]);
    }
    cout << ans << endl;
}

int main() {
    int T;
    cin >> T;
    for (int testcase = 1; testcase <= T; testcase++) {
        cout << "Case #" << testcase << ": ";
        solve();
    }

    return 0;
}
