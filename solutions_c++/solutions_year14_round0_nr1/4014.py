#include <iostream>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int tc = 0; tc < t; tc++) {
        int poss[2][4];
        int r, temp;
        for (int i = 0; i < 2; i++) {
            cin >> r;
            for (int j = 0; j < 4; j++) {
                for (int k = 0; k < 4; k++) {
                    if (j == r-1)
                        cin >> poss[i][k];
                    else
                        cin >> temp;
                }
            }
        }
        int matches = 0, ans;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if ( poss[0][i] == poss[1][j]) {
                    matches++;
                    ans = poss[0][i];
                }
            }
        }
        cout << "Case #" << tc + 1<< ": ";
        if (matches == 1)
            cout << ans;
        else if (matches == 0)
            cout << "Volunteer cheated!";
        else
            cout << "Bad magician!";
        cout << endl;
    }
    return 0;
}