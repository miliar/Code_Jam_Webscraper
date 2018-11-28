#include <bits/stdc++.h>

using namespace std;

int N;
char S[1005];

int solve() {
    int ans = 0;

    int sum = S[0] - '0';
    for (int i = 1, len = strlen(S); i < len; i++) {
        int x = S[i] - '0';

        if (i - sum >= 0) {
            ans += i - sum;
            sum += x + i - sum;
        } else {
            sum += x;
        }
    }

    return ans;
}

int main() {
    freopen("test.in", "r", stdin);
    cin.sync_with_stdio(0);

    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        cin >> N;
        cin >> S;
        cout << "Case #" << i << ": " << solve() << '\n';
    }


    return  0;
}
