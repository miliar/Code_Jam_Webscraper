#include <iostream>

using namespace std;

void solve_1(int j) {
    int cards[16] = {};
    bool first[16] = {};
    bool second[16] = {};

    int row;
    cin >> row;
    for (int i = 0; i < 16; i++) cin >> cards[i];
    for (int i = 0; i < 4; i++) first[cards[4 * (row - 1) + i]-1] = true;

    cin >> row;
    for (int i = 0; i < 16; i++) cin >> cards[i];
    for (int i = 0; i < 4; i++) second[cards[4 * (row - 1) + i]-1] = true;


    int idx = -1;
    for (int i = 0; i < 16; i++) {
        if (first[i] && second[i]) {
            if (idx == -1) {
                idx = i;
            }
            else {
                cout << "Case #" << j << ": Bad magician!" << endl;
                return;
            }
        }
    }
    if (idx == -1) cout << "Case #" << j << ": Volunteer cheated!" << endl;
    else cout << "Case #" << j << ": " << (idx+1) << endl;
}


int main(void) {
    int c;
    cin >> c;

    for (int i = 0; i < c; i++)
        solve_1(i + 1);
}