#include <bits/stdc++.h>
using namespace std;

#define INF 2000000000
#define maxN 1005

int TC;
int X, R, C;

int main() {
    #ifndef ONLINE_JUDGE
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("test.out", "w", stdout);
    #endif // ONLINE_JUDGE

    cin >> TC;
    for (int cs = 0; cs < TC; cs++) {
        cin >> X >> R >> C;
        if ((R * C % X != 0)
                || (X > R && X > C)
                || ((X + 1) / 2 > R || (X + 1) / 2 > C)
                || (X == 4 && (R < 3 || C < 3))) {
            cout << "Case #" << cs + 1 << ": RICHARD" << endl;
        } else {
            cout << "Case #" << cs + 1 << ": GABRIEL" << endl;
        }
    }

    return 0;
}
