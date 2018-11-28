#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int a[4][4];
int b[4][4];
int T, A, B;

void solve() {
    int res, count = 0;
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            if (a[A-1][i] == b[B-1][j]) {
                ++count;
                res = a[A-1][i];
            }
        }
    }
    if (count == 0) {
        cout << "Volunteer cheated!" << endl;
    } else if (count == 1) {
        cout << res << endl;
    } else {
        cout << "Bad magician!" << endl;
    }
}

int main() {
    //freopen("a.input", "r", stdin);
    cin >> T;
    for (int caseId = 1; caseId <= T; ++caseId) {
        cin >> A;
        for (int i = 0; i < 4; ++i) 
            for (int j = 0; j < 4; ++j) 
                cin >> a[i][j];

        cin >> B;
        for (int i = 0; i < 4; ++i) 
            for (int j = 0; j < 4; ++j) 
                cin >> b[i][j];
        
        cout << "Case #" << caseId << ": ";
        solve();
    }
    return 0;
}
