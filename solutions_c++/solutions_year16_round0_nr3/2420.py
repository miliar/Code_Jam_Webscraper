#include <bits/stdc++.h>

using namespace std;

bool t[16];
int proofs[11];

int main() {
    freopen("output.txt", "w", stdout);
    iostream::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cout << "Case #1:\n";
    int cnt = 0;
    for (int i = (1 << 15); i < (1 << 16); i++) {
        if (i % 2 == 0) {
            continue;
        }
        for (int j = 0; j < 16; j++) {
            t[j] = ((i >> j) & 1);
        }
        bool flag = 0;
        for (int k = 2; k <= 10; k++) {
            long long r = 0;
            long long x = 1;
            for (int p = 0; p < 16; p++) {
                r += x * t[p];
                x *= k;
            }
            proofs[k] = -1;
            for (long long j = 2; j * j <= r; j++) {
                if (r % j == 0) {
                    proofs[k] = j;
                    break;
                }
            }
            if (proofs[k] == -1) {
                flag = 1;
                break;
            }
        }
        if (flag) {
            continue;
        }
        for (int j = 0; j < 16; j++) {
            cout << t[15 - j];
        }
        for (int j = 2; j <= 10; j++) {
            cout << " " << proofs[j];
        }
        cout << "\n";
        cnt++;
        if (cnt == 50) {
            return 0;
        }
    }
}

