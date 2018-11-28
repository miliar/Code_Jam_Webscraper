#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <cstdio>

using namespace std;


int N, X;
vector<int> S;

void solve() {
    cin >> N >> X;
    S.clear();
    for (int i = 0; i < N; i++) {
        int s;
        cin >> s;
        S.push_back(s);
    }

    sort(S.begin(), S.end());
    int p = 0;
    int q = N - 1;
    int ans = 0;
    while (p < q) {
        if (S[q] + S[p] > X) {
            q--;
            ans++;
        } else {
            q--;
            p++;
            ans++;
        }
    }
    if (p == q)
        ans++;

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

