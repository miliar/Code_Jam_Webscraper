#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const int N = 16;
const int J = 50;

ll power[12][35];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0), cout.tie(0), cout.precision(15);

    for (int b = 2; b <= 10; b++) {
        power[b][0] = 1;
        for (int e = 1; e < 35; e++)
            power[b][e] = b * power[b][e-1];
    }

    cout << "Case #1:\n";

    int got = 0;

    for (ll val = (1ll << (N - 1)) + 1; ; val += 2) {
        bool succ = true;
        vector<ll> div(11);

        for (int b = 2; b <= 10; b++) {
            ll conv = 0;
            for (int i = 0; i < N; i++) {
                if ((val >> i)&1)
                    conv += power[b][i];
            }

            succ = false;

            for (ll d = 2; d * d <= conv; d++) {
                if (conv % d == 0) {
                    succ = true;
                    div[b] = d;
                    break;
                }
            }

            if (!succ) break;
        }

        if (succ) {
            for (int i = 0; i < N; i++) {
                cout << ((val >> (N - 1 - i))&1);
            }

            for (int b = 2; b <= 10; b++)
                cout << " " << div[b];
            cout << endl;

            if (++got == J) break;
        }
    }
}

