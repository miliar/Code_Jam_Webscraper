#include <iostream>
#include <vector>
using namespace std;
int main () {
    int T;
    cin >> T;
    for (int C = 1; C<= T; C++) {
        int r[2];
        int f[2][4][4];
        for (int i = 0; i < 2; i++) {
            cin >> r[i];
            r[i]--;
            for (int k = 0; k < 4; k++) {
                for (int j = 0; j < 4; j++) {
                    cin >> f[i][k][j];
                }
            }
        }
        std::vector<int> s;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (f[0][r[0]][i] == f[1][r[1]][j]) {
                    s.push_back(f[0][r[0]][i]);
                    break;
                }
            }
        }
        cout << "Case #" << C << ": ";
        if (s.size() == 1) cout << s[0] << endl;
        else if (s.size() > 1) cout << "Bad magician!" << endl;
        else cout << "Volunteer cheated!" << endl;
    }
}
