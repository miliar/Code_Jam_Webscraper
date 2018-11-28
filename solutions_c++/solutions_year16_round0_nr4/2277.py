#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0), cout.tie(0), cout.precision(15);

    int T;
    cin >> T;

    for (int tc = 1; tc <= T; tc++) {
        ll K, C, S;
        cin >> K >> C >> S;

        ll exp = 1;
        for (int i = 0; i < C - 1; i++)
            exp *= K;

        cout << "Case #" << tc << ": ";
        if (S < K) {
            cout << "fk u dudu\n";
        } else {
            for (int i = 0; i < S; i++)
                cout << 1 + i * exp << " ";
            cout << endl;
        }
    }
}

