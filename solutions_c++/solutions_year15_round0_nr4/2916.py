#include <iostream>
#include <string>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int caseNum = 1; caseNum <= T; ++caseNum) {
        int X, R, C;
        cin >> X >> R >> C;
        cout << "Case #" << caseNum << ": ";
        if (X == 1) cout << "GABRIEL";
        else if (X == 2) {
            if (R*C % 2 != 0) cout << "RICHARD";
            else cout  << "GABRIEL";
        }
        else if (X == 3) {
            if (R*C % 3 != 0) cout << "RICHARD";
            else if (R*C == 3) cout << "RICHARD";
            else cout  << "GABRIEL";
        }
        else if (X == 4) {
            if (R < 3 || C < 3) cout << "RICHARD";
            else if (R == 3 && C == 3) cout << "RICHARD";
            else cout  << "GABRIEL";
        }
        cout << endl;
    }
}
