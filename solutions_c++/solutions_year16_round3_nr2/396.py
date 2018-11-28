#include <bits/stdc++.h>

using namespace std;

void solve()
{
    int b;
    long long m;
    cin >> b >> m;
    long long power = 1;
    int st = 0;

    while (power <= m) {
        power *= 2;
        st++;
    }
    st--;
    power /= 2;

    if (b < st + 2) {
        cout << "IMPOSSIBLE\n";
        return;
    }

    vector <vector <int> > res(b, vector <int>(b));

    for (int i = 0; i < st + 2; i++) {
        for (int j = i + 1; j < st + 2; j++) {
            res[i][j] = 1;
        }
    }

    if (power != m) {
        if (b < st + 3) {
            cout << "IMPOSSIBLE\n";
            return;
        }

        for (int i = 1; i < st + 2; i++) {
            if ((m >> (i - 1)) & 1) {
                res[i][st + 2] = 1;
            }
        }
    }

    for (int i = st + 1; i < b - 1; i++) {
        res[i][i + 1] = 1;
    }

    cout << "POSSIBLE\n";

    for (int i = 0; i < b; i++) {
        for (int j = 0; j < b; j++) {
            cout << res[i][j];
        }
        cout << '\n';
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;

    for (int tst = 0; tst < T; tst++) {
        cout << "Case #" << tst + 1 << ": ";
        solve();
    }
}
