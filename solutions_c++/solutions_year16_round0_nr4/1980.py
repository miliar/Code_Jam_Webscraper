#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;

ll ans[105];
int cnt;

void go(int casenum) {
    int K, C, S;
    cin >> K >> C >> S;
    cnt = 0;
    for (int i = 0; i < K; ) {
        ll cur = 0;
        for (int j = 0; j < C; j++) {
            cur *= K;
            cur += min(i, K - 1);
            i++;
        }
        ans[cnt++] = cur;
    }

    if (cnt > S) cout << "Case #" << casenum << ": IMPOSSIBLE\n";
    else {
        cout << "Case #" << casenum << ": ";
        for (int i = 0; i < cnt; i++) {
            cout << ans[i] + 1;
            if (i < cnt - 1) cout << ' ';
            else cout << '\n';
        }
    }
}

int main() {
    int t; cin >> t;
    for (int i = 1; i <= t; i++) go(i);
}
