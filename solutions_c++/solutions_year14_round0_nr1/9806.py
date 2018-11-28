#include<iostream>
#include<cstdio>
using namespace std;
int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    int T, case_n = 1;
    cin >> T;
    while(T--) {
        int r1, r2, i, j, a[4][4], b[4][4], ans, matched = 0;
        cin >> r1;
        for(i=0;i<4;i++) {
            for(j=0;j<4;j++) {
                cin >> a[i][j];
            }
        }

        cin >> r2;
        for(i=0;i<4;i++) {
            for(j=0;j<4;j++) {
                cin >> b[i][j];
            }
        }

        for(i=0;i<4;i++) {
            for(j=0;j<4;j++) {
                if(a[r1-1][i] == b[r2-1][j]) {
                    matched++;
                    ans = a[r1-1][i];
                }
            }
        }

        cout << "Case #" << case_n <<  ": ";

        if (matched == 1) {
            cout << ans;
        } else if (matched == 0) {
            cout << "Volunteer cheated!";
        } else {
            cout << "Bad magician!";
        }

        cout << endl;
        case_n++;
    }
}
