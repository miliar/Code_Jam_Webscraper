#include <iostream>
#include <vector>

using namespace std;

int testCases;

void solve() {
    int row1, row2;
    int arr1[4][4], arr2[4][4];

    cin >> row1;
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            cin >> arr1[i][j];
        }
    }
    cin >> row2;
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            cin >> arr2[i][j];
        }
    }

    int num = 0, matches = 0;
    for (int col1 = 0; col1 < 4; ++col1) {
        for (int col2 = 0; col2 < 4; ++col2) {
            if (arr1[row1-1][col1] == arr2[row2-1][col2]) {
                ++matches;
                num = arr1[row1-1][col1];
            }
        }
    }

    if (matches == 1) {
        cout << num << "\n";
    }
    else if (matches == 0) {
        cout << "Volunteer cheated!\n";
    }
    else {
        cout << "Bad magician!\n";
    }
}

int main() {
    cin >> testCases;
    for (int i = 1; i <= testCases; ++i) {
        cout << "Case #" << i << ": ";
        solve();
    }
}

