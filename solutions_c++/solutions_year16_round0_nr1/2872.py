#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0), cout.tie(0), cout.precision(15);

    int T;
    cin >> T;

    for (int tc = 1; tc <= T; tc++) {
        cout << "Case #" << tc << ": ";

        int N;
        cin >> N;

        if (N == 0) {
            cout << "INSOMNIA\n";
            continue;
        }

        vector<bool> seen(10);

        for (int num = N; ; num += N) {
            for (int tmp = num; tmp; tmp /= 10)
                seen[tmp % 10] = true;

            bool all = true;
            for (bool b : seen)
                all &= b;

            if (all) {
                cout << num << "\n";
                break;
            }
        }
    }
}

