#include <iostream>

using namespace std;

int read_board() {
    int row, n, f = 0;
    cin >> row;
    for (int r=1; r<=4; r++) {
        for (int c=1; c<=4; c++) {
            cin >> n;
            if (r == row) {
                f |= 1<<n;
            }
        }
    }
    return f;
}

int main() {
    int T;

    cin >> T;
    for (int t=1; t<=T; t++) {
        cout << "Case #" << t << ": ";
        int f = read_board();
        int g = read_board();
        
        int res = 0;
        for (int i=1; i<=16; i++) {
            if (f & g & 1<<i) {
                if (res == 0) {
                    res = i;
                }
                else {
                    res = -1;
                    break;
                }
            }
        }
        if (res > 0) cout << res << endl;
        else if (res == 0) cout << "Volunteer cheated!" << endl;
        else cout << "Bad magician!" << endl;
    }
    return 0;
} 
