#include <iostream>
#include <cstdio>

using namespace std;

int a[5][5], b[5][5];

int main() {
    int t, k = 0;
    cin >> t;
    while (t--) {
        int x, y;
        cin >> x;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                cin >> a[i][j];
        cin >> y;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                cin >> b[i][j];
        int ans = 0, pos;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++) {
                if (a[x-1][i] == b[y-1][j]) {
                    ans++;
                    pos = i;
                }
            }
        printf("Case #%d: ", ++k);
        if (ans == 1) cout << a[x-1][pos] << endl;
        else if (ans > 1) cout << "Bad magician!" << endl;
        else cout << "Volunteer cheated!" << endl;
    }
    return 0;
}
