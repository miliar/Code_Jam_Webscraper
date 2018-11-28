#include <string>
#include <iostream>

using namespace std;

string solve(int P, int R, int S) {
    if (P + R + S == 1) {
        if (P == 1) {
            return "P";
        } else if (R == 1) {
            return "R";
        }
        return "S";
    }
    int PR = (P + R - S);
    int PS = (P + S - R);
    int RS = (R + S - P);
    if (PR < 0 || PS < 0 || RS < 0) {
        return "IMPOSSIBLE";
    }
    PR /= 2;
    PS /= 2;
    RS /= 2;
    string mid = solve(PR, PS, RS);
    if (mid == "IMPOSSIBLE") {
        return mid;
    }
    string res = "";
    for (auto const &c: mid) {
        if (c == 'P') {
            res += "PR";
        } else if (c == 'R') {
            res += "PS";
        } else {
            res += "RS";
        }
    }
    return res;
}

int main() {
    int T;
    cin >> T;
    for (int z = 1; z <= T; ++z) {
        cout << "Case #" << z << ": ";
        int n;
        cin >> n;
        int R, P, S;
        cin >> R >> P >> S;
        cout << solve(P, R, S) << endl;
    }
    return 0;
}
