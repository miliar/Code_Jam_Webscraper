#include <bits/stdc++.h>

using namespace std;

int T;

string S;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B.out", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> S;
        int j = S.size();
        while (j >= 1 && S[j - 1] == '+') --j;
        int res = 0;
        for (int i = 0; i < j; ++i)
            if (i == 0 || S[i] != S[i - 1])
                ++res;
        cout << "Case #" << t << ": " << res << endl;
    }
}
