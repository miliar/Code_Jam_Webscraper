#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("infile.in", "r", stdin);
    freopen("outfile.txt", "w", stdout);

    int t;

    cin >> t;

    int p = 1;

    while (t--) {
        int k;
        cin >> k;
        int a[4][4];
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin >> a[i][j];
            }
        }
        int k1;
        cin >> k1;
        int a1[4][4];
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin >> a1[i][j];
            }
        }
        int cnt = 0;
        int q = 0;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (a[k - 1][i] == a1[k1 - 1][j]) {
                    q = a[k - 1][i];
                    cnt++;
                }
            }
        }
        if (cnt == 1) {
            cout << "Case #" << p << ": " << q << endl;
        }
        if (cnt == 0) {
            cout << "Case #" << p << ": " << "Volunteer cheated!" << endl;
        }
        if (cnt > 1) {
            cout << "Case #" << p << ": " << "Bad magician!" << endl;
        }

        p++;
    }

    return 0;
}
