#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int t=1; t<=T; ++t) {
        int r1, r2;
        int q1[4][4];
        int q2[4][4];
        cin >> r1;
        r1--;
        for (int i=0; i<4; ++i) {
            for (int j=0; j<4; ++j) {
                cin >> q1[i][j];
            }
        }
        cin >> r2;
        r2--;
        for (int i=0; i<4; ++i) {
            for (int j=0; j<4; ++j) {
                cin >> q2[i][j];
            }
        }
        int oknum = 0;
        int ans = -1;
        for (int i=0; i<4; ++i) {
            int thisoknum = 0;
            for (int j=0; j<4; ++j) {
                if (q1[r1][i] == q2[r2][j]) {
                    thisoknum++;
                }
            }
            if (thisoknum > 0) {
                ans = q1[r1][i];
            }
            oknum += thisoknum;
        }
        cout << "Case #" << t << ": ";
        if (oknum < 1) {
            cout << "Volunteer cheated!";
        } else if (oknum == 1) {
            cout << ans;
        } else if (oknum > 1) {
            cout << "Bad magician!";
        }
        cout << endl;
    }
    return 0;
}
