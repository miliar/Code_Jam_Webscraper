#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int _c = 0; _c < T; _c++) {
        int r1;
        int a1[4][4];
        cin >> r1; r1--;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin >> a1[i][j];
            }
        }
        int r2;
        int a2[4][4];
        cin >> r2; r2--;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin >> a2[i][j];
            }
        }
        int answer = 0;
        bool bad = false;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (a1[r1][i] == a2[r2][j]) {
                    if (answer != 0) bad = true;
                    answer = a1[r1][i];
                }
            }
        }
        cout << "Case #" << _c+1 << ": ";
        if (bad) {
            cout << "Bad magician!";
        }
        else if (answer == 0) {
            cout << "Volunteer cheated!";
        }
        else {
            cout << answer;
        }
        cout << endl;
    }
}
