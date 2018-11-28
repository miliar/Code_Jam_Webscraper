#include <iostream>

using namespace std;

int T, m, n, a[5][5], b[5][5], s, ans;

int main() {
    cin >> T;
    for (int ti = 1; ti <= T; ++ti) {
        s = 0;
        cin >> m;
        for (int i = 1; i <= 4; ++i)
            for (int j = 1; j <= 4; ++j)
                cin >> a[i][j];
        cin >> n;
        for (int i = 1; i <= 4; ++i)
            for (int j = 1; j <= 4; ++j)
                cin >> b[i][j];
        for (int i = 1; i <= 4; ++i)
            for (int j = 1; j <= 4; ++j)
                if (a[m][i] == b[n][j]) {
                    s++;
                    ans = a[m][i];
                }
        cout << "Case #" << ti << ": ";
        if (s == 1)
            cout << ans << endl;
        else if (s == 0)
            cout << "Volunteer cheated!" << endl;
        else
            cout << "Bad magician!" << endl;
    }
    return 0;
}
