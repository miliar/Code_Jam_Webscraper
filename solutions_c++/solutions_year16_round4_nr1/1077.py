#include <bits/stdc++.h>

using namespace std;

int d[13][3][3];

bool check(int n, int i, int r, int p, int s)
{
    return d[n][i][0] == r && d[n][i][1] == p && d[n][i][2] == s;
}

string getres(int n, int i)
{
    if (n == 0) {
        if (i == 0) {
            return "R";
        } else if (i == 1) {
            return "P";
        } else {
            return "S";
        }
    } else {
        string s1 = getres(n - 1, i);
        string s2 = getres(n - 1, (i + 2) % 3);
        return (s1 < s2 ? s1 + s2 : s2 + s1);
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            d[0][i][j] = (i == j);
        }
    }

    for (int k = 1; k <= 12; k++) {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                d[k][i][j] = d[k - 1][i][j] + d[k - 1][(i + 2) % 3][j];
            }
        }
    }

    int T;
    cin >> T;

    for (int tst = 0; tst < T; tst++) {
        int n, r, p, s;
        cin >> n >> r >> p >> s;
        cout << "Case #" << tst + 1 << ": ";
        bool good = false;

        for (int i = 0; i < 3; i++) {
            if (check(n, i, r, p, s)) {
                good = true;
                cout << getres(n, i) << '\n';
                break;
            }
        }

        if (!good) {
            cout << "IMPOSSIBLE\n";
        }
    }
}
