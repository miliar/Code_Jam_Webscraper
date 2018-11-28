#include <bits/stdc++.h>
using namespace std;

#define sz(x) (int(x.size()))

string S;
int K;

void solve() {
    int cnt = 0;
    for (int i = 0; i + K - 1 < sz(S); i++) {
        if (S[i] == '-') {
            cnt++;
            for (int j = 0; j < K; j++) {
                S[i + j] = ((S[i + j] == '+') ? '-' : '+');
            }
        }
    }

    if (find(S.begin(), S.end(), '-') == S.end()) {
        cout << cnt << endl;
    }
    else {
        cout << "IMPOSSIBLE" << endl;
    }
}

int main() {
    int TC;
    cin >> TC;
    for (int tc = 1; tc <= TC; tc++) {
        cin >> S >> K;
        cout << "Case #" << tc << ": ";
        solve();
    }
    return 0;
}
