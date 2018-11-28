#include <iostream>
#include <sstream>
#include <string>
using namespace std;

string solve() {
    int a1, a2;
    int R1[4][4], R2[4][4];
    
    cin >> a1; a1--;
    for (int i = 0; i < 4; i++) for (int j = 0; j < 4; j++)
        cin >> R1[i][j];
    cin >> a2; a2--;
    for (int i = 0; i < 4; i++) for (int j = 0; j < 4; j++)
        cin >> R2[i][j];

    int num = -1;
    for (int j1 = 0; j1 < 4; j1++)
        for (int j2 = 0; j2 < 4; j2++) {
            if (R1[a1][j1] == R2[a2][j2]) {
                if (num != -1) return "Bad magician!";
                num = R1[a1][j1]; 
            }
        }

    if (num == -1) return "Volunteer cheated!";
    ostringstream convert;
    convert << num;
    return convert.str();
}

int main() {
    int t;
    cin >> t;
    for (int qq = 1; qq <= t; qq++) {
        cout << "Case #" << qq << ": " << solve() << endl;
    }
}
