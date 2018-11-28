#include <iostream>
#include <vector>

using namespace std;

int main() {
    int t, r, c;
    int row[2][4];
    cin >> t;
    for (int case_num=1; case_num<=t; case_num++) {
        vector<int> candidates;
        cout << "Case #" << case_num << ": ";
        for (int i=0; i<2; i++) {
            cin >> r;
            for (int y=0; y<4; y++) {
                for (int x=0; x<4; x++) {
                    cin >> c;
                    if (r == y+1) {
                        row[i][x] = c;
                    }
                }
            }
        }
        for (int i=0; i<4; i++) {
            for (int j=0; j<4; j++) {
                if (row[0][i] == row[1][j]) {
                    candidates.push_back(row[0][i]);
                }
            }
        }
        if (candidates.size() > 1) {
            cout << "Bad magician!" << endl;
        }
        else if (candidates.size() == 0) {
            cout << "Volunteer cheated!" << endl;
        }
        else {
            cout << candidates[0] << endl;
        }
    }
    return 0;
}
