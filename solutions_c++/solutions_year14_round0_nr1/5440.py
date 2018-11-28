#include <iostream>
#include <algorithm>
#include <set>
#include <vector>

using namespace std;

int A[4][4], B[4][4];

int main() {
    ios_base::sync_with_stdio(0);

    int t;
    cin >> t;
    for (int c = 1; c <= t; c++) {
        int r1, r2;
        cin >> r1;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin >> A[i][j];
            }
        }
        cin >> r2;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin >> B[i][j];
            }
        }

        set<int> orig;
        for (int j = 0; j < 4; j++) {
            orig.insert(A[r1-1][j]);
        }

        vector<int> comm;
        for (int j = 0; j < 4; j++) {
            if (orig.count(B[r2-1][j]))
                comm.push_back(B[r2-1][j]);
        }

        if (comm.size() > 1)
            cout << "Case #" << c << ": " << "Bad magician!\n";
        else if (comm.size() < 1)
            cout << "Case #" << c << ": " << "Volunteer cheated!\n";
        else
            cout << "Case #" << c << ": " << comm[0] << "\n";
    }
    return 0;
}

