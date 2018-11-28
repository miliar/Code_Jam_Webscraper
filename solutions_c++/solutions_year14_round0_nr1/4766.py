#include <iostream>
#include <cstdio>

using namespace std;

int T;
int a, b, ta[5][5], tb[5][5];
int res, f;

void solve() {
    cin >> a;
    for (int i = 1; i <= 4; i++)
        for (int j = 1; j <= 4; j++)
            cin >> ta[i][j];

    cin >> b;
    for (int i = 1; i <= 4; i++)
        for (int j = 1; j <= 4; j++)
            cin >> tb[i][j];

    res = 0; f = 0;
    for (int i = 1; i <= 4; i++)
        for (int j = 1; j <= 4; j++)
            if (ta[a][i] == tb[b][j])
                if (res == 0) {
                    res = ta[a][i];
                    f = 1;
                }
                else
                    f = 2;
    switch (f) {
        case 0: cout << "Volunteer cheated!";
        break;
        case 1: cout << res;
        break;
        case 2: cout << "Bad magician!";
        break;
    }
}

int main() {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    cin >> T;
    for (int i = 1; i <= T; i++) {
        cout << "Case #" << i << ": ";
        solve();
        cout << endl;
    }


}
