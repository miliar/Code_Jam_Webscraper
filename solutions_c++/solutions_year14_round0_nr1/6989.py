#include <iostream>
using namespace std;

int magia (int row_a[], int row_b[]) {
    int k = -2;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (row_a[i] == row_b[j]) {
                if (k == -2) {
                    k = i;
                    break;
                }
                else {
                    return -1;
                }
            }
        }
    }
    return k;
}

int main () {
    int T;
    cin >> T;
    
    for (int icase = 1; icase <= T; icase++) {
        int row_a, row_b;
        int rows_a[4][4];
        int rows_b[4][4];
        cin >> row_a;
        row_a--;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin >> rows_a[i][j];
            }
        }
        cin >> row_b;
        row_b--;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin >> rows_b[i][j];
            }
        }
        int answer = magia(rows_a[row_a], rows_b[row_b]);
        cout << "Case #" << icase << ": ";
        if (answer >= 0) {
            cout << rows_a[row_a][answer];
        }
        else if (answer == -1) {
            cout << "Bad magician!";
        }
        else {
            cout << "Volunteer cheated!";
        }
        cout << endl;
    }

    return 0;
}

